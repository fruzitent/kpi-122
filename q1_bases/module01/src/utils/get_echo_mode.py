from PySide6.QtWidgets import QLineEdit


def get_echo_mode(state):
    return QLineEdit.Normal if state else QLineEdit.Password
