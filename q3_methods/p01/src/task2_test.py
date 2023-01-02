from decimal import Decimal
from typing import Self

from src.task2 import BroadSense, NarrowSense, Sense


class TestSense(object):
    def test_significant_figures(self: Self) -> None:
        assert Sense("0.00208").significant_figures == "208"
        assert Sense("0.002080").significant_figures == "2080"
        assert Sense("0.0024").significant_figures == "24"
        assert Sense("0.037").significant_figures == "37"
        assert Sense("534.425").significant_figures == "534425"
        assert Sense("670.560").significant_figures == "670560"


class TestBroadSense(object):
    def test_real_significant_figures(self: Self) -> None:
        assert BroadSense("0.394").real_significant_figures(Decimal("0.00513")) == ("39", "4")
        assert BroadSense("0.3945").real_significant_figures(Decimal("0.00063")) == ("394", "5")
        assert BroadSense("2.35").real_significant_figures(Decimal("0.00911")) == ("235", "")
        assert BroadSense("2.3544").real_significant_figures(Decimal("0.002")) == ("235", "44")
        assert BroadSense("7.158").real_significant_figures(Decimal("0.009")) == ("715", "8")
        assert BroadSense("13.8").real_significant_figures(Decimal("0.07937")) == ("138", "")
        assert BroadSense("13.842").real_significant_figures(Decimal("0.0373734")) == ("138", "42")

    def test_round(self: Self) -> None:
        # assert BroadSense("0.34484").round(Decimal("0.00137936")) == (Decimal("0.345"), Decimal("0.00153936"))
        assert BroadSense("13.842").round(Decimal("0.0373734")) == (Decimal("13.8"), Decimal("0.0793734"))


class TestNarrowSense(object):
    def test_real_significant_figures(self: Self) -> None:
        assert NarrowSense("4.5").real_significant_figures(Decimal("0.0051")) == ("45", "")
        assert NarrowSense("4.5037").real_significant_figures(Decimal("0.0014")) == ("450", "37")
        assert NarrowSense("7.158").real_significant_figures(Decimal("0.009")) == ("71", "58")
        assert NarrowSense("27.1548").real_significant_figures(Decimal("0.0016")) == ("2715", "48")
        assert NarrowSense("72.353").real_significant_figures(Decimal("0.026")) == ("723", "53")
        assert NarrowSense("72.4").real_significant_figures(Decimal("0.379")) == ("72", "4")

    def test_round(self: Self) -> None:
        # assert NarrowSense("2.3485").round(Decimal("0.0042")) == (Decimal("2.349"), Decimal("0.0047"))
        assert NarrowSense("4.5037").round(Decimal("0.0014")) == (Decimal("4.5"), Decimal("0.0051"))
        assert NarrowSense("27.1548").round(Decimal("0.0016")) == (Decimal("27.2"), Decimal("0.0468"))
