import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    part1()
    part2()
    part3()


def part1() -> None:
    sample_rate: float = 128
    time: float = 0.5

    noise_amp: float = 10

    amp: float = 1
    freq: float = 20
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    half: int = round(timespan.size / 2)
    freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

    noise: npt.NDArray[np.float64] = np.abs(noise_amp * np.random.randn(timespan.size))
    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq * timespan) - hshift) + vshift
    inp0 += noise - np.average(noise)

    out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]

    with plt.style.context("seaborn"):
        title0: str = f"Sine {freq} $Hz$ + Noise"
        plot(timespan, freqs, inp0, out0, title0)


def part2() -> None:
    sample_rate: float = 128
    times: list[float] = [1, 10, 100, 1000]

    noise_amp: float = 10

    amp: float = 1
    freq: float = 20
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    for time in times:
        timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
        half: int = round(timespan.size / 2)
        freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

        noise: npt.NDArray[np.float64] = np.abs(noise_amp * np.random.randn(timespan.size))
        inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq * timespan) - hshift) + vshift
        inp0 += noise - np.average(noise)

        out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]

        with plt.style.context("seaborn"):
            title: str = f"Sine {freq} $Hz$ + Noise"
            plot(timespan, freqs, inp0, out0, title)


def part3() -> None:
    sample_rates: list[float] = [1280, 12800, 128000]
    time: float = 0.5

    noise_amp: float = 10
    max_freq: float = 100

    amp: float = 1
    freq: float = 20
    hshift: float = 0
    vshift: float = 0

    for sample_rate in sample_rates:
        dt: float = 1 / sample_rate

        timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
        half: int = round(timespan.size / 2)
        freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

        noise: npt.NDArray[np.float64] = np.abs(noise_amp * np.random.randn(timespan.size))
        inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq * timespan) - hshift) + vshift
        inp0 += noise - np.average(noise)

        out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]

        with plt.style.context("seaborn"):
            title: str = f"Sine {freq} $Hz$ + Noise, Sample Rate {sample_rate} $Hz$"
            plot(timespan, freqs, inp0, out0, title, max_freq)


def plot(
    timespan: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    inp: npt.NDArray[np.float64],
    out: npt.NDArray[np.float64],
    title: str,
    max_freq: float | None = None,
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

    if max_freq is not None:
        ax1.set_xlim(0, max_freq)

    plt.show()
