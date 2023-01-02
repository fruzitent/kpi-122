from decimal import Decimal
from math import sqrt

from src.task1 import get_abs_error, get_rel_error


def test_get_abs_error() -> None:
    assert get_abs_error(Decimal(7 / 22), Decimal("0.318")) == Decimal("0.00018")
    assert get_abs_error(Decimal(9 / 11), Decimal("0.818")) == Decimal("0.00018")
    assert get_abs_error(Decimal(15 / 7), Decimal("2.14")) == Decimal("0.0029")
    assert get_abs_error(Decimal(sqrt(10)), Decimal("3.16")) == Decimal("0.0023")
    assert get_abs_error(Decimal(sqrt(18)), Decimal("4.24")) == Decimal("0.0026")
    assert get_abs_error(Decimal(sqrt(62)), Decimal("7.87")) == Decimal("0.0040")


def test_get_rel_error() -> None:
    assert get_rel_error(Decimal("0.318"), Decimal("0.00018")) == Decimal("0.00057")
    assert get_rel_error(Decimal("0.818"), Decimal("0.00018")) == Decimal("0.00022")
    assert get_rel_error(Decimal("2.14"), Decimal("0.0029")) == Decimal("0.0014")
    assert get_rel_error(Decimal("3.16"), Decimal("0.0023")) == Decimal("0.00073")
    assert get_rel_error(Decimal("4.24"), Decimal("0.0026")) == Decimal("0.00061")
    assert get_rel_error(Decimal("7.87"), Decimal("0.0040")) == Decimal("0.00051")
