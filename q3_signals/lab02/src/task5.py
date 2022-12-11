from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from scipy.io import loadmat

from src.common import Axis, Signal


def main() -> None:
    fig: Figure = plt.figure(figsize=(16, 10))  # type: ignore
    fig_rows: int = 2
    fig_cols: int = 1

    ax0: plt.Axes = fig.add_subplot(fig_rows, fig_cols, 1)  # type: ignore
    ax1: plt.Axes = fig.add_subplot(fig_rows, fig_cols, 2)  # type: ignore

    hr_healthy: Signal = Signal(
        title="Heart Rate [Healthy]",
        xaxis=Axis(label="Time, s"),
        yaxis=Axis(
            label="Time, ms",
            samples=loadmat("./assets/hr_healthy_7.mat")["hr_norm"].squeeze(),
        ),
    )
    hr_healthy_interp: Signal = hr_healthy.interpolate(1, kind="linear")
    ax0 = hr_healthy.plot(ax0)
    ax0 = hr_healthy_interp.plot(ax0)
    ax0.legend(["Original", "Interpolated"])

    hr_apnea: Signal = Signal(
        title="Heart Rate [Apnea]",
        xaxis=Axis(label="Time, s"),
        yaxis=Axis(
            label="Time, ms",
            samples=loadmat("./assets/hr_apnea_7.mat")["hr_ap"].squeeze(),
        ),
    )
    hr_apnea_interp: Signal = hr_apnea.interpolate(1, kind="linear")
    ax1 = hr_apnea.plot(ax1)
    ax1 = hr_apnea_interp.plot(ax1)
    ax1.legend(["Original", "Interpolated"])

    plt.show()


if __name__ == "__main__":
    main()
