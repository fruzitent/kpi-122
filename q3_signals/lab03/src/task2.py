import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import lfilter

from src.task1 import get_coefficients
from src.task3 import gain, periods


def main() -> None:
    amp: float = 1
    freq0: float = 10
    hshift: float = 0
    sample_rate: int = 256
    time: int = 1
    vshift: float = 0

    rng: np.random.Generator = np.random.default_rng()
    denumerator, numerator = get_coefficients(rng)
    init: npt.NDArray[np.float64] = rng.random(np.maximum(denumerator.size, numerator.size) - 1)

    timespan: npt.NDArray[np.float64] = np.linspace(0, time, time * sample_rate)
    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan) - hshift) + vshift
    out0: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp0)
    out1: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp0, zi=init)[0]

    with plt.style.context("seaborn"):
        plot(timespan, inp0, out0, out1)

    stats(sample_rate, freq0, inp0, out0, out1)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
    out1: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0, label="Input")
    ax0.plot(timespan, out0, label="Output: None")
    ax0.plot(timespan, out1, label="Output: Rand", linestyle="dashed")
    ax0.legend()
    ax0.set_title("System Response")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Voltage, V")

    plt.show()


def stats(
    sample_rate: int,
    freq0: float,
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
    out1: npt.NDArray[np.float64],
) -> None:
    cycle: int = round(sample_rate / freq0)
    inp0 = inp0[cycle:]
    out0 = out0[cycle:]
    out1 = out1[cycle:]

    print("[None] Gain, db:", 10 * np.log10(gain(inp0, out0)))
    print("[Rand] Gain, db:", 10 * np.log10(gain(inp0, out1)))
    print("[None] Horizontal offset, s:", periods(inp0, out0) / sample_rate)
    print("[Rand] Horizontal offset, s:", periods(inp0, out1) / sample_rate)


if __name__ == "__main__":
    main()
