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

    eeg_healthy: Signal = Signal(
        title="Electroencephalogram [Healthy]",
        xaxis=Axis(label="Time, s"),
        yaxis=Axis(
            label="Voltage, μV",
            samples=loadmat("./assets/eeg_healthy_7.mat")["sig"][0],
        ),
    )
    eeg_healthy.plot(ax0)

    eeg_epilepsy: Signal = Signal(
        title="Electroencephalogram [Epilepsy]",
        xaxis=Axis(label="Time, s"),
        yaxis=Axis(
            label="Voltage, μV",
            samples=loadmat("./assets/eeg_epilepsy_7.mat")["sig"][0],
        ),
    )
    eeg_epilepsy.plot(ax1)

    plt.show()


if __name__ == "__main__":
    main()
