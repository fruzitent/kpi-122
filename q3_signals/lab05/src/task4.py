import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import typing as npt
from scipy.signal import spectrogram


def main() -> None:
    sample_rate: float = 256
    time0: float = 10
    time1: float = 20

    amp: float = 1
    freq0: float = 10
    freq1: float = 100
    hshift: float = 0
    vshift: float = 0

    windows: list[float] = [0.1, 2, 1]
    crosses: list[float] = [0, 0, 0.5]

    dt: float = 1 / sample_rate

    timespan0: npt.NDArray[np.float64] = np.arange(0, time0, dt, dtype=np.float64)
    timespan1: npt.NDArray[np.float64] = np.arange(0, time1, dt, dtype=np.float64)

    sig0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan0) - hshift) + vshift
    sig1: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq1 * timespan0) - hshift) + vshift

    inp0: npt.NDArray[np.float64] = sig0 + sig1
    inp1: npt.NDArray[np.float64] = np.concatenate([2 * sig0, 2 * sig1])
    inp2: npt.NDArray[np.float64] = np.concatenate([2 * sig1, 2 * sig0])

    for window, cross in zip(windows, crosses):
        samples: int = round(window * sample_rate)
        freqs0, times0, sxx0 = spectrogram(inp0, sample_rate, "cosine", samples, cross * samples)
        freqs1, times1, sxx1 = spectrogram(inp1, sample_rate, "cosine", samples, cross * samples)
        freqs2, times2, sxx2 = spectrogram(inp2, sample_rate, "cosine", samples, cross * samples)

        with plt.style.context("seaborn"):
            title0: str = f"Sine {freq0} $Hz$, w: {window}, c: {cross}"
            title1: str = f"Sine {freq0} $Hz$ + {freq1} $Hz$, w: {window}, c: {cross}"
            title2: str = f"Sine {freq1} $Hz$ + {freq0} $Hz$, w: {window}, c: {cross}"
            plot(timespan0, inp0, freqs0, times0, sxx0, title0)
            plot(timespan1, inp1, freqs1, times1, sxx1, title1)
            plot(timespan1, inp2, freqs2, times2, sxx2, title2)

    window0: float = 0.1
    cross0: float = 0
    samples0: int = round(window0 * sample_rate)

    freqs0, times0, sxx0 = spectrogram(inp0, sample_rate, "cosine", samples0, cross0 * samples0)
    freqs1, times1, sxx1 = spectrogram(inp1, sample_rate, "cosine", samples0, cross0 * samples0)

    m_times0, m_freqs0 = np.meshgrid(times0, freqs0)
    m_times1, m_freqs1 = np.meshgrid(times1, freqs1)

    with plt.style.context("seaborn"):
        plot3d(m_freqs0, m_freqs1, m_times0, m_times1, sxx0, sxx1)


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


def plot3d(
    m_freqs0: npt.NDArray[np.float64],
    m_freqs1: npt.NDArray[np.float64],
    m_times0: npt.NDArray[np.float64],
    m_times1: npt.NDArray[np.float64],
    sxx0: npt.NDArray[np.float64],
    sxx1: npt.NDArray[np.float64],
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 16), ncols=2, nrows=1, subplot_kw={"projection": Axes3D.name})

    ax0.plot_surface(m_freqs0, m_times0, sxx0, cmap="viridis")
    ax1.set_title("Width 0.1 $s$, Cross $50%$")
    ax0.set_xlabel("Frequency, $Hz$")
    ax0.set_ylabel("Time, $s$")
    ax0.set_zlabel("SPD, $dB/Hz$")

    ax1.plot_surface(m_freqs1, m_times1, sxx1, cmap="viridis")
    ax1.set_title("Width 0.1 $s$, Cross $50%$")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Time, $s$")
    ax1.set_zlabel("SPD, $dB/Hz$")

    plt.show()


if __name__ == "__main__":
    main()
