import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import freqz

from src.task1 import get_coefficients


def main() -> None:
    rng: np.random.Generator = np.random.default_rng()
    denumerator, numerator = get_coefficients(rng)

    sample_rate: float = 256
    samples: float = sample_rate * 2 * np.pi
    worn: float = 100

    freq: float = 10

    indicies, response = freqz(numerator, denumerator, worn, fs=samples)
    freqs: npt.NDArray[np.float64] = indicies / 2 / np.pi
    transfer: npt.NDArray[np.float64] = np.abs(response)
    phase: npt.NDArray[np.float64] = np.angle(response)

    with plt.style.context("seaborn"):
        plot(freqs, transfer, phase)

    print("Gain:", np.interp(freq, freqs, transfer))
    print("Horizontal offset:", np.interp(freq, freqs, phase))


def plot(
    freqs: npt.NDArray[np.float64],
    transfer: npt.NDArray[np.float64],
    phase: npt.NDArray[np.float64],
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 10), ncols=1, nrows=2)

    ax0.plot(freqs, transfer)
    ax0.set_title("Frequency response")
    ax0.set_xlabel("Frequency, $Hz$")
    ax0.set_ylabel("Voltage transfer ratio")

    ax1.plot(freqs, phase)
    ax1.set_title("Phase response")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Phases, $rad$")

    plt.show()


if __name__ == "__main__":
    main()
