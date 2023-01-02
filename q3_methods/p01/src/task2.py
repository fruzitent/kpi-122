from decimal import ROUND_HALF_UP, Decimal
from typing import ClassVar, Self

from src.task1 import get_abs_error


def main() -> None:
    narrow()
    print("---")
    broad()


def narrow() -> None:
    number: Decimal = Decimal("2.4543")
    print("x:", number)

    abs_error: Decimal = Decimal("0.0032")
    print("Δx:", abs_error)
    print()

    number_prime, abs_error_prime = NarrowSense(number).round(abs_error)
    print("x*:", number_prime)
    print("Δx*:", abs_error_prime)


def broad() -> None:
    number: Decimal = Decimal("24.5643")
    print("x:", number)

    rel_error: Decimal = Decimal("0.001")
    print("δx:", rel_error)

    abs_error: Decimal = number * rel_error
    print("Δx:", abs_error)
    print()

    number_prime, abs_error_prime = BroadSense(number).round(abs_error)
    print("x*:", number_prime)
    print("Δx*:", abs_error_prime)


class Sense(Decimal):
    factor: ClassVar[int]

    @property
    def maximum_absolute_error(self: Self) -> Decimal:
        exponent: int = int(self.as_tuple().exponent)
        return Decimal(f"1e{exponent}") / self.factor

    @property
    def maximum_relative_error(self: Self) -> Decimal:
        rel_error: Decimal = abs(self.maximum_absolute_error / self)
        exponent: int = rel_error.adjusted() - 1
        return rel_error.quantize(Decimal(f"1e{exponent}"), rounding=ROUND_HALF_UP)

    @property
    def significant_figures(self: Self) -> str:
        return str(self).replace(".", "").lstrip("0")

    def real_significant_figures(self: Self, abs_error: Decimal) -> tuple[str, str]:
        digits: list[int] = list(self.as_tuple().digits)

        # TODO: 2.4543(0.0032) and 2.3485(0.0042) behave incorrectly with -1
        exponent: int = len(str(int(self)).lstrip("0")) - 1

        certain: str = ""
        doubtful: str = ""

        for digit in digits:
            abs_error_max: Decimal = self.__class__(f"1e{exponent}").maximum_absolute_error

            if abs_error < abs_error_max:
                print(f"{digit} - certain:", abs_error, abs_error_max)
                certain += str(digit)
            else:
                print(f"{digit} - doubtful:", abs_error, abs_error_max)
                doubtful += str(digit)

            exponent -= 1

        return certain, doubtful

    def round(self: Self, abs_error: Decimal) -> tuple[Decimal, Decimal]:
        number: Self = self

        certain, doubtful = self.real_significant_figures(abs_error)
        rsf: int = len(certain)
        print("rsf:", rsf)
        print()

        is_quit: bool = False
        while not is_quit:
            before_decimal: int = len(str(int(number)).lstrip("0"))
            exponent: int = before_decimal - rsf
            number_round: Decimal = number.quantize(Decimal(f"1e{exponent}"), rounding=ROUND_HALF_UP)
            number_prime: Self = self.__class__(number_round)
            print("x*:", number_prime)

            abs_error_round: Decimal = get_abs_error(self, number_prime)
            print("Δr:", abs_error_round)

            abs_error_prime: Decimal = abs_error + abs_error_round
            print("Δx*:", abs_error_prime)

            certain, doubtful = number_prime.real_significant_figures(abs_error_prime)
            rsf_prime: int = len(certain)
            print("rsf*:", rsf_prime)

            if rsf == rsf_prime:
                is_quit = True
            else:
                number = number_prime
                rsf -= 1

            print()

        return number_prime, abs_error_prime


class BroadSense(Sense):
    factor: ClassVar[int] = 1


class NarrowSense(Sense):
    factor: ClassVar[int] = 2


if __name__ == "__main__":
    main()
