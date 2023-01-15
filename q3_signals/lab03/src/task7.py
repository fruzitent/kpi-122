import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import lfilter, unit_impulse

from src.task1 import get_coefficients


def main() -> None:
    samples: int = 30
    sample_rate: int = 256
    time: int = 1

    amp: float = 1
    freq0: float = 10
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    rng: np.random.Generator = np.random.default_rng()
    denumerator, numerator = get_coefficients(rng)

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan) - hshift) + vshift
    inp1: npt.NDArray[np.float64] = unit_impulse(samples)

    out0: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp0)
    out1: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp1)
    out2: npt.NDArray[np.float64] = np.convolve(inp0, out1)[:sample_rate]

    with plt.style.context("seaborn"):
        plot(timespan, inp0, out0, out2)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
    out1: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0, label="Input")
    ax0.plot(timespan, out0, label="Output: Difference equation")
    ax0.plot(timespan, out1, label="Output: Impulse function", linestyle="dashed")
    ax0.legend()
    ax0.set_title("System Response")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Voltage, $V$")

    plt.show()


if __name__ == "__main__":
    main()
