"""
Construct fuzzy set.

Make graphs of fuzzy sets (low, medium, high)
of the parameter "hemoglobin level in blood".
"""

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]

MIN: int = 0
MAX: int = 10
STEP: float = 0.01


def print_plot(plot: plt.Axes, x: ND, y: ND, title: str) -> None:
    plot.set_title(title)
    plot.plot(x, y)


def p_func(darr: ND, s: float, c: float) -> ND:
    step1: ND = (darr - c) ** 2
    step2: float = 2 * s**2
    return np.exp(-step1 / step2)


def s_func(darr: ND, a: float, b: float) -> ND:
    step1: ND = -a * (darr - b)
    step2: ND = np.exp(step1) + 1
    return step2 ** (-1)


def main() -> None:
    darr: ND = np.arange(MIN, MAX, STEP, dtype=TypeN)

    line1: ND = s_func(darr - 1, -5, 2)
    line3: ND = p_func(darr - 4, 0.5, 1)
    line6: ND = s_func(darr - 3, 5, 1)
    line2: ND = 1 - line1**2
    line5: ND = 1 - line6**2
    line4: ND = line5.copy()

    tmp_low: ND = 1 - line1
    tmp_high: ND = 1 - line6
    for itr in range(tmp_low.size):
        line4[itr] = min(tmp_low[itr], tmp_high[itr])

    plots: list[list[plt.Axes]] = plt.subplots(3, 2)[1]
    print_plot(plots[0][0], darr, line1, "low")
    print_plot(plots[0][1], darr, line2, "not very low")
    print_plot(plots[1][0], darr, line3, "average")
    print_plot(plots[1][1], darr, line4, "not low and not high")
    print_plot(plots[2][0], darr, line5, "not very high")
    print_plot(plots[2][1], darr, line6, "high")
    plt.tight_layout()  # type: ignore
    plt.show()


if __name__ == "__main__":
    main()
