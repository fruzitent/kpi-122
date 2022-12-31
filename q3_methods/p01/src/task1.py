from decimal import Decimal
from math import sqrt


def main() -> None:
    x0_expected: Decimal = Decimal(sqrt(22))
    x0_given: Decimal = Decimal("4.69")
    stats(x0_expected, x0_given, "x0")

    print("---")

    x1_expected: Decimal = Decimal(2 / 21)
    x1_given: Decimal = Decimal("0.095")
    stats(x1_expected, x1_given, "x1")


def get_abs_error(number0: Decimal, number1: Decimal) -> Decimal:
    return abs(number0 - number1)


def get_rel_error(number: Decimal, delta: Decimal) -> Decimal:
    return abs(delta / number)


def stats(expected: Decimal, given: Decimal, label: str) -> None:
    abs_error: Decimal = get_abs_error(expected, given)
    rel_error: Decimal = get_rel_error(given, abs_error)
    print(f"{label} expected: {expected}")
    print(f"{label} given: {given}")
    print(f"{label} absolute: {abs_error}")
    print(f"{label} relative: {rel_error}")


if __name__ == "__main__":
    main()
