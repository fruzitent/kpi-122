from PySide6.QtCore import QCoreApplication

translate = QCoreApplication.translate


def activity_invalid():
    return translate("errors", "no activity is chosen")


def db_no_connection():
    return translate("errors", "could not connect to the database")


def firstname_invalid():
    return translate("errors", "firstname can have only alphabetic characters")


def height_invalid():
    return translate("errors", "height cannot equal zero")


def lastname_invalid():
    return translate("errors", "lastname can have only alphabetic characters")


def password_empty():
    return translate("errors", "enter a password")


def password_mismatch():
    return translate("errors", "those passwords did not match. try again")


def password_short():
    return translate("errors", "use 8 characters or more for your password")


def sex_invalid():
    return translate("errors", "no sex is chosen")


def user_not_found():
    return translate("errors", "could not find your la calorie account")


def username_invalid():
    return translate("errors", "username can have only alphabetic characters")


def username_taken():
    return translate("errors", "that username is taken, try another")


def weight_invalid():
    return translate("errors", "weight cannot equal zero")


def wrong_password():
    return translate("errors", "wrong password")


def wrong_password_throttle(timeout):
    string = translate("errors", "wrong password. try again in")
    return f"{string} {timeout}"
