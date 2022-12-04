from dataclasses import dataclass
from typing import Self

from matplotlib import pyplot as plt
from scipy.io import loadmat

from src.common import Signal


@dataclass(frozen=True)
class HR(Signal):
    """Heart rate."""

    @classmethod
    def from_mat(cls, filename: str, key: str, *args, **kwargs) -> Self:
        kwargs["samples"] = loadmat(filename)[key]
        return cls(*args, **kwargs)

    def plot(self, ax: plt.Axes, title: str = "") -> plt.Axes:
        ax = super().plot(ax, title)
        ax.set_ylabel("t, ms")
        return ax


def main() -> None:
    fig: plt.Figure = plt.figure(figsize=(16, 10))
    fig_rows: int = 2
    fig_cols: int = 1

    hr_healthy: HR = HR.from_mat(
        filename="./assets/cardiorhythmogram_healthy.mat",
        key="hr_norm",
        sample_rate=1,
        units="",
    )
    hr_healthy.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 1),
        title="HR Healthy",
    )

    hr_anomalies: HR = HR.from_mat(
        filename="./assets/cardiorhythmogram_disease.mat",
        key="hr_ap",
        sample_rate=1,
        units="",
    )
    hr_anomalies.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 2),
        title="HR Anomalies",
    )


if __name__ == "__main__":
    main()
