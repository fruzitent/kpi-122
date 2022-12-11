import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from src.common import Axis, Signal


def main() -> None:
    fig: Figure = plt.figure(figsize=(16, 10))  # type: ignore
    fig_rows: int = 2
    fig_cols: int = 1

    ax0: plt.Axes = fig.add_subplot(fig_rows, fig_cols, 1)  # type: ignore
    ax1: plt.Axes = fig.add_subplot(fig_rows, fig_cols, 2)  # type: ignore

    with np.load("./assets/ecg_healthy_7.npz") as healthy_npz:
        ecg_healthy: Signal = Signal(
            title="Electrocardiogram [Healthy]",
            xaxis=Axis(
                label="Time, s",
                sample_rate=healthy_npz["fs"],
            ),
            yaxis=Axis(
                label=f"Voltage, {healthy_npz['units']}",
                samples=healthy_npz["signal"],
            ),
        )
        ax0 = ecg_healthy.plot(ax0)
        for healthy_x, healthy_text in zip(healthy_npz["labels_indexes"], healthy_npz["labels"]):
            healthy_y: np.float64 = ecg_healthy.yaxis.samples[healthy_x]
            ax0.scatter(healthy_x, healthy_y, color="#ff1818")
            ax0.annotate(
                text=healthy_text,
                xy=(healthy_x, healthy_y),
                xytext=(healthy_x + 50, healthy_y),
            )

    with np.load("./assets/ecg_anomaly_7.npz") as anomaly_npz:
        ecg_anomaly: Signal = Signal(
            title="Electrocardiogram [Anomaly]",
            xaxis=Axis(
                label="Time, s",
                sample_rate=anomaly_npz["fs"],
            ),
            yaxis=Axis(
                label=f"Voltage, {anomaly_npz['units']}",
                samples=anomaly_npz["signal"],
            ),
        )
        ax1 = ecg_anomaly.plot(ax1)
        for anomaly_x, anomaly_text in zip(anomaly_npz["labels_indexes"], anomaly_npz["labels"]):
            anomaly_y: np.float64 = ecg_anomaly.yaxis.samples[anomaly_x]
            ax1.scatter(anomaly_x, anomaly_y, color="#ff1818")
            ax1.annotate(
                text=anomaly_text,
                xy=(anomaly_x, anomaly_y),
                xytext=(anomaly_x + 50, anomaly_y),
            )

    plt.show()


if __name__ == "__main__":
    main()
