from decimal import Decimal
from math import sin, sqrt
from typing import Callable, Generator

from matplotlib import pyplot as plt


def main() -> None:
    x0: Decimal = Decimal("0.5")
    y0: Decimal = Decimal("0.6")
    xn: Decimal = Decimal("1.5")

    step: Decimal = Decimal("0.1")

    xs, ys = zip(*cauchy(func, x0, y0, xn, step))

    with plt.style.context("seaborn"):
        plot(xs, ys)


def plot(
    xs: tuple[Decimal, ...],
    ys: tuple[Decimal, ...],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(xs, ys)
    ax0.scatter(xs, ys, color="red")
    ax0.set_title("Cauchy's method")
    ax0.set_xlabel("$x$")
    ax0.set_ylabel("$y$")

    plt.show()


def func(xi: Decimal, yi: Decimal) -> Decimal:
    return xi + Decimal(sin(yi / Decimal(sqrt(7))))


def cauchy(
    callback: Callable[[Decimal, Decimal], Decimal],
    x0: Decimal,
    y0: Decimal,
    xn: Decimal,
    step: Decimal,
) -> Generator[tuple[Decimal, Decimal], None, None]:
    while x0 <= xn:
        yield x0, y0
        current: Decimal = callback(x0, y0)
        succeeding: Decimal = callback(x0 + step, y0 + step * current)
        y0 += step * (current + succeeding) / 2
        x0 += step


if __name__ == "__main__":
    main()
