from decimal import Decimal
from typing import Self

from src.task2 import BroadSense, NarrowSense


class TestBroadSense(object):
    def test_maximum_absolute_error(self: Self) -> None:
        assert BroadSense("0.745").maximum_absolute_error == Decimal("0.001")
        assert BroadSense("12.384").maximum_absolute_error == Decimal("0.001")
        assert BroadSense("21.7").maximum_absolute_error == Decimal("0.1")

    def test_maximum_relative_error(self: Self) -> None:
        assert BroadSense("0.745").maximum_relative_error == Decimal("0.0013")
        assert BroadSense("12.384").maximum_relative_error == Decimal("0.000081")
        assert BroadSense("21.7").maximum_relative_error == Decimal("0.0046")


class TestNarrowSense(object):
    def test_maximum_absolute_error(self: Self) -> None:
        assert NarrowSense("0.3648").maximum_absolute_error == Decimal("0.00005")
        assert NarrowSense("0.4357").maximum_absolute_error == Decimal("0.00005")
        assert NarrowSense("2.3445").maximum_absolute_error == Decimal("0.00005")

    def test_maximum_relative_error(self: Self) -> None:
        assert NarrowSense("0.3648").maximum_relative_error == Decimal("0.00014")
        assert NarrowSense("2.3445").maximum_relative_error == Decimal("0.000021")
        assert NarrowSense("0.4357").maximum_relative_error == Decimal("0.00011")
