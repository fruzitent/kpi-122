import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft
from scipy.signal.windows import cosine


def main() -> None:
    samples: int = 256

    half: int = round(samples / 2)

    window: npt.NDArray[np.float64] = cosine(samples)
    out0: npt.NDArray[np.float64] = (2 * np.abs(fft(window)) / samples)[:half]

    with plt.style.context("seaborn"):
        plot(window, out0)


def plot(
    window: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 10), ncols=1, nrows=2)

    ax0.plot(window)
    ax0.set_title("Cosine window")
    ax0.set_xlabel("Samples, $n$")
    ax0.set_ylabel("Amplitude, $V$")

    ax1.stem(out0)
    ax1.set_title("Amplitude spectrum")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Amplitude, $V$")

    plt.show()


if __name__ == "__main__":
    main()
