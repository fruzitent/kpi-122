from decimal import Decimal
from math import cos
from typing import Callable, Generator

from matplotlib import pyplot as plt


def main() -> None:
    x0: Decimal = Decimal("1.4")
    y0: Decimal = Decimal("2.5")
    xn: Decimal = Decimal("2.4")

    step: Decimal = Decimal("0.1")

    xs, ys = zip(*euler(func, x0, y0, xn, step))

    with plt.style.context("seaborn"):
        plot(xs, ys)


def plot(
    xs: tuple[Decimal, ...],
    ys: tuple[Decimal, ...],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(xs, ys)
    ax0.scatter(xs, ys, color="red")
    ax0.set_title("Euler's method")
    ax0.set_xlabel("$x$")
    ax0.set_ylabel("$y$")

    plt.show()


def func(xi: Decimal, yi: Decimal) -> Decimal:
    return xi + Decimal(cos(yi / Decimal("2.25")))


def euler(
    callback: Callable[[Decimal, Decimal], Decimal],
    x0: Decimal,
    y0: Decimal,
    xn: Decimal,
    step: Decimal,
) -> Generator[tuple[Decimal, Decimal], None, None]:
    while x0 <= xn:
        yield x0, y0
        y0 += step * callback(x0, y0)
        x0 += step


if __name__ == "__main__":
    main()
