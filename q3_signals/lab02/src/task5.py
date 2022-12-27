import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.interpolate import interp1d
from scipy.io import loadmat


def main() -> None:
    hr_healthy()
    hr_apnea()


def hr_healthy() -> None:
    sample_rate: float = 1

    inp0: npt.NDArray[np.float64] = loadmat("./assets/hr_healthy_7.mat")["hr_norm"].squeeze()[1:]
    timespan0: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

    interpolator: interp1d = interp1d(
        kind="cubic",
        x=np.cumsum(inp0) / 1000,
        y=inp0,
    )

    timespan1: npt.NDArray[np.float64] = np.arange(
        start=interpolator.x[0],
        stop=interpolator.x[-1],
        step=1 / sample_rate,
        dtype=np.float64,
    )
    inp1: npt.NDArray[np.float64] = interpolator(timespan1)

    with plt.style.context("seaborn"):
        plot_healthy(timespan0, timespan1, inp0, inp1)


def plot_healthy(
    timespan0: npt.NDArray[np.float64],
    timespan1: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    inp1: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan0, inp0, label="Original")
    ax0.plot(timespan1, inp1, label="Interpolated")
    ax0.legend()
    ax0.set_title("Heart Rate [Healthy]")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Time, ms")

    plt.show()


def hr_apnea() -> None:
    sample_rate: float = 1

    inp0: npt.NDArray[np.float64] = loadmat("./assets/hr_apnea_7.mat")["hr_ap"].squeeze()
    timespan0: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

    interpolator: interp1d = interp1d(
        kind="cubic",
        x=np.cumsum(inp0) / 1000,
        y=inp0,
    )

    timespan1: npt.NDArray[np.float64] = np.arange(
        start=interpolator.x[0],
        stop=interpolator.x[-1],
        step=1 / sample_rate,
        dtype=np.float64,
    )
    inp1: npt.NDArray[np.float64] = interpolator(timespan1)

    with plt.style.context("seaborn"):
        plot_apnea(timespan0, timespan1, inp0, inp1)


def plot_apnea(
    timespan0: npt.NDArray[np.float64],
    timespan1: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    inp1: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan0, inp0, label="Original")
    ax0.plot(timespan1, inp1, label="Interpolated")
    ax0.legend()
    ax0.set_title("Heart Rate [Apnea]")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Time, ms")

    plt.show()


if __name__ == "__main__":
    main()
