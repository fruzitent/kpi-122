from datetime import datetime

from PySide6.QtCore import QDate


def get_current_qdate():
    today = datetime.utcnow()
    return QDate(today.year, today.month, today.day)
