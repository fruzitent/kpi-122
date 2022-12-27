import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt


def main() -> None:
    sample_rate: float = 256
    time: float = 10

    amp: float = 1
    freq0: float = 1
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq0 * timespan) - hshift) + vshift

    with plt.style.context("seaborn"):
        plot(timespan, inp0)

    stats(inp0, time)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Sine Wave")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Amplitude, V")

    plt.show()


def stats(
    inp0: npt.NDArray[np.float64],
    time: float,
) -> None:
    upto: int = round(inp0.size / (time * 2))
    half: npt.NDArray[np.float64] = inp0[:upto]
    mean: np.float64 = np.sum(half) / half.size
    print("Mean:", mean)


if __name__ == "__main__":
    main()
