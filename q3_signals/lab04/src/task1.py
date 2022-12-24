import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    amp: float = 1
    freqs: tuple[float, ...] = 2, 2.5, 40, 100, 600
    hshift: float = 0
    sample_rate: int = 128
    time: int = 1
    vshift: float = 0

    timespan: npt.NDArray[np.float64] = np.arange(0, time, 1 / sample_rate, dtype=np.float64)
    half: int = round(timespan.size / 2)
    out0: npt.NDArray[np.float64] = fftfreq(timespan.size, 1 / sample_rate)[:half]

    for freq0 in freqs:
        inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan) - hshift) + vshift
        out1: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]

        with plt.style.context("seaborn"):
            title: str = f"Sine {freq0} Hz"
            plot(timespan, inp0, out0, out1, title)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
    out1: npt.NDArray[np.float64],
    title: str,
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 10), ncols=1, nrows=2)

    ax0.plot(timespan, inp0)
    ax0.set_title(title)
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Amplitude, V")

    ax1.stem(out0, out1)
    ax1.set_title("Amplitude Spectrum")
    ax1.set_xlabel("Frequency, Hz")
    ax1.set_ylabel("Amplitude, V")

    plt.show()


if __name__ == "__main__":
    main()
