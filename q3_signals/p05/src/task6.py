import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import spectrogram

from src.task3 import make_square_pulse


def main() -> None:
    sample_rate: float = 128
    time: float = 10
    window: float = 0.2

    amp: float = 75
    width: float = 2
    center: float = 5

    dt: float = 1 / sample_rate
    samples: int = round(window * sample_rate)

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = make_square_pulse(timespan, sample_rate, amp, center, width)
    freqs, times, sxx = spectrogram(inp0, sample_rate, "cosine", samples, 0)
    out0: npt.NDArray[np.float64] = np.mean(sxx, axis=0)

    with plt.style.context("seaborn"):
        plot(out0, freqs, times, sxx, xlim=(3, 7), ylim=(0, 30))


def plot(
    out0: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    times: npt.NDArray[np.float64],
    sxx: npt.NDArray[np.float64],
    xlim: tuple[float, float],
    ylim: tuple[float, float],
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 8), ncols=2, nrows=1)

    ax0.plot(times, out0)
    ax0.set_title("Power Spectral Density")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Power, $V^2/Hz$")
    ax0.set_xlim(xlim)
    ax0.set_ylim(ylim)

    ax1.pcolormesh(times, freqs, sxx, shading="gouraud")
    ax1.set_title("Spectrogram")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Amplitude, $V$")
    ax1.set_xlim(xlim)

    plt.colorbar(
        ax=ax1,
        mappable=ax1.collections[0],
        orientation="horizontal",
    )

    plt.show()


if __name__ == "__main__":
    main()
