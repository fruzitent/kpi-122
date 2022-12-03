from dataclasses import dataclass

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt


def strip_left(array: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    zero_index: int = int(np.take(np.where(array == 0), 0))
    return array[zero_index:]


@dataclass(frozen=True)
class Signal(object):
    sample_rate: int
    samples: npt.NDArray[np.float64]
    units: str

    @property
    def timespan(self) -> npt.NDArray[np.float64]:
        return np.arange(
            start=0,
            stop=len(self.samples),
            step=1,
            dtype=np.float64,
        )

    def plot(self, ax: plt.Axes, title: str = "") -> plt.Axes:
        ax.plot(self.timespan, self.samples, zorder=0)

        ax.grid(True)
        ax.set_title(title)
        ax.set_xlabel("t, s")
        ax.set_ylabel(f"U, {self.units}")

        rate_indices, time_labels = self.xticks(ax)
        ax.set_xticks(rate_indices)
        ax.set_xticklabels(np.round(time_labels, 2))

        return ax

    def xticks(self, ax: plt.Axes) -> tuple[npt.NDArray[np.int64], npt.NDArray[np.float64]]:
        filtered: npt.NDArray[np.bool_] = ax.get_xticks() < len(self.timespan)
        rate_indices: npt.NDArray[np.int64] = strip_left(ax.get_xticks()[filtered]).astype(np.int64)
        time_labels: npt.NDArray[np.float64] = self.timespan[rate_indices] / self.sample_rate
        return rate_indices, time_labels
