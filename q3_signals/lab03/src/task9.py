import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import freqz

from src.task1 import get_coefficients


def main() -> None:
    rng: np.random.Generator = np.random.default_rng()
    denumerator, numerator = get_coefficients(rng)

    indicies, response = freqz(numerator, denumerator)
    freqs: npt.NDArray[np.float64] = indicies / 2 / np.pi
    transfer: npt.NDArray[np.float64] = np.abs(response)

    gain: npt.NDArray[np.float64] = freqs[np.where(transfer > transfer.mean())]

    with plt.style.context("seaborn"):
        plot(freqs, transfer)

    print(gain)


def plot(
    freqs: npt.NDArray[np.float64],
    transfer: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(freqs, transfer)
    ax0.set_title("Frequency Response")
    ax0.set_xlabel("Frequency, $Hz$")
    ax0.set_ylabel("Voltage transfer ratio")

    plt.show()


if __name__ == "__main__":
    main()
