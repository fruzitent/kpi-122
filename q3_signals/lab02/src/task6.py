from dataclasses import dataclass
from typing import Self

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure, SubFigure
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
from numpy import typing as npt

from src.common import Axis, Signal

TIME_S: str = "Time, s"
OFFSET_CM: str = "Offset, cm"


@dataclass(frozen=True, kw_only=True)
class COP(object):
    """Center of Pressure."""

    title: str = ""

    bottom_left: Signal
    bottom_right: Signal
    top_left: Signal
    top_right: Signal
    total: Signal

    cop: Signal

    @classmethod
    def from_csv(cls, filepath: str, title: str = "") -> Self:
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
        timespan: npt.NDArray[np.float64] = df["timespan"].to_numpy()
        return cls(
            title=title,
            bottom_left=Signal(
                title="Bottom Left",
                xaxis=Axis(
                    label=TIME_S,
                    samples=timespan,
                ),
                yaxis=Axis(
                    label=OFFSET_CM,
                    samples=df["bottom_left"].to_numpy(),
                ),
            ),
            bottom_right=Signal(
                title="Bottom Right",
                xaxis=Axis(
                    label=TIME_S,
                    samples=timespan,
                ),
                yaxis=Axis(
                    label=OFFSET_CM,
                    samples=df["bottom_right"].to_numpy(),
                ),
            ),
            top_left=Signal(
                title="Top Left",
                xaxis=Axis(
                    label=TIME_S,
                    samples=timespan,
                ),
                yaxis=Axis(
                    label=OFFSET_CM,
                    samples=df["top_left"].to_numpy(),
                ),
            ),
            top_right=Signal(
                title="Top Right",
                xaxis=Axis(
                    label=TIME_S,
                    samples=timespan,
                ),
                yaxis=Axis(
                    label=OFFSET_CM,
                    samples=df["top_right"].to_numpy(),
                ),
            ),
            total=Signal(
                title="Total",
                xaxis=Axis(
                    label="Time, ms",
                    samples=timespan,
                ),
                yaxis=Axis(
                    label="Power, F",
                    samples=df["total"].to_numpy(),
                ),
            ),
            cop=Signal(
                title="Center of Pressure",
                xaxis=Axis(
                    label=OFFSET_CM,
                    samples=df["cop_x"].to_numpy(),
                ),
                yaxis=Axis(
                    label=OFFSET_CM,
                    samples=df["cop_y"].to_numpy(),
                ),
            ),
        )

    def plot(self, fig: Figure | SubFigure) -> Figure | SubFigure:  # type: ignore
        gs: GridSpec = GridSpec(figure=fig, ncols=2, nrows=1)  # type: ignore
        gs0: GridSpecFromSubplotSpec = gs[0].subgridspec(ncols=2, nrows=3)  # type: ignore
        gs1: GridSpecFromSubplotSpec = gs[1].subgridspec(ncols=1, nrows=1)  # type: ignore
        self.top_left.plot(fig.add_subplot(gs0[0]))
        self.top_right.plot(fig.add_subplot(gs0[1]))
        self.bottom_left.plot(fig.add_subplot(gs0[2]))
        self.bottom_right.plot(fig.add_subplot(gs0[3]))
        self.total.plot(fig.add_subplot(gs0[4:]))
        self.cop.plot(fig.add_subplot(gs1[0]))
        fig.suptitle(self.title)
        return fig


@dataclass(frozen=True, kw_only=True)
class BalanceBoard(object):
    title: str = ""
    states: dict[str, COP]

    def plot(self, fig: Figure | SubFigure) -> Figure | SubFigure:  # type: ignore
        gs: GridSpec = GridSpec(figure=fig, ncols=1, nrows=len(self.states))  # type: ignore
        for idx, state in enumerate(self.states.values()):
            sfig: SubFigure = fig.add_subfigure(gs[idx])  # type: ignore
            state.plot(sfig)
        fig.suptitle(self.title)
        return fig


def main() -> None:
    fig: Figure = plt.figure(figsize=(80, 96))  # type: ignore
    gs: GridSpec = GridSpec(figure=fig, ncols=2, nrows=1)  # type: ignore
    sfig0: SubFigure = fig.add_subfigure(gs[0])  # type: ignore
    sfig1: SubFigure = fig.add_subfigure(gs[1])  # type: ignore

    acrobats: BalanceBoard = BalanceBoard(
        title="Acrobats",
        states={
            "base_close": COP.from_csv(
                filepath="./assets/cop_acrobats_base_close_7.csv",
                title="Base Close",
            ),
            "base_open": COP.from_csv(
                filepath="./assets/cop_acrobats_base_open_7.csv",
                title="Base Open",
            ),
            "sway_front30": COP.from_csv(
                filepath="./assets/cop_acrobats_sway_front30_8.csv",
                title="Sway Front/Back 30",
            ),
            "sway_front60": COP.from_csv(
                filepath="./assets/cop_acrobats_sway_front60_8.csv",
                title="Sway Front/Back 60",
            ),
            "sway_left30": COP.from_csv(
                filepath="./assets/cop_acrobats_sway_left30_8.csv",
                title="Sway Left/Right 30",
            ),
            "sway_left60": COP.from_csv(
                filepath="./assets/cop_acrobats_sway_left60_8.csv",
                title="Sway Left/Right 60",
            ),
        },
    )
    acrobats.plot(sfig0)

    handball: BalanceBoard = BalanceBoard(
        title="Handball",
        states={
            "base_close": COP.from_csv(
                filepath="./assets/cop_handball_base_close_7.csv",
                title="Base Close",
            ),
            "base_open": COP.from_csv(
                filepath="./assets/cop_handball_base_open_7.csv",
                title="Base Open",
            ),
            "sway_front30": COP.from_csv(
                filepath="./assets/cop_handball_sway_front30_6.csv",
                title="Sway Front/Back 30",
            ),
            "sway_front60": COP.from_csv(
                filepath="./assets/cop_handball_sway_front60_7.csv",
                title="Sway Front/Back 60",
            ),
            "sway_left30": COP.from_csv(
                filepath="./assets/cop_handball_sway_left30_6.csv",
                title="Sway Left/Right 30",
            ),
            "sway_left60": COP.from_csv(
                filepath="./assets/cop_handball_sway_left60_7.csv",
                title="Sway Left/Right 60",
            ),
        },
    )
    handball.plot(sfig1)

    plt.show()


if __name__ == "__main__":
    main()
