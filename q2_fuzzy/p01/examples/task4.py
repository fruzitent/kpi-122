"""
Construct fuzzy set.

Make graphs of fuzzy sets (young, middle age, old) using skfuzzy library.
"""

import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]

MIN: int = 0
MAX: int = 100
STEP: int = 1


def main() -> None:
    darr: ND = np.arange(MIN, MAX, STEP, dtype=TypeN)

    line1: ND = fuzz.gaussmf(darr, 30, 10)
    line2: ND = fuzz.smf(darr, 35, 80)
    line3: ND = fuzz.zmf(darr, 0, 20)
    line4: ND = line2**0.5
    line5: ND = 1 - line1**2

    plt.plot(darr, line1, label="middle age")
    plt.plot(darr, line2, label="old")
    plt.plot(darr, line3, label="young")
    plt.plot(darr, line4, label="slightly old")
    plt.plot(darr, line5, label="not middle age")

    plt.grid()
    plt.legend()
    plt.xlabel("age")
    plt.show()


if __name__ == "__main__":
    main()
