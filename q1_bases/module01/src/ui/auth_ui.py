# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1280, 693)
        font = QFont()
        font.setPointSize(16)
        Form.setFont(font)
        Form.setWindowTitle("Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(10, 75, 10, 10)
        self.app_label = QLabel(Form)
        self.app_label.setObjectName("app_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_label.sizePolicy().hasHeightForWidth())
        self.app_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(48)
        font1.setBold(True)
        self.app_label.setFont(font1)
        self.app_label.setText("la calorie")
        self.app_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.app_label)

        self.stacked_auth_method = QStackedWidget(Form)
        self.stacked_auth_method.setObjectName("stacked_auth_method")
        sizePolicy.setHeightForWidth(
            self.stacked_auth_method.sizePolicy().hasHeightForWidth()
        )
        self.stacked_auth_method.setSizePolicy(sizePolicy)
        self.container_signin = QWidget()
        self.container_signin.setObjectName("container_signin")
        sizePolicy.setHeightForWidth(
            self.container_signin.sizePolicy().hasHeightForWidth()
        )
        self.container_signin.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.container_signin)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(426, 25, 426, 0)
        self.container_signin_header = QWidget(self.container_signin)
        self.container_signin_header.setObjectName("container_signin_header")
        sizePolicy.setHeightForWidth(
            self.container_signin_header.sizePolicy().hasHeightForWidth()
        )
        self.container_signin_header.setSizePolicy(sizePolicy)
        self.layout_signin_header = QVBoxLayout(self.container_signin_header)
        self.layout_signin_header.setSpacing(0)
        self.layout_signin_header.setObjectName("layout_signin_header")
        self.layout_signin_header.setContentsMargins(0, 0, 0, 0)
        self.label_signin = QLabel(self.container_signin_header)
        self.label_signin.setObjectName("label_signin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.label_signin.sizePolicy().hasHeightForWidth()
        )
        self.label_signin.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_signin.setFont(font2)
        self.label_signin.setAlignment(Qt.AlignCenter)

        self.layout_signin_header.addWidget(self.label_signin)

        self.label_use = QLabel(self.container_signin_header)
        self.label_use.setObjectName("label_use")
        sizePolicy1.setHeightForWidth(self.label_use.sizePolicy().hasHeightForWidth())
        self.label_use.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.label_use.setFont(font3)
        self.label_use.setAlignment(Qt.AlignCenter)

        self.layout_signin_header.addWidget(self.label_use)

        self.verticalLayout_2.addWidget(self.container_signin_header)

        self.spacer_signin_body = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum
        )

        self.verticalLayout_2.addItem(self.spacer_signin_body)

        self.stacked_signin_body = QStackedWidget(self.container_signin)
        self.stacked_signin_body.setObjectName("stacked_signin_body")
        sizePolicy1.setHeightForWidth(
            self.stacked_signin_body.sizePolicy().hasHeightForWidth()
        )
        self.stacked_signin_body.setSizePolicy(sizePolicy1)
        self.container_signin_username = QWidget()
        self.container_signin_username.setObjectName("container_signin_username")
        self.verticalLayout_3 = QVBoxLayout(self.container_signin_username)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.input_signin_username = QLineEdit(self.container_signin_username)
        self.input_signin_username.setObjectName("input_signin_username")
        self.input_signin_username.setMaxLength(63)
        self.input_signin_username.setClearButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.input_signin_username)

        self.spacer_username = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.spacer_username)

        self.stacked_signin_body.addWidget(self.container_signin_username)
        self.container_signin_password = QWidget()
        self.container_signin_password.setObjectName("container_signin_password")
        sizePolicy.setHeightForWidth(
            self.container_signin_password.sizePolicy().hasHeightForWidth()
        )
        self.container_signin_password.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.container_signin_password)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.input_signin_password = QLineEdit(self.container_signin_password)
        self.input_signin_password.setObjectName("input_signin_password")
        self.input_signin_password.setMaxLength(127)
        self.input_signin_password.setEchoMode(QLineEdit.Password)
        self.input_signin_password.setClearButtonEnabled(False)

        self.verticalLayout_4.addWidget(self.input_signin_password)

        self.checkbox_signin_showpassword = QCheckBox(self.container_signin_password)
        self.checkbox_signin_showpassword.setObjectName("checkbox_signin_showpassword")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.checkbox_signin_showpassword.sizePolicy().hasHeightForWidth()
        )
        self.checkbox_signin_showpassword.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.checkbox_signin_showpassword)

        self.stacked_signin_body.addWidget(self.container_signin_password)

        self.verticalLayout_2.addWidget(self.stacked_signin_body)

        self.container_signin_footer = QWidget(self.container_signin)
        self.container_signin_footer.setObjectName("container_signin_footer")
        sizePolicy.setHeightForWidth(
            self.container_signin_footer.sizePolicy().hasHeightForWidth()
        )
        self.container_signin_footer.setSizePolicy(sizePolicy)
        self.layout_signin_controls = QHBoxLayout(self.container_signin_footer)
        self.layout_signin_controls.setSpacing(0)
        self.layout_signin_controls.setObjectName("layout_signin_controls")
        self.button_signin_signup = QPushButton(self.container_signin_footer)
        self.button_signin_signup.setObjectName("button_signin_signup")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.button_signin_signup.sizePolicy().hasHeightForWidth()
        )
        self.button_signin_signup.setSizePolicy(sizePolicy3)

        self.layout_signin_controls.addWidget(self.button_signin_signup)

        self.spacer_signin_footer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.layout_signin_controls.addItem(self.spacer_signin_footer)

        self.button_signin_next = QPushButton(self.container_signin_footer)
        self.button_signin_next.setObjectName("button_signin_next")
        self.button_signin_next.setEnabled(True)
        sizePolicy3.setHeightForWidth(
            self.button_signin_next.sizePolicy().hasHeightForWidth()
        )
        self.button_signin_next.setSizePolicy(sizePolicy3)

        self.layout_signin_controls.addWidget(self.button_signin_next)

        self.verticalLayout_2.addWidget(self.container_signin_footer)

        self.spacer_signin = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.spacer_signin)

        self.stacked_auth_method.addWidget(self.container_signin)
        self.container_signup = QWidget()
        self.container_signup.setObjectName("container_signup")
        sizePolicy.setHeightForWidth(
            self.container_signup.sizePolicy().hasHeightForWidth()
        )
        self.container_signup.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.container_signup)
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(426, 25, 426, 0)
        self.container_signup_header = QWidget(self.container_signup)
        self.container_signup_header.setObjectName("container_signup_header")
        sizePolicy.setHeightForWidth(
            self.container_signup_header.sizePolicy().hasHeightForWidth()
        )
        self.container_signup_header.setSizePolicy(sizePolicy)
        self.layout_signup_header = QVBoxLayout(self.container_signup_header)
        self.layout_signup_header.setSpacing(0)
        self.layout_signup_header.setObjectName("layout_signup_header")
        self.layout_signup_header.setContentsMargins(0, 0, 0, 0)
        self.label_signup = QLabel(self.container_signup_header)
        self.label_signup.setObjectName("label_signup")
        sizePolicy1.setHeightForWidth(
            self.label_signup.sizePolicy().hasHeightForWidth()
        )
        self.label_signup.setSizePolicy(sizePolicy1)
        self.label_signup.setFont(font2)
        self.label_signup.setAlignment(Qt.AlignCenter)

        self.layout_signup_header.addWidget(self.label_signup)

        self.label_text = QLabel(self.container_signup_header)
        self.label_text.setObjectName("label_text")
        sizePolicy1.setHeightForWidth(self.label_text.sizePolicy().hasHeightForWidth())
        self.label_text.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(14)
        self.label_text.setFont(font4)
        self.label_text.setAlignment(Qt.AlignCenter)

        self.layout_signup_header.addWidget(self.label_text)

        self.verticalLayout_5.addWidget(self.container_signup_header)

        self.stacked_signup_body = QStackedWidget(self.container_signup)
        self.stacked_signup_body.setObjectName("stacked_signup_body")
        sizePolicy.setHeightForWidth(
            self.stacked_signup_body.sizePolicy().hasHeightForWidth()
        )
        self.stacked_signup_body.setSizePolicy(sizePolicy)
        self.stacked_signup_body.setFocusPolicy(Qt.StrongFocus)
        self.container_signup_account = QWidget()
        self.container_signup_account.setObjectName("container_signup_account")
        sizePolicy.setHeightForWidth(
            self.container_signup_account.sizePolicy().hasHeightForWidth()
        )
        self.container_signup_account.setSizePolicy(sizePolicy)
        self.layout_signup_inputs = QGridLayout(self.container_signup_account)
        self.layout_signup_inputs.setSpacing(25)
        self.layout_signup_inputs.setObjectName("layout_signup_inputs")
        self.layout_signup_inputs.setContentsMargins(0, 0, 0, 0)
        self.input_signup_username = QLineEdit(self.container_signup_account)
        self.input_signup_username.setObjectName("input_signup_username")
        self.input_signup_username.setFocusPolicy(Qt.StrongFocus)
        self.input_signup_username.setMaxLength(63)
        self.input_signup_username.setClearButtonEnabled(False)

        self.layout_signup_inputs.addWidget(self.input_signup_username, 1, 0, 1, 2)

        self.input_signup_lastname = QLineEdit(self.container_signup_account)
        self.input_signup_lastname.setObjectName("input_signup_lastname")
        self.input_signup_lastname.setFocusPolicy(Qt.StrongFocus)
        self.input_signup_lastname.setMaxLength(63)
        self.input_signup_lastname.setClearButtonEnabled(False)

        self.layout_signup_inputs.addWidget(self.input_signup_lastname, 0, 1, 1, 1)

        self.input_signup_firstname = QLineEdit(self.container_signup_account)
        self.input_signup_firstname.setObjectName("input_signup_firstname")
        self.input_signup_firstname.setFocusPolicy(Qt.StrongFocus)
        self.input_signup_firstname.setMaxLength(63)
        self.input_signup_firstname.setClearButtonEnabled(False)

        self.layout_signup_inputs.addWidget(self.input_signup_firstname, 0, 0, 1, 1)

        self.container_signup_password = QWidget(self.container_signup_account)
        self.container_signup_password.setObjectName("container_signup_password")
        sizePolicy1.setHeightForWidth(
            self.container_signup_password.sizePolicy().hasHeightForWidth()
        )
        self.container_signup_password.setSizePolicy(sizePolicy1)
        self.layout_signup_password = QGridLayout(self.container_signup_password)
        self.layout_signup_password.setObjectName("layout_signup_password")
        self.layout_signup_password.setHorizontalSpacing(25)
        self.layout_signup_password.setVerticalSpacing(0)
        self.layout_signup_password.setContentsMargins(0, 0, 0, 0)
        self.input_signup_password = QLineEdit(self.container_signup_password)
        self.input_signup_password.setObjectName("input_signup_password")
        self.input_signup_password.setFocusPolicy(Qt.StrongFocus)
        self.input_signup_password.setMaxLength(127)
        self.input_signup_password.setEchoMode(QLineEdit.Password)
        self.input_signup_password.setClearButtonEnabled(False)

        self.layout_signup_password.addWidget(self.input_signup_password, 1, 0, 1, 1)

        self.input_signup_confirm = QLineEdit(self.container_signup_password)
        self.input_signup_confirm.setObjectName("input_signup_confirm")
        self.input_signup_confirm.setFocusPolicy(Qt.StrongFocus)
        self.input_signup_confirm.setMaxLength(127)
        self.input_signup_confirm.setEchoMode(QLineEdit.Password)
        self.input_signup_confirm.setClearButtonEnabled(False)

        self.layout_signup_password.addWidget(self.input_signup_confirm, 1, 1, 1, 1)

        self.checkbox_signup_showpassword = QCheckBox(self.container_signup_password)
        self.checkbox_signup_showpassword.setObjectName("checkbox_signup_showpassword")

        self.layout_signup_password.addWidget(
            self.checkbox_signup_showpassword, 2, 0, 1, 2
        )

        self.layout_signup_inputs.addWidget(self.container_signup_password, 3, 0, 1, 2)

        self.checkbox_tos = QCheckBox(self.container_signup_account)
        self.checkbox_tos.setObjectName("checkbox_tos")
        sizePolicy.setHeightForWidth(self.checkbox_tos.sizePolicy().hasHeightForWidth())
        self.checkbox_tos.setSizePolicy(sizePolicy)
        self.checkbox_tos.setFont(font)
        self.checkbox_tos.setIconSize(QSize(16, 16))

        self.layout_signup_inputs.addWidget(self.checkbox_tos, 4, 0, 1, 2)

        self.stacked_signup_body.addWidget(self.container_signup_account)
        self.container_signup_profile = QWidget()
        self.container_signup_profile.setObjectName("container_signup_profile")
        self.gridLayout_3 = QGridLayout(self.container_signup_profile)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.laabel_signup_age = QLabel(self.container_signup_profile)
        self.laabel_signup_age.setObjectName("laabel_signup_age")

        self.gridLayout_3.addWidget(self.laabel_signup_age, 2, 0, 1, 1)

        self.label_signup_weight = QLabel(self.container_signup_profile)
        self.label_signup_weight.setObjectName("label_signup_weight")
        sizePolicy.setHeightForWidth(
            self.label_signup_weight.sizePolicy().hasHeightForWidth()
        )
        self.label_signup_weight.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_signup_weight, 0, 0, 1, 1)

        self.button_signup_male = QRadioButton(self.container_signup_profile)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.button_signup_male)
        self.button_signup_male.setObjectName("button_signup_male")

        self.gridLayout_3.addWidget(self.button_signup_male, 4, 0, 1, 1)

        self.label_signup_height = QLabel(self.container_signup_profile)
        self.label_signup_height.setObjectName("label_signup_height")

        self.gridLayout_3.addWidget(self.label_signup_height, 1, 0, 1, 1)

        self.date_birthday = QDateEdit(self.container_signup_profile)
        self.date_birthday.setObjectName("date_birthday")
        self.date_birthday.setMaximumDate(QDate(2100, 1, 1))
        self.date_birthday.setMinimumDate(QDate(1899, 12, 31))
        self.date_birthday.setCalendarPopup(True)
        self.date_birthday.setTimeSpec(Qt.UTC)
        self.date_birthday.setDate(QDate(2000, 1, 1))

        self.gridLayout_3.addWidget(self.date_birthday, 2, 1, 1, 1)

        self.spinbox_signup_height = QSpinBox(self.container_signup_profile)
        self.spinbox_signup_height.setObjectName("spinbox_signup_height")
        self.spinbox_signup_height.setAccelerated(True)
        self.spinbox_signup_height.setMaximum(512)

        self.gridLayout_3.addWidget(self.spinbox_signup_height, 1, 1, 1, 1)

        self.spinbox_signup_weight = QSpinBox(self.container_signup_profile)
        self.spinbox_signup_weight.setObjectName("spinbox_signup_weight")
        self.spinbox_signup_weight.setWrapping(False)
        self.spinbox_signup_weight.setFrame(True)
        self.spinbox_signup_weight.setAccelerated(True)
        self.spinbox_signup_weight.setProperty("showGroupSeparator", False)
        self.spinbox_signup_weight.setMaximum(512)

        self.gridLayout_3.addWidget(self.spinbox_signup_weight, 0, 1, 1, 1)

        self.button_signup_female = QRadioButton(self.container_signup_profile)
        self.buttonGroup.addButton(self.button_signup_female)
        self.button_signup_female.setObjectName("button_signup_female")

        self.gridLayout_3.addWidget(self.button_signup_female, 4, 1, 1, 1)

        self.combobox_signup_activity = QComboBox(self.container_signup_profile)
        self.combobox_signup_activity.addItem("")
        self.combobox_signup_activity.addItem("")
        self.combobox_signup_activity.addItem("")
        self.combobox_signup_activity.addItem("")
        self.combobox_signup_activity.addItem("")
        self.combobox_signup_activity.setObjectName("combobox_signup_activity")

        self.gridLayout_3.addWidget(self.combobox_signup_activity, 5, 0, 1, 2)

        self.stacked_signup_body.addWidget(self.container_signup_profile)

        self.verticalLayout_5.addWidget(self.stacked_signup_body)

        self.container_signup_footer = QWidget(self.container_signup)
        self.container_signup_footer.setObjectName("container_signup_footer")
        sizePolicy.setHeightForWidth(
            self.container_signup_footer.sizePolicy().hasHeightForWidth()
        )
        self.container_signup_footer.setSizePolicy(sizePolicy)
        self.layout_signup_controls = QHBoxLayout(self.container_signup_footer)
        self.layout_signup_controls.setSpacing(0)
        self.layout_signup_controls.setObjectName("layout_signup_controls")
        self.button_signup_signin = QPushButton(self.container_signup_footer)
        self.button_signup_signin.setObjectName("button_signup_signin")
        sizePolicy3.setHeightForWidth(
            self.button_signup_signin.sizePolicy().hasHeightForWidth()
        )
        self.button_signup_signin.setSizePolicy(sizePolicy3)

        self.layout_signup_controls.addWidget(self.button_signup_signin)

        self.spacer_signup_footer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.layout_signup_controls.addItem(self.spacer_signup_footer)

        self.button_signup_next = QPushButton(self.container_signup_footer)
        self.button_signup_next.setObjectName("button_signup_next")
        self.button_signup_next.setEnabled(False)
        sizePolicy3.setHeightForWidth(
            self.button_signup_next.sizePolicy().hasHeightForWidth()
        )
        self.button_signup_next.setSizePolicy(sizePolicy3)

        self.layout_signup_controls.addWidget(self.button_signup_next)

        self.verticalLayout_5.addWidget(self.container_signup_footer)

        self.spacer_signup = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.spacer_signup)

        self.stacked_auth_method.addWidget(self.container_signup)

        self.verticalLayout.addWidget(self.stacked_auth_method)

        QWidget.setTabOrder(self.input_signin_username, self.input_signin_password)
        QWidget.setTabOrder(
            self.input_signin_password, self.checkbox_signin_showpassword
        )
        QWidget.setTabOrder(self.checkbox_signin_showpassword, self.button_signin_next)
        QWidget.setTabOrder(self.button_signin_next, self.button_signin_signup)
        QWidget.setTabOrder(self.button_signin_signup, self.stacked_signup_body)
        QWidget.setTabOrder(self.stacked_signup_body, self.input_signup_firstname)
        QWidget.setTabOrder(self.input_signup_firstname, self.input_signup_lastname)
        QWidget.setTabOrder(self.input_signup_lastname, self.input_signup_username)
        QWidget.setTabOrder(self.input_signup_username, self.input_signup_password)
        QWidget.setTabOrder(self.input_signup_password, self.input_signup_confirm)
        QWidget.setTabOrder(
            self.input_signup_confirm, self.checkbox_signup_showpassword
        )
        QWidget.setTabOrder(self.checkbox_signup_showpassword, self.checkbox_tos)
        QWidget.setTabOrder(self.checkbox_tos, self.spinbox_signup_weight)
        QWidget.setTabOrder(self.spinbox_signup_weight, self.spinbox_signup_height)
        QWidget.setTabOrder(self.spinbox_signup_height, self.date_birthday)
        QWidget.setTabOrder(self.date_birthday, self.button_signup_male)
        QWidget.setTabOrder(self.button_signup_male, self.button_signup_female)
        QWidget.setTabOrder(self.button_signup_female, self.combobox_signup_activity)
        QWidget.setTabOrder(self.combobox_signup_activity, self.button_signup_next)
        QWidget.setTabOrder(self.button_signup_next, self.button_signup_signin)

        self.retranslateUi(Form)

        self.stacked_auth_method.setCurrentIndex(1)
        self.stacked_signin_body.setCurrentIndex(0)
        self.stacked_signup_body.setCurrentIndex(1)
        self.combobox_signup_activity.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        self.label_signin.setText(QCoreApplication.translate("Form", "sign in", None))
        self.label_use.setText(
            QCoreApplication.translate("Form", "use your la calorie account", None)
        )
        self.input_signin_username.setPlaceholderText(
            QCoreApplication.translate("Form", "username", None)
        )
        self.input_signin_password.setPlaceholderText(
            QCoreApplication.translate("Form", "password", None)
        )
        self.checkbox_signin_showpassword.setText(
            QCoreApplication.translate("Form", "show password", None)
        )
        self.button_signin_signup.setText(
            QCoreApplication.translate("Form", "create account", None)
        )
        self.button_signin_next.setText(
            QCoreApplication.translate("Form", "next", None)
        )
        self.label_signup.setText(QCoreApplication.translate("Form", "sign up", None))
        self.label_text.setText(
            QCoreApplication.translate("Form", "create your la calorie account", None)
        )
        self.input_signup_username.setPlaceholderText(
            QCoreApplication.translate("Form", "username", None)
        )
        self.input_signup_lastname.setPlaceholderText(
            QCoreApplication.translate("Form", "last name", None)
        )
        self.input_signup_firstname.setPlaceholderText(
            QCoreApplication.translate("Form", "first name", None)
        )
        self.input_signup_password.setPlaceholderText(
            QCoreApplication.translate("Form", "password", None)
        )
        self.input_signup_confirm.setPlaceholderText(
            QCoreApplication.translate("Form", "confirm", None)
        )
        self.checkbox_signup_showpassword.setText(
            QCoreApplication.translate("Form", "show password", None)
        )
        self.checkbox_tos.setText(
            QCoreApplication.translate(
                "Form", "i agree to the la calorie terms of use", None
            )
        )
        self.laabel_signup_age.setText(
            QCoreApplication.translate("Form", "birthday", None)
        )
        self.label_signup_weight.setText(
            QCoreApplication.translate("Form", "weight (kg)", None)
        )
        self.button_signup_male.setText(
            QCoreApplication.translate("Form", "male", None)
        )
        self.label_signup_height.setText(
            QCoreApplication.translate("Form", "height (cm)", None)
        )
        self.date_birthday.setDisplayFormat(
            QCoreApplication.translate("Form", "MM/dd/yyyy", None)
        )
        self.spinbox_signup_height.setSuffix("")
        self.spinbox_signup_height.setPrefix("")
        self.spinbox_signup_weight.setSpecialValueText("")
        self.spinbox_signup_weight.setSuffix("")
        self.spinbox_signup_weight.setPrefix("")
        self.button_signup_female.setText(
            QCoreApplication.translate("Form", "female", None)
        )
        self.combobox_signup_activity.setItemText(
            0, QCoreApplication.translate("Form", "low", None)
        )
        self.combobox_signup_activity.setItemText(
            1, QCoreApplication.translate("Form", "moderate", None)
        )
        self.combobox_signup_activity.setItemText(
            2, QCoreApplication.translate("Form", "average", None)
        )
        self.combobox_signup_activity.setItemText(
            3, QCoreApplication.translate("Form", "high", None)
        )
        self.combobox_signup_activity.setItemText(
            4, QCoreApplication.translate("Form", "abnormal", None)
        )

        self.combobox_signup_activity.setCurrentText("")
        self.combobox_signup_activity.setPlaceholderText(
            QCoreApplication.translate("Form", "activity", None)
        )
        self.button_signup_signin.setText(
            QCoreApplication.translate("Form", "sign in instead", None)
        )
        self.button_signup_next.setText(
            QCoreApplication.translate("Form", "next", None)
        )
        pass

    # retranslateUi
