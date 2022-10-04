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


class Larsen(object):
    def __init__(self, start: float, end: float, step: float) -> None:
        self._universe: ND = arange(start, end, step, dtype=TypeN)

        self.b0: ND = self._universe.copy()[::-1]
        self._inp1: ND = self._universe.copy()
        self._out0: ND = self._universe.copy()

        self.res_x: float = 0
        self.res_y: float = 0

        self.x11: ND = np.array([0, self.x0, 1], dtype=TypeN)
        self.a11: ND = np.array([1, self.x1, 0], dtype=TypeN)
        self.a12 = self.x11

        self.x22: ND = np.array([0, self.x1, 1], dtype=TypeN)
        self.a21: ND = np.array([1, self.x0, 0], dtype=TypeN)
        self.a22 = self.x22




def main() -> None:
    larsen = Larsen(MIN, MAX, STEP)


if __name__ == '__main__':
    main()
