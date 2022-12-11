from __future__ import annotations

from dataclasses import dataclass, field
from typing import Self

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.interpolate import interp1d


@dataclass(kw_only=True)
class Axis(object):  # noqa: H601 class has low (0.00%) cohesion
    label: str = ""
    samples: npt.NDArray[np.float64] = field(default_factory=lambda: np.array([], dtype=np.float64))


@dataclass(kw_only=True)
class Signal(object):
    title: str = ""
    xaxis: Axis = field(default_factory=Axis)
    yaxis: Axis

    def __post_init__(self) -> None:
        if self.xaxis.samples.size == 0:
            self.xaxis.samples = np.arange(
                start=0,
                stop=self.yaxis.samples.size,
                step=1,
                dtype=np.float64,
            )

    def interpolate(self, sample_rate: int, kind: str) -> Self:
        interpolator: interp1d = interp1d(  # type: ignore
            kind=kind,
            x=self.xaxis.samples,
            y=self.yaxis.samples,
        )

        # TODO: possibly wrong?
        timespan: npt.NDArray[np.float64] = np.arange(
            start=0,
            stop=1 / sample_rate * self.xaxis.samples.size,
            step=1 / sample_rate,
            dtype=np.float64,
        )

        self.xaxis.samples = timespan
        self.yaxis.samples = interpolator(timespan)
        return self

    def plot(self, ax: plt.Axes) -> plt.Axes:  # type: ignore
        ax.plot(self.xaxis.samples, self.yaxis.samples, zorder=0)
        ax.grid(True)
        ax.set_title(self.title)
        ax.set_xlabel(self.xaxis.label)
        ax.set_ylabel(self.yaxis.label)
        return ax

    def slice(self, t0: int, t1: int) -> Self:
        self.xaxis.samples = self.xaxis.samples[t0:t1]
        self.yaxis.samples = self.yaxis.samples[t0:t1]
        return self
