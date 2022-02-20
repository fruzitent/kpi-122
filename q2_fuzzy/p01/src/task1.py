import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]

MIN: int = 0
MAX: int = 100
STEP: int = 1
YOUNG_THRESHOLD: int = 20
OLD_THRESHOLD: int = 70


def main() -> None:
    darr: ND = np.arange(MIN, MAX, STEP, dtype=TypeN)
    tmp_young: ND = fuzz.zmf(darr, MIN, YOUNG_THRESHOLD) ** 2
    tmp_old: ND = fuzz.smf(darr, OLD_THRESHOLD, MAX) ** 2
    line1: ND = np.minimum(1 - tmp_young, 1 - tmp_old)
    line2: ND = np.maximum(tmp_young, tmp_old)

    plt.plot(darr, line1, label="not very young and not very old")
    plt.plot(darr, line2, label="very young or very old")

    plt.grid()
    plt.legend()
    plt.xlabel("age")
    plt.show()


if __name__ == "__main__":
    main()
