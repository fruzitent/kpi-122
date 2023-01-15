import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq
from scipy.signal.windows import cosine


def main() -> None:
    sample_rate: float = 128
    time: float = 1

    amp: float = 1
    freq0: float = 2
    freq1: float = 2.5
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    half: int = round(timespan.size / 2)
    freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

    window: npt.NDArray[np.float64] = cosine(timespan.size)

    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan) - hshift) + vshift
    inp2: npt.NDArray[np.float64] = inp0 * window
    out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan.size)[:half]
    out2: npt.NDArray[np.float64] = (2 * np.abs(fft(inp2)) / timespan.size)[:half]

    inp1: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq1 * timespan) - hshift) + vshift
    inp3: npt.NDArray[np.float64] = inp1 * window
    out1: npt.NDArray[np.float64] = (2 * np.abs(fft(inp1)) / timespan.size)[:half]
    out3: npt.NDArray[np.float64] = (2 * np.abs(fft(inp3)) / timespan.size)[:half]

    with plt.style.context("seaborn"):
        title0: str = f"Sine {freq0} $Hz$"
        title1: str = f"Sine {freq1} $Hz$"
        plot(timespan, freqs, inp0, inp2, out0, out2, title0)
        plot(timespan, freqs, inp1, inp3, out1, out3, title1)


def plot(
    timespan: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    inp1: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
    out1: npt.NDArray[np.float64],
    title: str,
) -> None:
    _, ((ax0, ax1), (ax2, ax3)) = plt.subplots(figsize=(16, 10), ncols=2, nrows=2)

    ax0.plot(timespan, inp0)
    ax0.set_title(f"{title}")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Amplitude, $V$")

    ax1.plot(timespan, inp1)
    ax1.set_title(f"{title} + window")
    ax1.set_xlabel("Time, $s$")
    ax1.set_ylabel("Amplitude, $V$")

    ax2.stem(freqs, out0)
    ax2.set_title("Amplitude spectrum")
    ax2.set_xlabel("Frequency, $Hz$")
    ax2.set_ylabel("Amplitude, $V$")

    ax3.stem(freqs, out1)
    ax3.set_title("Amplitude spectrum + window")
    ax3.set_xlabel("Frequency, $Hz$")
    ax3.set_ylabel("Amplitude, $V$")

    plt.show()


if __name__ == "__main__":
    main()
