from dataclasses import dataclass
from typing import Self, Callable

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.interpolate import interp1d
from scipy.io import loadmat

from src.common import Signal


@dataclass(frozen=True)
class HR(Signal):
    """Heart rate."""

    @classmethod
    def from_mat(cls, filepath: str, key: str, *args, **kwargs) -> Self:
        kwargs["samples"] = loadmat(filepath)[key].squeeze()
        return cls(*args, **kwargs)

    def plot(self, ax: plt.Axes, title: str = "") -> plt.Axes:
        ax = super().plot(ax, title)
        ax.set_ylabel(f"t, {self.units}")

        interpolator = interp1d(self.timespan, self.samples, kind="linear")
        timespan_interp: npt.NDArray[np.float64] = np.arange(
            start=0,
            stop=len(self.samples),
            step=self.sample_rate,
            dtype=np.float64,
        )
        samples_interp: npt.NDArray[np.float64] = interpolator(timespan_interp)
        ax.plot(timespan_interp, samples_interp, color="orange")

        return ax


def main() -> None:
    fig: plt.Figure = plt.figure(figsize=(16, 10))
    fig_rows: int = 2
    fig_cols: int = 1

    hr_healthy: HR = HR.from_mat(
        filepath="./assets/hr_healthy_7.mat",
        key="hr_norm",
        sample_rate=1,
        units="ms",
    )
    hr_healthy.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 1),
        title="HR Healthy",
    )

    hr_apnea: HR = HR.from_mat(
        filepath="./assets/hr_apnea_7.mat",
        key="hr_ap",
        sample_rate=1,
        units="ms",
    )
    hr_apnea.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 2),
        title="HR Anomalies",
    )

    plt.show()


if __name__ == "__main__":
    main()
