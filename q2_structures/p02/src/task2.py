from functools import cache
from math import exp, factorial


def exp_itr(power: float, eps: float) -> tuple[float, int]:
    sigma: float = 0
    counter: int = 0
    while True:
        value: float = power**counter / factorial(counter)
        sigma += value
        if abs(value) < eps:
            return sigma, counter
        counter += 1


@cache  # type: ignore
def exp_rec(power: float, eps: float, counter: int = 0) -> tuple[float, int]:
    value: float = power**counter / factorial(counter)
    if abs(value) >= eps:
        next_value, next_counter = exp_rec(power, eps, counter + 1)
        return value + next_value, next_counter
    return value, counter


def main() -> None:
    power: int = 10
    eps: float = 1e-3
    print(exp_itr(power, eps))
    print(exp_rec(power, eps))
    print(exp(power))


if __name__ == "__main__":
    main()
