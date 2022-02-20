"""
Construct fuzzy set.

...?
"""

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal.windows import gaussian

TypeN = np.float64
ND = npt.NDArray[TypeN]

MIN: int = 0
MAX: int = 100
STEP: int = 1


def s_func(darr: ND) -> ND:
    step1: ND = darr / 20
    step2: ND = np.power(step1, 4)
    return np.power(step2 + 1, -1)


def z_func(darr: ND) -> ND:
    step1: ND = (darr - 100) / 30
    step2: ND = np.power(step1, 6)
    return np.power(step2 + 1, -1)


def main() -> None:
    darr: ND = np.arange(MIN, MAX, STEP, dtype=TypeN)

    line1: ND = gaussian(100, 15)
    line2: ND = s_func(darr)
    line3: ND = s_func(darr) ** 2
    line4: ND = z_func(darr)
    line5: ND = z_func(darr) ** 2

    plt.plot(darr, line1, label="?")
    plt.plot(darr, line2, label="?")
    plt.plot(darr, line3, label="?")
    plt.plot(darr, line4, label="?")
    plt.plot(darr, line5, label="?")

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("mu")
    plt.show()


if __name__ == "__main__":
    main()
