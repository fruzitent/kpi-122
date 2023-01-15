import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    sample_rate: float = 128
    time: float = 3

    amp: float = 1
    freq0: float = 20
    freq1: float = 20
    hshift: float = 0
    vshift: float = 0

    null_samples: int = 10
    null0: float = 1.05
    null1: float = 2

    null0_from: int = round(null0 * sample_rate - null_samples / 2)
    null0_upto: int = round(null0 * sample_rate + null_samples / 2)
    null1_from: int = round(null1 * sample_rate - null_samples / 2)
    null1_upto: int = round(null1 * sample_rate + null_samples / 2)

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    half: int = round(timespan.size / 2)
    freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan) - hshift) + vshift
    inp1: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq1 * timespan) - hshift) + vshift
    inp0[null0_from:null0_upto] = 0  # noqa: WPS362 Found assignment to a subscript slice
    inp1[null1_from:null1_upto] = 0  # noqa: WPS362 Found assignment to a subscript slice

    out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]
    out1: npt.NDArray[np.float64] = (2 * np.abs(fft(inp1)) / timespan.size)[:half]

    with plt.style.context("seaborn"):
        title0: str = f"Sine {freq0} $Hz$, null at {null0} $s$"
        title1: str = f"Sine {freq1} $Hz$, null at {null1} $s$"
        plot(timespan, freqs, inp0, out0, title0)
        plot(timespan, freqs, inp1, out1, title1)


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

    plt.show()


if __name__ == "__main__":
    main()
