from decimal import Decimal
from math import sqrt

from src.task1 import get_abs_error, get_rel_error


def test_get_abs_error() -> None:
    assert get_abs_error(
        Decimal(7 / 22),
        Decimal("0.318"),
    ) == Decimal("0.0001818181818181767717135244311")
    assert get_abs_error(
        Decimal(9 / 11),
        Decimal("0.818"),
    ) == Decimal("0.0001818181818182322828647556889")
    assert get_abs_error(
        Decimal(15 / 7),
        Decimal("2.14"),
    ) == Decimal("0.002857142857142793701541449991")
    assert get_abs_error(
        Decimal(sqrt(10)),
        Decimal("3.16"),
    ) == Decimal("0.002277660168379522787063251599")
    assert get_abs_error(
        Decimal(sqrt(18)),
        Decimal("4.24"),
    ) == Decimal("0.002640687119284770290050801123")
    assert get_abs_error(
        Decimal(sqrt(62)),
        Decimal("7.87"),
    ) == Decimal("0.004007874011811125569693103898")


def test_get_rel_error() -> None:
    assert get_rel_error(
        Decimal("0.318"),
        Decimal("0.0001818181818181767717135244311"),
    ) == Decimal("0.0005717552887364049424953598462")
    assert get_rel_error(
        Decimal("0.818"),
        Decimal("0.0001818181818182322828647556889"),
    ) == Decimal("0.0002222716159147093922552025537")
    assert get_rel_error(
        Decimal("2.14"),
        Decimal("0.002857142857142793701541449991"),
    ) == Decimal("0.001335113484646165281094135510")
    assert get_rel_error(
        Decimal("3.16"),
        Decimal("0.002277660168379522787063251599"),
    ) == Decimal("0.0007207785342973173376782441769")
    assert get_rel_error(
        Decimal("4.24"),
        Decimal("0.002640687119284770290050801123"),
    ) == Decimal("0.0006228035658690495967100946045")
    assert get_rel_error(
        Decimal("7.87"),
        Decimal("0.004007874011811125569693103898"),
    ) == Decimal("0.0005092597219582116352850195550")
