from dataclasses import dataclass
from typing import Self

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
from numpy import typing as npt


@dataclass(frozen=True)
class Signal(object):
    timespan: npt.NDArray[np.float64] | pd.Series | None
    samples: npt.NDArray[np.float64] | pd.Series

    def plot(self, ax: plt.Axes, title: str = "") -> plt.Axes:
        if self.timespan is None:
            ax.plot(self.samples)
        else:
            ax.plot(self.timespan, self.samples)
        ax.grid(True)
        ax.set_title(title)
        return ax


@dataclass(frozen=True)
class COP(object):
    """Center of Pressure."""

    bottom_left: Signal
    bottom_right: Signal
    top_left: Signal
    top_right: Signal
    total: Signal

    cop: Signal

    @classmethod
    def from_pandas(cls, filepath: str) -> Self:
        df: pd.DataFrame = pd.read_csv(
            delimiter=" ",
            filepath_or_buffer=filepath,
            header=None,
            names=[
                "timespan",
                "top_left",
                "top_right",
                "bottom_left",
                "bottom_right",
                "cop_x",
                "cop_y",
                "total",
            ],
        )
        return cls(
            bottom_left=Signal(df["timespan"], df["bottom_left"]),
            bottom_right=Signal(df["timespan"], df["bottom_right"]),
            top_left=Signal(df["timespan"], df["top_left"]),
            top_right=Signal(df["timespan"], df["top_right"]),
            total=Signal(df["timespan"], df["total"]),
            cop=Signal(df["cop_x"], df["cop_y"]),
        )

    def plot(self, fig: plt.Figure, title: str = "") -> plt.Figure:
        gs: GridSpec = GridSpec(figure=fig, ncols=2, nrows=1, wspace=0.1)

        gs0: GridSpecFromSubplotSpec = gs[0].subgridspec(ncols=2, nrows=3)
        self.top_left.plot(
            ax=fig.add_subplot(gs0[0]),
            title="Top Left",
        )
        self.top_right.plot(
            ax=fig.add_subplot(gs0[1]),
            title="Top Right",
        )
        self.bottom_left.plot(
            ax=fig.add_subplot(gs0[2]),
            title="Bottom Left",
        )
        self.bottom_right.plot(
            ax=fig.add_subplot(gs0[3]),
            title="Bottom Right",
        )
        self.total.plot(
            ax=fig.add_subplot(gs0[4:]),
            title="Total",
        )

        gs1: GridSpecFromSubplotSpec = gs[1].subgridspec(ncols=1, nrows=1)
        self.cop.plot(
            ax=fig.add_subplot(gs1[0]),
            title="Center of Pressure",
        )

        fig.suptitle(title)
        return fig


@dataclass(frozen=True)
class BalanceBoard(object):
    base_close: COP
    base_open: COP
    sway_front30: COP
    sway_front60: COP
    sway_left30: COP
    sway_left60: COP

    def describe(self) -> pd.DataFrame:
        df: pd.DataFrame = pd.DataFrame()
        for state, signals in self.__dict__.items():
            df[f"{state}.cop_x"] = signals.cop.timespan.describe()
            df[f"{state}.cop_y"] = signals.cop.samples.describe()
            df[f"{state}.total"] = signals.total.samples.describe()
        return df.loc[["mean", "std", "50%"]].transpose().sort_index()

    def plot(self, fig: plt.Figure, title: str = "") -> plt.Figure:
        gs: GridSpec = GridSpec(figure=fig, ncols=1, nrows=6, wspace=0.1)
        self.base_close.plot(
            fig=fig.add_subfigure(gs[0]),
            title="Base Close",
        )
        self.base_open.plot(
            fig=fig.add_subfigure(gs[1]),
            title="Base Open",
        )
        self.sway_front30.plot(
            fig=fig.add_subfigure(gs[2]),
            title="Sway Front/Back 30",
        )
        self.sway_front60.plot(
            fig=fig.add_subfigure(gs[3]),
            title="Sway Front/Back 60",
        )
        self.sway_left30.plot(
            fig=fig.add_subfigure(gs[4]),
            title="Sway Left/Right 30",
        )
        self.sway_left60.plot(
            fig=fig.add_subfigure(gs[5]),
            title="Sway Left/Right 60",
        )
        fig.suptitle(title)
        return fig


def main() -> None:
    fig = plt.figure(figsize=(64, 64))
    gs: GridSpec = GridSpec(figure=fig, ncols=2, nrows=1)

    acrobats: BalanceBoard = BalanceBoard(
        base_close=COP.from_pandas("./assets/cop_acrobats_base_close_7.csv"),
        base_open=COP.from_pandas("./assets/cop_acrobats_base_open_7.csv"),
        sway_front30=COP.from_pandas("./assets/cop_acrobats_sway_front30_8.csv"),
        sway_front60=COP.from_pandas("./assets/cop_acrobats_sway_front60_8.csv"),
        sway_left30=COP.from_pandas("./assets/cop_acrobats_sway_left30_8.csv"),
        sway_left60=COP.from_pandas("./assets/cop_acrobats_sway_left60_8.csv"),
    )
    acrobats.plot(
        fig=fig.add_subfigure(gs[0]),
        title="Acrobats",
    )
    print("Acrobats:", acrobats.describe(), sep="\n")

    handball: BalanceBoard = BalanceBoard(
        base_close=COP.from_pandas("./assets/cop_handball_base_close_7.csv"),
        base_open=COP.from_pandas("./assets/cop_handball_base_open_7.csv"),
        sway_front30=COP.from_pandas("./assets/cop_handball_sway_front30_6.csv"),
        sway_front60=COP.from_pandas("./assets/cop_handball_sway_front60_7.csv"),
        sway_left30=COP.from_pandas("./assets/cop_handball_sway_left30_6.csv"),
        sway_left60=COP.from_pandas("./assets/cop_handball_sway_left60_7.csv"),
    )
    handball.plot(
        fig=fig.add_subfigure(gs[1]),
        title="Handball",
    )
    print("Handball:", handball.describe(), sep="\n")

    plt.show()


if __name__ == "__main__":
    main()
