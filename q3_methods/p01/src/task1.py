from dataclasses import dataclass
from math import isclose, sqrt
from typing import Self


def main() -> None:
    x0: Expression = Expression(
        expected=Fraction(x0=sqrt(22)),
        original=Fraction(x0=4.69),
    )

    x1: Expression = Expression(
        expected=Fraction(x0=2, x1=21),
        original=Fraction(x0=0.095),
    )

    print("Original:", x0.original(), x1.original())
    print("Expected:", x0.expected(), x1.expected())
    print("Absolute:", x0.absolute_rounding_error(), x1.absolute_rounding_error())
    print("Relative:", x0.relative_rounding_error(), x1.relative_rounding_error())
    print("x0", get_sign(x0.relative_rounding_error(), x1.relative_rounding_error()), "x1")


@dataclass
class Fraction(object):
    x0: float
    x1: float = 1

    def __call__(self: Self) -> float:
        return self.x0 if isclose(self.x1, 1) else self.x0 / self.x1


@dataclass
class Expression(object):
    expected: Fraction
    original: Fraction

    def absolute_rounding_error(self: Self) -> float:
        return abs(self.original() - self.expected())

    def relative_rounding_error(self: Self) -> float:
        return self.absolute_rounding_error() / self.original()


def get_sign(lhs: float, rhs: float) -> str:
    if isclose(lhs, rhs):
        return "is as accurate as"

    if lhs < rhs:
        return "is more accurate than"

    if lhs > rhs:
        return "is less accurate than"

    raise RuntimeError("Unreachable")


if __name__ == "__main__":
    main()
