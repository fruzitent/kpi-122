import numpy as np
from numpy import typing as npt


def gain(
    vec0: npt.NDArray[np.float64],
    vec1: npt.NDArray[np.float64],
) -> np.float64:
    return rms(vec1) / rms(vec0)


def periods(
    vec0: npt.NDArray[np.float64],
    vec1: npt.NDArray[np.float64],
) -> int:
    cors: npt.NDArray[np.float64] = np.correlate(vec0, vec1, mode="full")
    lags: npt.NDArray[np.int64] = np.arange(-vec1.size + 1, vec0.size)
    return lags[np.argmax(cors)]  # type: ignore


def rms(samples: npt.NDArray[np.float64]) -> np.float64:
    return np.sqrt(np.mean(samples**2))  # type: ignore
