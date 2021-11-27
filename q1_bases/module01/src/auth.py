import argon2
from PySide6.QtCore import QTimer, Signal
from PySide6.QtWidgets import QWidget

from public.i18n import errors, translations
from src.components.database import db
from src.components.multithreading import Worker, pool
from src.ui.auth_ui import Ui_Form
from src.utils.error_handlers import qt_error_handler
from src.utils.get_current_qdate import get_current_qdate
from src.utils.get_echo_mode import get_echo_mode
from src.utils.logger import Logger
from src.utils.verifier import verify_account, verify_profile

log = Logger(__name__)
ph = argon2.PasswordHasher()


class AuthWindow(QWidget):
    on_user = Signal(dict)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._attempt = 0
        self._user = None
        self._reset_date()

        self.ui.button_signin_next.clicked.connect(self.signin_router)
        self.ui.button_signup_next.clicked.connect(self.signup_router)

        self.ui.button_signin_signup.clicked.connect(lambda: self.reset("signin"))
        self.ui.button_signup_signin.clicked.connect(lambda: self.reset("signup"))

        self.ui.checkbox_signin_showpassword.stateChanged.connect(
            lambda state: (
                self.ui.input_signin_password.setEchoMode(get_echo_mode(state))
            )
        )
        self.ui.checkbox_signup_showpassword.stateChanged.connect(
            lambda state: (
                self.ui.input_signup_password.setEchoMode(get_echo_mode(state)),
                self.ui.input_signup_confirm.setEchoMode(get_echo_mode(state)),
            )
        )

        self.ui.checkbox_tos.toggled.connect(self.ui.button_signup_next.setEnabled)

    def on_reject(self, err_msg):
        qt_error_handler(self, err_msg)

    def _reset_date(self):
        date = get_current_qdate()
        self.ui.date_birthday.setDate(date)
        self.ui.date_birthday.setMaximumDate(date)

    def _reset_signin(self):
        self.ui.label_signin.setText(translations.signin())
        self.ui.label_use.setText(translations.use_signin())

        self.ui.input_signin_username.setText("")
        self.ui.input_signin_password.setText("")
        self.ui.checkbox_signin_showpassword.setChecked(False)

        self.ui.stacked_signin_body.setCurrentIndex(0)
        self.ui.stacked_auth_method.setCurrentIndex(1)

    def _reset_signup(self):
        self.ui.input_signup_firstname.setText("")
        self.ui.input_signup_lastname.setText("")
        self.ui.input_signup_username.setText("")
        self.ui.input_signup_password.setText("")
        self.ui.input_signup_confirm.setText("")
        self.ui.checkbox_signup_showpassword.setChecked(False)
        self.ui.checkbox_tos.setChecked(False)
        self.ui.spinbox_signup_weight.setValue(0)
        self.ui.spinbox_signup_height.setValue(0)
        self.ui.combobox_signup_activity.setCurrentIndex(-1)

        self.ui.buttonGroup.setExclusive(False)
        self.ui.button_signup_male.setChecked(False)
        self.ui.button_signup_female.setChecked(False)
        self.ui.buttonGroup.setExclusive(True)

        self._reset_date()

        self.ui.stacked_signup_body.setCurrentIndex(0)
        self.ui.stacked_auth_method.setCurrentIndex(0)

    def reset(self, page):
        log.warning("reset")
        self.ui.retranslateUi(self)
        self._user = None

        match page:
            case "signin":
                self._reset_signin()
            case "signup":
                self._reset_signup()

    def _username_handler(self):
        username = self.ui.input_signin_username.text().strip()

        def on_resolve(user):
            self._user = user
            self.ui.label_signin.setText(translations.welcome())
            self.ui.label_use.setText(username)
            self.ui.stacked_signin_body.setCurrentIndex(1)

        worker = Worker(db.get_user, username)
        worker.signals.resolve.connect(on_resolve)
        worker.signals.reject.connect(self.on_reject)
        pool.run(worker)

    def _password_handler(self):
        try:
            ph.verify(self._user["password"], self.ui.input_signin_password.text())
        except argon2.exceptions.VerifyMismatchError:
            return self._throttle_on_wrong_password()

        self.on_user.emit(self._user)

    def _throttle_on_wrong_password(self):
        self._attempt += 1
        throttle_time = 5 * (self._attempt - 2) ** 2

        if self._attempt < 3:
            return qt_error_handler(self, errors.wrong_password())

        self.ui.button_signin_next.setDisabled(True)
        qt_error_handler(self, errors.wrong_password_throttle(throttle_time))
        QTimer.singleShot(
            1e3 * throttle_time,
            lambda: self.ui.button_signin_next.setEnabled(True),
        )

    def signin_router(self):
        match self.ui.stacked_signin_body.currentIndex():
            case 0:
                self._username_handler()
            case 1:
                self._password_handler()

    def _account_handler(self):
        username = self.ui.input_signup_username.text().strip()

        try:
            self._user = verify_account(
                firstname=self.ui.input_signup_firstname.text().strip(),
                lastname=self.ui.input_signup_lastname.text().strip(),
                username=username,
                password=self.ui.input_signup_password.text().strip(),
                confirm=self.ui.input_signup_confirm.text().strip(),
            )
        except ValueError as err:
            return qt_error_handler(self, err.args[0])

        def on_resolve():
            qt_error_handler(self, errors.username_taken())

        def on_reject():
            self.ui.stacked_signup_body.setCurrentIndex(1)

        worker = Worker(db.get_user, username)
        worker.signals.resolve.connect(on_resolve)
        worker.signals.reject.connect(on_reject)
        pool.run(worker)

    def _profile_handler(self):
        try:
            profile = verify_profile(
                weight=self.ui.spinbox_signup_weight,
                height=self.ui.spinbox_signup_height,
                birthday=self.ui.date_birthday,
                sex=[self.ui.button_signup_male, self.ui.button_signup_female],
                activity=self.ui.combobox_signup_activity,
            )
        except ValueError as err:
            return qt_error_handler(self, err.args[0])

        self._user.update(profile)

        def on_resolve():
            self.on_user.emit(self._user)

        worker = Worker(db.add_user, self._user)
        worker.signals.resolve.connect(on_resolve)
        worker.signals.reject.connect(self.on_reject)
        pool.run(worker)

    def signup_router(self):
        match self.ui.stacked_signup_body.currentIndex():
            case 0:
                self._account_handler()
            case 1:
                self._profile_handler()
