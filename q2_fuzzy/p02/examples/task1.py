"""
Modeling the input-output relationship defined on the basis of a set of pairs.

p1 = [0, 0], t1 = 0
p2 = [0, 1], t2 = 0
p3 = [1, 0], t3 = 0
p4 = [1, 1], t4 = 1
"""

import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]
MIN: float = 0
MAX: float = 10.1
STEP: float = 0.1
METHODS = ("centroid", "bisector", "mom", "som", "lom")


def set_plot_limit(plot: plt.Axes, x0: float, x1: float, y0: float, y1: float) -> None:
    plot.set_xlim(x0, x1)
    plot.set_ylim(y0, y1)


def get_plots() -> tuple[plt.Axes, ...]:
    axes = plt.subplots(nrows=3)[1]
    set_plot_limit(axes[0], 0, 1, 0, 1)
    set_plot_limit(axes[1], 0, 1, 0, 1)
    set_plot_limit(axes[2], 0, 1, 0, 1)
    return tuple(axes)


def show_legend(*plots: plt.Axes) -> None:
    for plot in plots:
        plot.legend()


def setup_plot(plot: plt.Axes, *, title: str) -> None:
    plot.set_title(title)
    show_legend(plot)
    plot.spines["top"].set_visible(False)  # type: ignore
    plot.get_xaxis().tick_bottom()  # type: ignore
    plot.get_yaxis().tick_left()  # type: ignore


class Task(object):  # noqa: H601 class has low (0.00%) cohesion
    def __init__(self) -> None:
        self._darr_a: ND = np.arange(MIN, MAX, STEP, dtype=TypeN)
        self._darr_b: ND = np.arange(MIN, MAX, STEP, dtype=TypeN)
        self._vert_a: ND = np.arange(MIN, MAX, STEP, dtype=TypeN)
        self._vert_b: ND = np.arange(MIN, MAX, STEP, dtype=TypeN)
        self._res: ND = fuzz.trimf(self._darr_a, [0, 0, 1])
        self._a1: ND = fuzz.trimf(self._darr_a, [0, 0, 1])
        self._a2: ND = fuzz.trimf(self._darr_a, [0, 1, 1])
        self._b1: ND = fuzz.trimf(self._darr_a, [0, 0, 1])
        self._b2: ND = fuzz.trimf(self._darr_a, [0, 1, 1])
        self._x0: float = 0.1
        self._x1: float = 0.1

        self._a11_level: float = fuzz.interp_membership(
            self._darr_a,
            self._a1,
            self._x0,
        )
        self._a12_level: float = fuzz.interp_membership(
            self._darr_a,
            self._a2,
            self._x0,
        )
        self._a21_level: float = fuzz.interp_membership(
            self._darr_a,
            self._a1,
            self._x1,
        )
        self._a22_level: float = fuzz.interp_membership(
            self._darr_a,
            self._a2,
            self._x1,
        )

        self._act: list[int] = [0, 0]
        self._r: list[int] = [0, 0, 0, 0]
        self._rule_list: list[list[int]] = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1],
        ]

    def calculate1(self) -> None:
        for itr, _ in enumerate(self._vert_a):
            self._vert_a[itr] = self._x0
            self._vert_b[itr] = self._x1

    def calculate2(self) -> None:
        for itr, rule in enumerate(self._rule_list):
            num1: float = self._a11_level if rule[0] == 0 else self._a12_level
            num2: float = self._a21_level if rule[1] == 0 else self._a22_level
            self._r[itr] = np.fmin(num1, num2)

        for itr, _ in enumerate(self._rule_list):
            jtr = self._rule_list[itr][2]
            self._act[jtr] = np.fmax(self._act[jtr], self._r[itr])

        for itr, _ in enumerate(self._b1):
            if self._b1[itr] > self._act[0]:
                self._b1[itr] = self._act[0]
            if self._b2[itr] > self._act[1]:
                self._b2[itr] = self._act[1]
            self._res = np.fmax(self._b1, self._b2)

    def calculate3(self) -> None:
        for method in METHODS:
            y: float = fuzz.defuzz(self._darr_b, self._res, method)
            print(f"{method}, {y=}")

        sum1: float = 0
        sum2: float = 0
        for itr, _ in enumerate(self._darr_b):
            sum1 += self._darr_b[itr] * self._res[itr]
            sum2 += self._res[itr]
        ratio: float = sum1 / sum2
        print(f"{sum1=}, {sum2=}, {ratio=}")

    def plot1(self) -> None:
        ax0, ax1, ax2 = get_plots()

        ax0.plot(self._vert_a, self._a1, color="yellow", label="x1")
        ax0.plot(self._darr_a, self._a1, color="blue", label="a11")
        ax0.plot(self._darr_a, self._a2, color="green", label="a12")
        setup_plot(ax0, title="a1")

        ax1.plot(self._vert_b, self._a1, color="yellow", label="x2")
        ax1.plot(self._darr_a, self._a1, color="blue", label="a21")
        ax1.plot(self._darr_a, self._a2, color="green", label="a22")
        setup_plot(ax1, title="a2")

        ax2.plot(self._darr_b, self._b1, color="blue", label="b1")
        ax2.plot(self._darr_b, self._b2, color="green", label="b2")
        setup_plot(ax2, title="darr_b")

        plt.tight_layout()  # type: ignore
        plt.show()

    def plot2(self) -> None:
        ax0, ax1, ax2 = get_plots()
        ax0.plot(self._darr_b, self._b1, color="blue", label="b1")
        ax1.plot(self._darr_b, self._b2, color="green", label="b2")
        ax2.plot(self._darr_b, self._res, color="green", label="res")
        show_legend(ax0, ax1, ax2)
        plt.show()


def main() -> None:
    task = Task()
    task.calculate1()
    task.plot1()
    task.calculate2()
    task.plot2()
    task.calculate3()


if __name__ == "__main__":
    main()
