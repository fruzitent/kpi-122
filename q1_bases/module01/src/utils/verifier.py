import argon2
from zxcvbn import zxcvbn

from public.i18n import errors

ph = argon2.PasswordHasher()


def verify_account(firstname, lastname, username, password, confirm):
    if not firstname.isalpha():
        raise ValueError(errors.firstname_invalid())

    if not lastname.isalpha():
        raise ValueError(errors.lastname_invalid())

    if not username.isalpha():
        raise ValueError(errors.username_invalid())

    if not password:
        raise ValueError(errors.password_empty())

    if len(password) < 8:
        raise ValueError(errors.password_short())

    if password != confirm:
        raise ValueError(errors.password_mismatch())

    report = zxcvbn(password)
    if report["score"] < 2:
        feedback = report["feedback"]
        err_msg = "\n".join([feedback["warning"], *feedback["suggestions"]])
        raise ValueError(err_msg)

    return {
        "firstname": firstname.lower(),
        "lastname": lastname.lower(),
        "username": username.lower(),
        "password": ph.hash(password),
    }


def verify_profile(weight=None, height=None, birthday=None, sex=None, activity=None):
    profile = {}

    if weight is not None:
        if weight.value():
            profile["weight"] = weight.value()
        else:
            raise ValueError(errors.weight_invalid())

    if height is not None:
        if height.value():
            profile["height"] = height.value()
        else:
            raise ValueError(errors.height_invalid())

    if birthday is not None:
        date = birthday.dateTime().toUTC().toPython()
        profile["birthday"] = str(date)

    if sex is not None:
        male, female = sex
        if male.isChecked():
            profile["sex"] = 0
        elif female.isChecked():
            profile["sex"] = 1
        else:
            raise ValueError(errors.sex_invalid())

    if activity is not None:
        if activity.currentIndex() != -1:  # noqa: WPS504
            profile["activity"] = activity.currentIndex()
        else:
            raise ValueError(errors.activity_invalid())

    return profile
