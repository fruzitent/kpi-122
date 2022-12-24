from __future__ import annotations

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec


def main() -> None:
    acrobats()
    handball()


def acrobats() -> None:
    board("./assets/cop_acrobats_base_close_7.csv")
    board("./assets/cop_acrobats_base_open_7.csv")
    board("./assets/cop_acrobats_sway_front30_8.csv")
    board("./assets/cop_acrobats_sway_front60_8.csv")
    board("./assets/cop_acrobats_sway_left30_8.csv")
    board("./assets/cop_acrobats_sway_left60_8.csv")


def handball() -> None:
    board("./assets/cop_handball_base_close_7.csv")
    board("./assets/cop_handball_base_open_7.csv")
    board("./assets/cop_handball_sway_front30_6.csv")
    board("./assets/cop_handball_sway_front60_7.csv")
    board("./assets/cop_handball_sway_left30_6.csv")
    board("./assets/cop_handball_sway_left60_7.csv")


def board(filepath: str) -> None:
    df: pd.DataFrame = pd.read_csv(
        delimiter=" ",
        filepath_or_buffer=filepath,
        header=None,
    )

    timespan: pd.Series[float] = df.iloc[:, 0]
    inp0: pd.Series[float] = df.iloc[:, 1]
    inp1: pd.Series[float] = df.iloc[:, 2]
    inp2: pd.Series[float] = df.iloc[:, 3]
    inp3: pd.Series[float] = df.iloc[:, 4]
    inp4: pd.Series[float] = df.iloc[:, 5]
    inp5: pd.Series[float] = df.iloc[:, 6]
    inp6: pd.Series[float] = df.iloc[:, 7]

    with plt.style.context("seaborn"):
        plot(timespan, inp0, inp1, inp2, inp3, inp4, inp5, inp6, filepath)

    stats(inp4, inp5, inp6, filepath)


def plot(
    timespan: pd.Series[float],
    inp0: pd.Series[float],
    inp1: pd.Series[float],
    inp2: pd.Series[float],
    inp3: pd.Series[float],
    inp4: pd.Series[float],
    inp5: pd.Series[float],
    inp6: pd.Series[float],
    filepath: str,
) -> None:
    fig: Figure = plt.figure(figsize=(24, 15))  # type: ignore
    gs: GridSpec = GridSpec(figure=fig, height_ratios=[4, 1], ncols=2, nrows=2)  # type: ignore
    ax0: plt.Axes = fig.add_subplot(gs[0, 0])  # type: ignore
    ax1: plt.Axes = fig.add_subplot(gs[1, 0])  # type: ignore
    ax2: plt.Axes = fig.add_subplot(gs[:, 1])  # type: ignore

    ax0.plot(timespan, inp0, label="Top Left")
    ax0.plot(timespan, inp1, label="Top Right")
    ax0.plot(timespan, inp2, label="Bottom Left")
    ax0.plot(timespan, inp3, label="Bottom Right")
    ax0.legend()
    ax0.set_title("Sensors")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Offset, cm")

    ax1.plot(timespan, inp6, label="Total")
    ax1.set_title("Total")
    ax1.set_xlabel("Time, s")
    ax1.set_ylabel("Offset, cm")

    ax2.plot(inp4, inp5, label="Center of Pressure")
    ax2.set_title("Center of Pressure")
    ax2.set_xlabel("Offset, cm")
    ax2.set_ylabel("Offset, cm")

    fig.suptitle(filepath)

    plt.tight_layout()
    plt.show()


def stats(
    inp4: pd.Series[float],
    inp5: pd.Series[float],
    inp6: pd.Series[float],
    filepath: str,
) -> None:
    methods: list[str] = ["50%", "mean", "std"]
    df: pd.DataFrame = pd.DataFrame()
    df["cop_x"] = inp4.describe().loc[methods]
    df["cop_y"] = inp5.describe().loc[methods]
    df["total"] = inp6.describe().loc[methods]
    df = df.transpose()
    print(f"{filepath}:", df, sep="\n")


if __name__ == "__main__":
    main()
