import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    sample_rate: float = 1000
    time: float = 10

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    half: int = round(timespan.size / 2)
    freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

    inp0: npt.NDArray[np.float64] = np.random.randn(timespan.size)
    out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]

    with plt.style.context("seaborn"):
        plot(timespan, freqs, inp0, out0)


def plot(
    timespan: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    inp: npt.NDArray[np.float64],
    out: npt.NDArray[np.float64],
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 10), ncols=1, nrows=2)

    ax0.plot(timespan, inp)
    ax0.set_title("Noise")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Amplitude, $V$")

    ax1.stem(freqs, out)
    ax1.set_title("Amplitude Spectrum")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Amplitude, $V$")

    plt.show()


if __name__ == "__main__":
    main()
