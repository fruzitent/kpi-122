from dataclasses import dataclass
from math import factorial, prod
from typing import Self, TypeAlias

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt

ArrayType: TypeAlias = list[float]
ValueType: TypeAlias = float


def main() -> None:
    xs: ArrayType = [2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6]
    ys: ArrayType = [3.526, 3.782, 3.945, 4.043, 4.104, 4.155, 4.222, 4.331, 4.507, 4.775, 5.159, 5.683]
    resolution: float = 0.001

    timespan: npt.NDArray[np.float64] = np.arange(xs[0], xs[-1], resolution)
    out0: ArrayType = [BackwardNewton(xs, ys).interpolate(point) for point in timespan]
    out1: ArrayType = [ForwardNewton(xs, ys).interpolate(point) for point in timespan]

    with plt.style.context("seaborn"):
        plot(xs, ys, timespan, out0, out1)

    # TODO: calculate derivatives


def plot(
    xs: ArrayType,
    ys: ArrayType,
    timespan: npt.NDArray[np.float64],
    out0: ArrayType,
    out1: ArrayType,
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.scatter(xs, ys)
    ax0.plot(xs, ys)
    ax0.plot(timespan, out0, label="Backward")
    ax0.plot(timespan, out1, linestyle="--", label="Forward")
    ax0.legend()
    ax0.set_title("")
    ax0.set_xlabel("$x$")
    ax0.set_ylabel("$y$")

    plt.plot()


@dataclass
class Newton(object):
    xs: ArrayType
    ys: ArrayType

    def __post_init__(self: Self) -> None:
        assert len(self.xs) == len(self.ys)

    @property
    def step(self: Self) -> ValueType:
        return self.xs[1] - self.xs[0]


@dataclass
class BackwardNewton(Newton):
    def divdiff(self: Self, order: int, index: int) -> ValueType:
        return self.ys[index] if order == 0 else self.divdiff(order - 1, index) - self.divdiff(order - 1, index - 1)

    def interpolate(self: Self, point: ValueType) -> ValueType:
        return sum(
            self.divdiff(order, -1) * prod(self.phase(point) + index for index in range(order)) / factorial(order)
            for (order, _) in enumerate(self.xs)
        )

    def phase(self: Self, point: ValueType) -> ValueType:
        return (point - self.xs[-1]) / self.step


@dataclass
class ForwardNewton(Newton):
    def divdiff(self: Self, order: int, index: int) -> ValueType:
        return self.ys[index] if order == 0 else self.divdiff(order - 1, index + 1) - self.divdiff(order - 1, index)

    def interpolate(self: Self, point: ValueType) -> ValueType:
        return sum(
            self.divdiff(order, 0) * prod(self.phase(point) - index for index in range(order)) / factorial(order)
            for order, _ in enumerate(self.xs)
        )

    def phase(self: Self, point: ValueType) -> ValueType:
        return (point - self.xs[0]) / self.step


if __name__ == "__main__":
    main()
