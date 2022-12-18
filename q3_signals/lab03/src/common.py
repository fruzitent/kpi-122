import numpy as np
import pandas as pd
from numpy import typing as npt


def as_db(level: np.float64) -> np.float64:
    return 10 * np.log10(level)  # type: ignore


def get_lag(
    vec0: npt.NDArray[np.float64] | pd.Series[float],
    vec1: npt.NDArray[np.float64] | pd.Series[float],
) -> int:
    cors: npt.NDArray[np.float64] = np.correlate(vec0, vec1, mode="full")
    lags: npt.NDArray[np.int64] = np.arange(-vec1.size + 1, vec0.size)
    return lags[np.argmax(cors)]  # type: ignore


def rms(timespan: npt.NDArray[np.float64] | pd.Series[float]) -> np.float64:
    return np.sqrt(np.mean(timespan**2))  # type: ignore


def sine(
    timespan: npt.NDArray[np.float64] | pd.Series[float],
    amplitude: float = 1,
    horizontal_shift: float = 0,
    vertical_shift: float = 0,
) -> npt.NDArray[np.float64]:
    return amplitude * np.sin(timespan - horizontal_shift) + vertical_shift  # type: ignore
