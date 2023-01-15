import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import spectrogram


def main() -> None:
    sample_rate: float = 128
    time: float = 3

    windows: list[float] = [0.2, 0.8, 0.2]
    crosses: list[float] = [0.1, 0.7, 0.9]

    amp: float = 1
    freq: float = 20
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
    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq * timespan) - hshift) + vshift
    inp1: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq * timespan) - hshift) + vshift
    inp0[null0_from:null0_upto] = 0  # noqa: WPS362 Found assignment to a subscript slice
    inp1[null1_from:null1_upto] = 0  # noqa: WPS362 Found assignment to a subscript slice

    for window, cross in zip(windows, crosses):
        samples: int = round(window * sample_rate)

        freqs0, times0, sxx0 = spectrogram(inp0, sample_rate, "cosine", samples, cross * samples)
        freqs1, times1, sxx1 = spectrogram(inp1, sample_rate, "cosine", samples, cross * samples)

        with plt.style.context("seaborn"):
            title0: str = f"Sine {freq} $Hz$, w: {window}, c: {cross}"
            title1: str = f"Sine {freq} $Hz$, w: {window}, c: {cross}"
            plot(timespan, inp0, freqs0, times0, sxx0, title0)
            plot(timespan, inp1, freqs1, times1, sxx1, title1)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    times: npt.NDArray[np.float64],
    sxx: npt.NDArray[np.float64],
    title: str,
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 12.5), ncols=1, nrows=2)

    ax0.plot(timespan, inp0)
    ax0.set_title(title)
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


if __name__ == "__main__":
    main()
