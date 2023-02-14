import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import spectrogram


def main() -> None:
    sine()
    noise()
    square()
    sigma()


def sine() -> None:
    sample_rate: float = 128
    time: float = 15
    window: float = 0.2

    amp: float = 1
    freq: float = 40
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate
    samples: int = round(window * sample_rate)

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq * timespan) - hshift) + vshift
    freqs, times, sxx = spectrogram(inp0, sample_rate, "cosine", samples, 0)

    with plt.style.context("seaborn"):
        plot(timespan, inp0, freqs, times, sxx)


def noise() -> None:
    sample_rate: float = 128
    time: float = 15
    window: float = 0.2

    dt: float = 1 / sample_rate
    samples: int = round(window * sample_rate)

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = np.random.randn(timespan.size) / 2
    freqs, times, sxx = spectrogram(inp0, sample_rate, "cosine", samples, 0)

    with plt.style.context("seaborn"):
        plot(timespan, inp0, freqs, times, sxx)


def square() -> None:
    sample_rate: float = 128
    time: float = 15
    window: float = 0.2

    amp: float = 1
    width: float = 1
    center: float = 10

    dt: float = 1 / sample_rate
    samples: int = round(window * sample_rate)

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = make_square_pulse(timespan, sample_rate, amp, center, width)
    freqs, times, sxx = spectrogram(inp0, sample_rate, "cosine", samples, 0)

    with plt.style.context("seaborn"):
        plot(timespan, inp0, freqs, times, sxx)


def sigma() -> None:
    sample_rate: float = 128
    time: float = 15
    window: float = 0.2

    amp0: float = 1
    freq0: float = 40
    hshift0: float = 0
    vshift0: float = 0

    amp2: float = 1
    width2: float = 1
    center2: float = 10

    dt: float = 1 / sample_rate
    samples: int = round(window * sample_rate)

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = amp0 * np.sin((2 * np.pi * freq0 * timespan) - hshift0) + vshift0
    inp1: npt.NDArray[np.float64] = np.random.randn(timespan.size) / 2
    inp2: npt.NDArray[np.float64] = make_square_pulse(timespan, sample_rate, amp2, center2, width2)
    inp3: npt.NDArray[np.float64] = np.sum([inp0 + inp1 + inp2], axis=0)
    freqs, times, sxx = spectrogram(inp3, sample_rate, "cosine", samples, 0)

    with plt.style.context("seaborn"):
        plot(timespan, inp3, freqs, times, sxx)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    times: npt.NDArray[np.float64],
    sxx: npt.NDArray[np.float64],
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 12.5), ncols=1, nrows=2)

    ax0.plot(timespan, inp0)
    ax0.set_title("Signal")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Amplitude, $V$")

    ax1.pcolormesh(times, freqs, sxx, shading="gouraud")
    ax1.set_title("Spectrogram")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Amplitude, $V$")

    plt.colorbar(
        ax=ax1,
        mappable=ax1.collections[0],
        orientation="horizontal",
    )

    plt.show()


def make_square_pulse(
    timespan: npt.NDArray[np.float64],
    sample_rate: float,
    amp: float,
    center: float,
    width: float,
) -> npt.NDArray[np.float64]:
    buffer: npt.NDArray[np.float64] = np.zeros_like(timespan, dtype=np.float64)

    buffer_from: int = round(sample_rate * (center - width / 2))
    buffer_upto: int = round(sample_rate * (center + width / 2))
    if buffer_from < 0 or buffer_upto > len(timespan):
        raise ValueError("out of bounds")

    buffer[buffer_from:buffer_upto] = amp  # noqa: WPS362 Found assignment to a subscript slice
    return buffer


if __name__ == "__main__":
    main()
