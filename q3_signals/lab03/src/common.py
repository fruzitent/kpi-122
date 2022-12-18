from __future__ import annotations

from time import time_ns

import numpy as np
import pandas as pd
from numpy import typing as npt

seed: int = time_ns() % 2**32
rng: np.random.Generator = np.random.default_rng(seed)
print("Seed:", seed)


def as_db(level: np.float64) -> np.float64:
    return 10 * np.log10(level)  # type: ignore


def sine(
    timespan: npt.NDArray[np.float64] | pd.Series[float],
    amplitude: float = 1,
    horizontal_shift: float = 0,
    vertical_shift: float = 0,
) -> npt.NDArray[np.float64]:
    return amplitude * np.sin(timespan - horizontal_shift) + vertical_shift  # type: ignore
