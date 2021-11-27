from PySide6.QtCore import QCoreApplication

translate = QCoreApplication.translate


def activity_abnormal():
    return translate("translations", "abnormal")


def activity_average():
    return translate("translations", "average")


def activity_high():
    return translate("translations", "high")


def activity_low():
    return translate("translations", "low")


def activity_normal():
    return translate("translations", "moderate")


def category_normal():
    return translate("translations", "normal")


def category_obesity_one():
    return translate("translations", "obesity 1")


def category_obesity_three():
    return translate("translations", "obesity 3")


def category_obesity_two():
    return translate("translations", "obesity 2")


def category_overweight():
    return translate("translations", "overweight")


def category_underweight():
    return translate("translations", "underweight")


def goal_gain():
    return translate("translations", "gain")


def goal_keep():
    return translate("translations", "keep")


def goal_lose():
    return translate("translations", "lose")


def sex_female():
    return translate("translations", "female")


def sex_male():
    return translate("translations", "male")


def signin():
    return translate("translations", "sign in")


def title_on_error():
    return translate("translations", "la calorie - application error")


def use_signin():
    return translate("translations", "use your la calorie account")


def welcome():
    return translate("translations", "welcome")
