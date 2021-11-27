import os
import sys

from PySide6.QtCore import QCoreApplication, QLocale, QTranslator
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow
from qt_material import list_themes

from src.auth import AuthWindow
from src.components.database import db
from src.components.multithreading import pool
from src.components.theme import Theme
from src.config import config
from src.home import HomeWindow
from src.ui.main_ui import Ui_MainWindow
from src.utils.logger import Logger

log = Logger(__name__)
os.environ["QT_FONT_DPI"] = config.QT_FONT_DPI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_file_exit.triggered.connect(lambda: app_exit(0))

        self.AuthWidget = AuthWindow()
        self.ui.container.addWidget(self.AuthWidget)
        self.AuthWidget.on_user.connect(self.auth_handler)

        self.HomeWidget = HomeWindow()
        self.ui.container.addWidget(self.HomeWidget)

    def auth_handler(self, user):
        self.HomeWidget.refresh(user)
        self.ui.container.setCurrentIndex(1)
        log.info(f"user {user['username']} successfully logged in")


def app_exit(code):
    db.exit()
    pool.exit()
    log.warning("exit")
    sys.exit(code)


def main():
    app = QApplication(sys.argv)
    theme = Theme(app)

    translator = QTranslator()
    translator.load(QLocale(), "", "", config.I18N_PATH)
    QCoreApplication.installTranslator(translator)

    window = MainWindow()
    window.setFixedSize(1280, 720)  # noqa: WPS432

    def set_lang(lang):
        translator.load(f"{config.I18N_PATH}/{lang}.qm")
        log.debug(f"app language is set to {lang}")

        window.ui.retranslateUi(window)
        window.AuthWidget.ui.retranslateUi(window.AuthWidget)
        window.HomeWidget.ui.retranslateUi(window.HomeWidget)

    window.ui.action_language_english.triggered.connect(lambda: set_lang("en_US"))
    window.ui.action_language_russian.triggered.connect(lambda: set_lang("ru_RU"))

    for filename in list_themes():  # noqa: WPS 426
        title = " ".join(filename[:-4].split("_"))
        action = QAction(title, window)
        action.triggered.connect(lambda checked=False, x=filename: theme.set_theme(x))
        window.ui.menu_view_theme.addAction(action)

    window.ui.container.setCurrentIndex(0)
    window.AuthWidget.ui.stacked_auth_method.setCurrentIndex(0)
    window.AuthWidget.ui.stacked_signin_body.setCurrentIndex(0)
    window.AuthWidget.ui.stacked_signup_body.setCurrentIndex(0)
    window.HomeWidget.ui.container.setCurrentIndex(0)

    window.show()
    app_exit(app.exec())
