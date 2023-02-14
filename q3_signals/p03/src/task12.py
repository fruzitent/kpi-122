import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import lfilter, square

from src.task1 import get_coefficients


def main() -> None:
    sample_rate: float = 256
    time: float = 1

    duty: float = 0.3
    freq: float = 5

    dt: float = 1 / sample_rate

    rng: np.random.Generator = np.random.default_rng()
    denumerator, numerator = get_coefficients(rng)

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = square(2 * np.pi * freq * timespan, duty)
    out0: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp0)

    with plt.style.context("seaborn"):
        _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

        ax0.plot(timespan, inp0, label="Input")
        ax0.plot(timespan, out0, label="Output")
        ax0.set_title("System Response")
        ax0.set_xlabel("Time, $s$")
        ax0.set_ylabel("Voltage, $V$")

        plt.show()


if __name__ == "__main__":
    main()
