import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.io import loadmat


def main() -> None:
    eeg_healthy()
    eeg_epilepsy()


def eeg_healthy() -> None:
    sample_rate: float = 256

    inp0: npt.NDArray[np.float64] = loadmat("./assets/eeg_healthy_7.mat")["sig"][0]
    timespan: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

    with plt.style.context("seaborn"):
        plot_healthy(timespan, inp0)


def plot_healthy(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Electroencephalogram [Healthy]")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Voltage, $μV$")

    plt.show()


def eeg_epilepsy() -> None:
    sample_rate: float = 256

    inp0: npt.NDArray[np.float64] = loadmat("./assets/eeg_epilepsy_7.mat")["sig"][0]
    timespan: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

    with plt.style.context("seaborn"):
        plot_epilepsy(timespan, inp0)


def plot_epilepsy(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Electroencephalogram [Epilepsy]")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Voltage, $μV$")

    plt.show()


if __name__ == "__main__":
    main()
