from dataclasses import dataclass
from typing import Self

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt

from src.common import Signal


@dataclass(frozen=True)
class ECG(Signal):
    """Electrocardiogram."""

    description: np.str_
    label_indices: npt.NDArray[np.int64]
    labels: npt.NDArray[np.str_]
    source: np.str_
    t0: np.int64
    t1: np.int64

    @classmethod
    def from_npz(cls, filepath: str) -> Self:
        with np.load(filepath) as npz_file:
            return cls(
                description=np.take(npz_file["description"], 0),
                label_indices=npz_file["labels_indexes"],
                labels=npz_file["labels"],
                sample_rate=np.take(npz_file["fs"], 0),
                samples=npz_file["signal"],
                source=np.take(npz_file["source"], 0),
                t0=np.take(npz_file["source_start"], 0),
                t1=np.take(npz_file["source_end"], 0),
                units=np.take(npz_file["units"], 0),
            )

    def plot(self, ax: plt.Axes, title: str = "") -> plt.Axes:
        ax = super().plot(ax, title)

        label_offset: int = 50
        for label_x, label_text in zip(self.label_indices, self.labels):
            label_y: np.float64 = self.samples[label_x]
            ax.annotate(
                text=label_text,
                xy=(label_x, label_y),
                xytext=(label_x + label_offset, label_y),
            )
            ax.stem(label_x, label_y)

        _, time_labels = self.xticks(ax)
        timespan_offset: np.float64 = np.abs(self.t1 - self.t0) / self.sample_rate
        ax.set_xticklabels(time_labels + timespan_offset)

        return ax


def main() -> None:
    fig: plt.Figure = plt.figure(figsize=(16, 10))
    fig_rows: int = 2
    fig_cols: int = 1

    ecg_healthy: ECG = ECG.from_npz("./assets/ecg_healthy_7.npz")
    ecg_healthy.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 1),
        title="ECG Healthy",
    )

    ecg_anomaly: ECG = ECG.from_npz("./assets/ecg_anomaly_7.npz")
    ecg_anomaly.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 2),
        title="ECG Anomalies",
    )

    plt.show()


if __name__ == "__main__":
    main()
