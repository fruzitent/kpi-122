import numpy as np
from numpy import typing as npt

from src.common import rng

# 3379786959 | max = 0.25, mean = 0.25
# 899906383  | max = 0.60, mean = 0.25
# 462902678  | max = 0.75, mean = 0.75
# 4062541548 | max = 0.90, mean = 1.20
# 3393353340 | max = 1.50, mean = 0.55
# 4039093075 | max = 1.50, mean = 1.00


def get_coefficients() -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    d0: int = rng.integers(0, 10)
    d1: int = rng.integers(0, 10)
    m0: int = rng.integers(0, 10)
    m1: int = rng.integers(0, 10)
    p0: int = rng.integers(0, 10)
    p1: int = rng.integers(0, 10)
    p2: int = rng.integers(0, 10)

    denumerator: npt.NDArray[np.float64] = np.array(
        [1, (d0 + d1) / 150, (p0 - d0) / 140, 0, -d1 / 130, -(m1 - d0) / 150],
        dtype=np.float64,
    )
    numerator: npt.NDArray[np.float64] = np.array(
        [m0 / 20, (p1 - d1) / 10, -(m1 - m0) / 20, -p2 / 20, d1 / 30, -m1 / 20],
        dtype=np.float64,
    )

    return denumerator, numerator
