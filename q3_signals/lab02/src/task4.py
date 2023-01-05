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

        peaks_x: npt.NDArray[np.float64] = timespan[npz["labels_indexes"]]
        peaks_y: npt.NDArray[np.float64] = inp0[npz["labels_indexes"]]
        peaks_coords: list[tuple[np.float64, np.float64]] = list(zip(peaks_x, peaks_y))
        peaks_labels: list[str] = npz["labels"]
        peaks: dict[tuple[np.float64, np.float64], str] = dict(zip(peaks_coords, peaks_labels))

        with plt.style.context("seaborn"):
            plot_healthy(timespan, inp0, peaks, units)


def plot_healthy(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    peaks: dict[tuple[np.float64, np.float64], str],
    units: str,
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0, zorder=1)

    for (peaks_x, peaks_y), peak_label in peaks.items():
        ax0.scatter(peaks_x, peaks_y, color="#ff1818")
        ax0.annotate(
            text=peak_label,
            xy=(peaks_x, peaks_y),
            xytext=(peaks_x + 0.1, peaks_y),
        )

    ax0.set_title("Electrocardiogram [Healthy]")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel(f"Voltage, ${units}$")

    plt.show()


def ecg_anomaly() -> None:
    with np.load("./assets/ecg_anomaly_7.npz") as npz:
        sample_rate: int = npz["fs"]
        units: str = npz["units"]

        inp0: npt.NDArray[np.float64] = npz["signal"]
        timespan: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

        peaks_x: npt.NDArray[np.float64] = timespan[npz["labels_indexes"]]
        peaks_y: npt.NDArray[np.float64] = inp0[npz["labels_indexes"]]
        peaks_coords: list[tuple[np.float64, np.float64]] = list(zip(peaks_x, peaks_y))
        peaks_labels: list[str] = npz["labels"]
        peaks: dict[tuple[np.float64, np.float64], str] = dict(zip(peaks_coords, peaks_labels))

        with plt.style.context("seaborn"):
            plot_anomaly(timespan, inp0, peaks, units)


def plot_anomaly(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    peaks: dict[tuple[np.float64, np.float64], str],
    units: str,
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0, zorder=1)

    for (peaks_x, peaks_y), peak_label in peaks.items():
        ax0.scatter(peaks_x, peaks_y, color="#ff1818")
        ax0.annotate(
            text=peak_label,
            xy=(peaks_x, peaks_y),
            xytext=(peaks_x + 0.1, peaks_y),
        )

    ax0.set_title("Electrocardiogram [Anomaly]")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel(f"Voltage, ${units}$")

    plt.show()


if __name__ == "__main__":
    main()
