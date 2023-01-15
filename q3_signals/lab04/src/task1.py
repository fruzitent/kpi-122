import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    sample_rate: int = 128
    time: int = 1

    amp: float = 1
    freq0: float = 2
    freq1: float = 2.5
    freq2: float = 40
    freq3: float = 100
    freq4: float = 600
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    half: int = round(timespan.size / 2)
    freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan) - hshift) + vshift
    inp1: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq1 * timespan) - hshift) + vshift
    inp2: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq2 * timespan) - hshift) + vshift
    inp3: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq3 * timespan) - hshift) + vshift
    inp4: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq4 * timespan) - hshift) + vshift

    out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]
    out1: npt.NDArray[np.float64] = (2 * np.abs(fft(inp1)) / timespan.size)[:half]
    out2: npt.NDArray[np.float64] = (2 * np.abs(fft(inp2)) / timespan.size)[:half]
    out3: npt.NDArray[np.float64] = (2 * np.abs(fft(inp3)) / timespan.size)[:half]
    out4: npt.NDArray[np.float64] = (2 * np.abs(fft(inp4)) / timespan.size)[:half]

    with plt.style.context("seaborn"):
        title0: str = f"Sine {freq0} $Hz$"
        title1: str = f"Sine {freq1} $Hz$"
        title2: str = f"Sine {freq2} $Hz$"
        title3: str = f"Sine {freq3} $Hz$"
        title4: str = f"Sine {freq4} $Hz$"
        plot(timespan, freqs, inp0, out0, title0)
        plot(timespan, freqs, inp1, out1, title1)
        plot(timespan, freqs, inp2, out2, title2)
        plot(timespan, freqs, inp3, out3, title3)
        plot(timespan, freqs, inp4, out4, title4)


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
