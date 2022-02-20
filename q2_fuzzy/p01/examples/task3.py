"""
Construct fuzzy set.

Make graphs of fuzzy sets (young, old) using skfuzzy library.
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

    plots: list[plt.Axes] = plt.subplots(2, 1)[1]  # type: ignore
    plot1: plt.Axes = plots[0]
    plot2: plt.Axes = plots[1]

    line1: ND = fuzz.smf(darr, 70, 100)  # np.exp(-(((darr - 100) / 30) ** 2))
    line2: ND = fuzz.zmf(darr, 0, 20)  # np.exp(-((darr / 20) ** 2))
    line3: ND = np.maximum(line2**2, line1**2)
    line4: ND = np.minimum(1 - line2**2, 1 - line1**2)

    plot1.plot(darr, line1, label="old")
    plot1.plot(darr, line2, label="young")
    plot2.plot(darr, line3, label="very young or very old")
    plot2.plot(darr, line4, label="not very young and not very old")

    plot1.grid()
    plot2.grid()
    plot1.legend()
    plot2.legend()
    plt.xlabel("age")
    plt.show()


if __name__ == "__main__":
    main()
