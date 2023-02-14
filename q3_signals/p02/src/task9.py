import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.io import loadmat


def main() -> None:
    hr_apnea()
    ecg_anomaly()


def hr_apnea() -> None:
    sample_rate: float = 100

    inp0: npt.NDArray[np.float64] = loadmat("./assets/hr_apnea_7.mat")["hr_ap"].squeeze()
    timespan: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

    mask: npt.NDArray[np.bool_] = cut(timespan, 20, 23)
    inp0 = inp0[mask]
    timespan = timespan[mask]

    with plt.style.context("seaborn"):
        plot_apnea(timespan, inp0)


def plot_apnea(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Heart Rate [Apnea]")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Time, $ms$")

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

        mask: npt.NDArray[np.bool_] = cut(timespan, 0, 5)
        inp0 = inp0[mask]
        timespan = timespan[mask]
        peaks = {
            (peaks_x, peaks_y): peaks_label
            for (peaks_x, peaks_y), peaks_label in peaks.items()
            if peaks_x < timespan[-1]
        }

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

    for (peaks_x, peaks_y), peaks_label in peaks.items():
        ax0.scatter(peaks_x, peaks_y, color="#ff1818")
        ax0.annotate(
            text=peaks_label,
            xy=(peaks_x, peaks_y),
            xytext=(peaks_x + 0.1, peaks_y),
        )

    ax0.set_title("Electrocardiogram [Anomaly]")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel(f"Voltage, ${units}$")

    plt.show()


def cut(samples: npt.NDArray[np.float64], t0: float, t1: float) -> npt.NDArray[np.bool_]:
    if t0 < 0:
        raise ValueError("t0 must be equal or greater than 0")

    if t0 > t1:
        raise ValueError("t0 must be equal or less than t1")

    back: np.float64 = samples[-1]
    if t1 > back:
        raise ValueError(f"t1 must be equal or less than {back}")

    cond0: npt.NDArray[np.bool_] = samples >= t0
    cond1: npt.NDArray[np.bool_] = samples <= t1
    return cond0 & cond1


if __name__ == "__main__":
    main()
