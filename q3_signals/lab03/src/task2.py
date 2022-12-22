import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import lfilter

from src.common import as_db, rng, sine
from src.task1 import get_coefficients
from src.task3 import gain, periods

FIG_SIZE: tuple[float, float] = 16, 5


def main() -> None:
    freq: int = 10
    sample_rate: int = 256
    time: int = 1

    denumerator, numerator = get_coefficients()
    init: npt.NDArray[np.float64] = rng.random(np.maximum(denumerator.size, numerator.size) - 1)

    timespan: npt.NDArray[np.float64] = np.linspace(0, time, time * sample_rate)
    inp0: npt.NDArray[np.float64] = sine(2 * np.pi * freq * timespan)
    out0: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp0)
    out1: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp0, zi=init)[0]

    with plt.style.context("seaborn"):
        _, (ax0) = plt.subplots(figsize=FIG_SIZE, ncols=1, nrows=1)

        ax0.plot(timespan, inp0, label="Input")
        ax0.plot(timespan, out0, label="Init: None")
        ax0.plot(timespan, out1, label="Init: Rand", linestyle="dashed")
        ax0.legend()
        ax0.set_title("System Response")
        ax0.set_xlabel("Time, s")
        ax0.set_ylabel("Voltage, V")

        plt.show()

    cycle: int = round(sample_rate / freq)
    inp0 = inp0[cycle:]
    out0 = out0[cycle:]
    out1 = out1[cycle:]

    print("[None] Gain, db:", as_db(gain(inp0, out0)))
    print("[Rand] Gain, db:", as_db(gain(inp0, out1)))
    print("[None] Horizontal offset, s:", periods(inp0, out0) / sample_rate)
    print("[Rand] Horizontal offset, s:", periods(inp0, out1) / sample_rate)


if __name__ == "__main__":
    main()
