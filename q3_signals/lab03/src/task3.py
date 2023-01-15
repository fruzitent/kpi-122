import numpy as np
from numpy import typing as npt
from scipy.signal import lfilter

from src.task1 import get_coefficients


def main() -> None:
    sample_rate: float = 256
    time: float = 1

    amp: float = 1
    freq: float = 10
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    rng: np.random.Generator = np.random.default_rng()
    denumerator, numerator = get_coefficients(rng)

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq * timespan) - hshift) + vshift
    out0: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp0)

    print("Gain, db:", 10 * np.log10(gain(inp0, out0)))
    print("Horizontal offset, s:", periods(inp0, out0) / sample_rate)


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


if __name__ == "__main__":
    main()
