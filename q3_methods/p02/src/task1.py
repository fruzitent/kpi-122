from collections.abc import Generator
from math import prod
from typing import Sequence

from matplotlib import pyplot as plt


def main() -> None:
    xs: tuple[float, ...] = -3, -2, 1, 3
    ys: tuple[float, ...] = -4, 19, -8, 14

    points: tuple[float, ...] = -1.5, 0.5, 1.5, 2
    resolution: float = 0.001

    timespan: list[float] = list(arange(xs[0], xs[-1], resolution))
    out0: list[float] = [lagrange(xs, ys, point) for point in timespan]

    with plt.style.context("seaborn"):
        plot(xs, ys, timespan, out0)

    for point in points:
        print(point, lagrange(xs, ys, point))


def plot(
    xs: Sequence[float],
    ys: Sequence[float],
    timespan: Sequence[float],
    out0: Sequence[float],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.scatter(xs, ys)
    ax0.plot(timespan, out0)

    ax0.set_title("$y = L(x)$")
    ax0.set_xlabel("$x$")
    ax0.set_ylabel("$y$")

    plt.show()


def arange(start: float, stop: float, step: float) -> Generator[float, None, None]:
    steps: int = int((stop - start) // step)
    yield from (start + idx * step for idx in range(steps))


def lagrange(xs: Sequence[float], ys: Sequence[float], point: float) -> float:
    assert len(xs) == len(ys)
    assert 1 < len(xs) < 10

    if len(xs) == 2:
        inp20: float = (point - xs[1]) / (xs[0] - xs[1])
        inp21: float = (point - xs[0]) / (xs[1] - xs[0])
        return (inp20 * ys[0]) + (inp21 * ys[1])

    if len(xs) == 3:
        inp30: float = ((point - xs[1]) * (point - xs[2])) / ((xs[0] - xs[1]) * (xs[0] - xs[2]))
        inp31: float = ((point - xs[0]) * (point - xs[2])) / ((xs[1] - xs[0]) * (xs[1] - xs[2]))
        inp32: float = ((point - xs[0]) * (point - xs[1])) / ((xs[2] - xs[0]) * (xs[2] - xs[1]))
        return (inp30 * ys[0]) + (inp31 * ys[1]) + (inp32 * ys[2])

    return sum(
        prod((point - x_j) / (x_i - x_j) for jdx, x_j in enumerate(xs) if idx != jdx) * ys[idx]
        for idx, x_i in enumerate(xs)
    )


if __name__ == "__main__":
    main()
