import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    sample_rate: float = 1000
    time: float = 1

    null_samples: list[int] = [0, 10, 100, 1000, 10000]

    amp: float = 1
    freq0: float = 20.5
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    half: int = round(timespan.size / 2)
    freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

    sig0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan) - hshift) + vshift

    for null in null_samples:
        overhead: float = null / sample_rate

        timespan = np.arange(0, time + overhead, dt, dtype=np.float64)
        half = round(timespan.size / 2)
        freqs = fftfreq(timespan.size, dt)[:half]

        inp0: npt.NDArray[np.float64] = np.concatenate([sig0, np.zeros(null)])
        out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]

        with plt.style.context("seaborn"):
            title: str = f"Sine {freq0} $Hz$"
            plot(timespan, freqs, inp0, out0, title)


def plot(
    timespan: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    inp: npt.NDArray[np.float64],
    out: npt.NDArray[np.float64],
    title: str,
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 10), ncols=1, nrows=2)

    ax0.plot(timespan, inp)
    ax0.set_title(title)
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Amplitude, $V$")

    ax1.stem(freqs, out)
    ax1.set_title("Amplitude Spectrum")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Amplitude, $V$")
    ax1.set_xlim(19, 22)

    plt.show()


if __name__ == "__main__":
    main()
