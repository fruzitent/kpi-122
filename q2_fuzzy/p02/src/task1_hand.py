from functools import reduce
from itertools import product
from typing import Literal

import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, fmin, fmax, linspace, meshgrid
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]

STEP: float = 0.1
MIN: float = 0
MAX: float = 1 + STEP

X0: float = 0.2
X1: float = 1 - X0

METHODS = Literal["centroid", "bisector", "mom", "som", "lom"]

fuzzy_and = fmin
fuzzy_or = fmax


def compute_rules(*rules: list[ND]) -> list[ND]:
    return [fuzzy_and(antecedent, consequent) for antecedent, consequent in rules]


class Task(object):
    def __init__(self, start: float, end: float, step: float) -> None:
        self._universe: ND = arange(start, end, step, dtype=TypeN)
        self._inp0: ND = self._universe.copy()
        self._inp1: ND = self._universe.copy()
        self._out0: ND = self._universe.copy()
        self.res_x: float = 0
        self.res_y: float = 0

    def fuzzify(self) -> None:
        self._inp0_low: ND = fuzz.trimf(self._inp0, [0, 0, 1])
        self._inp0_hgh: ND = fuzz.trimf(self._inp0, [0, 1, 1])
        self._inp1_low: ND = fuzz.trimf(self._inp1, [0, 0, 1])
        self._inp1_hgh: ND = fuzz.trimf(self._inp1, [0, 1, 1])
        self._out0_low: ND = fuzz.trimf(self._out0, [0, 0, 1])
        self._out0_hgh: ND = fuzz.trimf(self._out0, [0, 1, 1])

    def aggregate(self, x0: float, x1: float) -> None:
        inp0_lvl_low: ND = fuzz.interp_membership(self._inp0, self._inp0_low, x0)
        inp0_lvl_hgh: ND = fuzz.interp_membership(self._inp0, self._inp0_hgh, x0)
        inp1_lvl_low: ND = fuzz.interp_membership(self._inp1, self._inp1_low, x1)
        inp1_lvl_hgh: ND = fuzz.interp_membership(self._inp1, self._inp1_hgh, x1)

        self._rules: list[ND] = compute_rules(
            [fuzzy_and(inp0_lvl_low, inp1_lvl_low), self._out0_hgh],
            [fuzzy_and(inp0_lvl_low, inp1_lvl_hgh), self._out0_low],
            [fuzzy_and(inp0_lvl_hgh, inp1_lvl_low), self._out0_low],
            [fuzzy_and(inp0_lvl_hgh, inp1_lvl_hgh), self._out0_hgh],
        )

    def defuzzify(self, method: METHODS = "centroid") -> None:
        activation: ND = reduce(fuzzy_or, self._rules)

        if not any(activation):
            return

        self.res_x = fuzz.defuzz(self._out0, activation, method)
        self.res_y = fuzz.interp_membership(self._out0, activation, self.res_x)

    def plot_fuzzify(self) -> None:
        ax0, ax1, ax2 = plt.subplots(nrows=3)[1]

        ax0.set_title("inp0")
        ax0.plot(self._inp0, self._inp0_low, label="inp0_low")
        ax0.plot(self._inp0, self._inp0_hgh, label="inp0_hgh")
        ax0.legend()

        ax1.set_title("inp1")
        ax1.plot(self._inp1, self._inp1_low, label="inp1_low")
        ax1.plot(self._inp1, self._inp1_hgh, label="inp1_hgh")
        ax1.legend()

        ax2.set_title("out0")
        ax2.plot(self._out0, self._out0_low, label="out0_low")
        ax2.plot(self._out0, self._out0_hgh, label="out0_hgh")
        ax2.legend()

        plt.tight_layout()  # type: ignore
        plt.show()

    def plot_aggregate(self) -> None:
        axs = plt.subplots(nrows=len(self._rules))[1]

        for ax, rule in zip(axs, self._rules):
            ax.set_ylim(0, 1)
            ax.fill_between(self._out0, 0, rule)  # type: ignore
            ax.plot(self._out0, rule)

        plt.tight_layout()  # type: ignore
        plt.show()

    def plot_defuzzify(self) -> None:
        fig = plt.figure()
        ax = fig.add_subplot()

        ax.set_title("out0")
        ax.plot(self._out0, self._out0_low, color="gray")
        ax.plot(self._out0, self._out0_hgh, color="gray")

        tmp_x: list[float] = [self.res_x, self.res_x]
        tmp_y: list[float] = [0, self.res_y]
        ax.plot(tmp_x, tmp_y, color="red")

        plt.show()

    def plot3d(self, resolution: int | None = None) -> None:
        if resolution is None:
            resolution = len(self._universe) - 1

        unsampled: ND = linspace(MIN, MAX, resolution, dtype=TypeN)
        x_axis, y_axis = meshgrid(unsampled, unsampled)
        z_axis: ND = np.zeros_like(x_axis)

        for itr, jtr in product(range(resolution), range(resolution)):
            inp0: float = x_axis[itr, jtr]
            inp1: float = y_axis[itr, jtr]
            self.aggregate(inp0, inp1)
            self.defuzzify()
            z_axis[itr, jtr] = self.res_x

        fig = plt.figure()
        ax = fig.add_subplot(projection=Axes3D.name)
        ax.plot_surface(x_axis, y_axis, z_axis)  # type: ignore

        ax.set_xlabel("inp0")
        ax.set_ylabel("inp1")
        ax.set_zlabel("out0")  # type: ignore

        plt.show()


def main() -> None:
    task = Task(MIN, MAX, STEP)

    task.fuzzify()
    task.plot_fuzzify()

    task.aggregate(X0, X1)
    task.plot_aggregate()

    task.defuzzify("centroid")
    task.plot_defuzzify()
    print(task.res_x, task.res_y)

    task.plot3d()


if __name__ == "__main__":
    main()
