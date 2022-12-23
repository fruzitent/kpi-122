import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt


def main() -> None:
    ecg_healthy()
    ecg_anomaly()


def ecg_healthy() -> None:
    with np.load("./assets/ecg_healthy_7.npz") as npz:
        sample_rate: int = npz["fs"]
        units: str = npz["units"]

        inp0: npt.NDArray[np.float64] = npz["signal"]
        timespan: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

        with plt.style.context("seaborn"):
            plot_healthy(timespan, inp0, units)


def plot_healthy(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    units: str,
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Electrocardiogram [Healthy]")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel(f"Voltage, {units}")

    plt.show()


def ecg_anomaly() -> None:
    with np.load("./assets/ecg_anomaly_7.npz") as npz:
        sample_rate: int = npz["fs"]
        units: str = npz["units"]

        inp0: npt.NDArray[np.float64] = npz["signal"]
        timespan: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

        with plt.style.context("seaborn"):
            plot_anomaly(timespan, inp0, units)


def plot_anomaly(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    units: str,
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Electrocardiogram [Anomaly]")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel(f"Voltage, {units}")

    plt.show()


if __name__ == "__main__":
    main()
