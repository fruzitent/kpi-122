import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt


def main() -> None:
    sample_rate: float = 256
    time: float = 1

    amp: float = 1
    freq0: float = 1
    freq1: float = 10
    freq2: float = 50
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan) - hshift) + vshift
    inp1: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq1 * timespan) - hshift) + vshift
    inp2: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq2 * timespan) - hshift) + vshift
    out0: npt.NDArray[np.float64] = inp0 + inp1 + inp2

    with plt.style.context("seaborn"):
        plot(timespan, inp0, inp1, inp2, out0)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    inp1: npt.NDArray[np.float64],
    inp2: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
) -> None:
    _, (ax0, ax1, ax2, ax3) = plt.subplots(figsize=(16, 20), ncols=1, nrows=4)

    ax0.plot(timespan, inp0)
    ax0.set_title("Sine 1 Hz")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Amplitude, V")

    ax1.plot(timespan, inp1)
    ax1.set_title("Sine 10 Hz")
    ax1.set_xlabel("Time, s")
    ax1.set_ylabel("Amplitude, V")

    ax2.plot(timespan, inp2)
    ax2.set_title("Sine 50 Hz")
    ax2.set_xlabel("Time, s")
    ax2.set_ylabel("Amplitude, V")

    ax3.plot(timespan, out0)
    ax3.set_title("Sine Composite")
    ax3.set_xlabel("Time, s")
    ax3.set_ylabel("Amplitude, V")

    plt.show()


if __name__ == "__main__":
    main()
