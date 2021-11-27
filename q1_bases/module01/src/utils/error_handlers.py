import sqlite3

from PySide6.QtWidgets import QMessageBox

from public.i18n import translations
from src.utils.logger import Logger


def qt_error_handler(widget, err):
    log = Logger(str(widget))
    log.error(err)

    QMessageBox.critical(widget, translations.title_on_error(), str(err))


def sqlite_error_handler(func):
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as err:
            raise sqlite3.Error(err) from err

    return decorator
