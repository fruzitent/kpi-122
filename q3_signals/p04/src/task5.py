from itertools import product

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    sample_rate: float = 512
    time: float = 30

    ats: npt.NDArray[np.float64] = np.array([0, 5], dtype=np.float64)
    amps: npt.NDArray[np.float64] = np.array([1, 1, 1], dtype=np.float64)
    widths: npt.NDArray[np.float64] = np.array([0.1, 1, 10], dtype=np.float64)
    max_freqs: list[float] = [200, 20, 2]

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    half: int = round(timespan.size / 2)
    freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

    for at, (idx, width) in product(ats, enumerate(widths)):
        center: float = width / 2
        max_freq: float = max_freqs[idx]

        inp_from: int = round(sample_rate * (center - width / 2 + at))
        inp_upto: int = round(sample_rate * (center + width / 2 + at))

        inp0: npt.NDArray[np.float64] = np.zeros_like(timespan)
        inp0[inp_from:inp_upto] = amps[idx]  # # noqa: WPS362 Found assignment to a subscript slice

        out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]
        out1: npt.NDArray[np.float64] = np.angle(fft(inp0))[:half]

        with plt.style.context("seaborn"):
            title0: str = f"Square Pulse {width} $s$"
            plot(timespan, freqs, inp0, out0, out1, title0, max_freq)


def plot(
    timespan: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
    out1: npt.NDArray[np.float64],
    title: str,
    max_freq: float,
) -> None:
    _, (ax0, ax1, ax2) = plt.subplots(figsize=(16, 15), ncols=1, nrows=3)

    ax0.plot(timespan, inp0)
    ax0.set_title(title)
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Amplitude, $V$")

    ax1.plot(freqs, out0)
    ax1.set_title("Amplitude Spectrum")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Amplitude, $V$")
    ax1.set_xlim(0, max_freq)

    ax2.plot(freqs, out1)
    ax2.set_title("Phase Spectrum")
    ax2.set_xlabel("Frequency, $Hz$")
    ax2.set_ylabel("Phase, $rad$")
    ax2.set_xlim(0, max_freq)

    plt.show()


if __name__ == "__main__":
    main()
