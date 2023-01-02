from decimal import ROUND_HALF_UP, Decimal
from math import sqrt


def main() -> None:
    x0_expected: Decimal = Decimal(sqrt(22))
    x0_given: Decimal = Decimal("4.69")
    stats(x0_expected, x0_given, "x0")

    print("---")

    x1_expected: Decimal = Decimal(2 / 21)
    x1_given: Decimal = Decimal("0.095")
    stats(x1_expected, x1_given, "x1")


def stats(expected: Decimal, given: Decimal, label: str) -> None:
    abs_error: Decimal = get_abs_error(expected, given)
    rel_error: Decimal = get_rel_error(given, abs_error)
    print(label, given)
    print(f"{label}*:", expected)
    print(f"Δ{label}:", abs_error)
    print(f"δ{label}:", rel_error)


def get_abs_error(number0: Decimal, number1: Decimal) -> Decimal:
    abs_error: Decimal = abs(number0 - number1)
    return round_half_up(abs_error)


def get_rel_error(number: Decimal, delta: Decimal) -> Decimal:
    rel_error: Decimal = abs(delta / number)
    return round_half_up(rel_error)


def round_half_up(number: Decimal) -> Decimal:
    exponent: int = number.adjusted() - 1
    return number.quantize(Decimal(f"1e{exponent}"), rounding=ROUND_HALF_UP)


if __name__ == "__main__":
    main()
