import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec
from seaborn import objects as so

PLOT_SIZE: tuple[float, float] = 32, 16


def board(filepath: str) -> None:
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

    stats: pd.DataFrame = df.describe()
    stats = stats.loc[["50%", "mean", "std"]]
    stats = stats.transpose()
    stats = stats.loc[["cop_x", "cop_y", "total"]]
    print(f"{filepath}:", stats, sep="\n")

    fig: Figure = plt.figure(figsize=PLOT_SIZE)  # type: ignore
    gs: GridSpec = GridSpec(figure=fig, height_ratios=[4, 1], ncols=2, nrows=2)  # type: ignore
    sfig00: plt.Axes = fig.add_subfigure(gs[0, 0])  # type: ignore
    sfig10: plt.Axes = fig.add_subfigure(gs[1, 0])  # type: ignore
    sfig01: plt.Axes = fig.add_subfigure(gs[:, 1])  # type: ignore

    raw: pd.DataFrame = df.melt(
        id_vars=["timespan"],
        value_name="samples",
        value_vars=[
            "bottom_left",
            "bottom_right",
            "top_left",
            "top_right",
        ],
        var_name="signal",
    )

    plot: so.Plot = so.Plot(data=raw, x="timespan", y="samples")  # type: ignore
    plot = plot.add(so.Lines(), color="signal", legend=None)

    plot = plot.label(
        title="Sensors",
        x="Time, s",
        y="Offset, cm",
    )

    plot = plot.on(sfig00)
    plot.plot()

    plot: so.Plot = so.Plot(data=df, x="timespan", y="total")  # type: ignore
    plot = plot.add(so.Path())

    plot = plot.label(
        title="Total",
        x="Time, s",
        y="Offset, cm",
    )

    plot = plot.on(sfig10)
    plot.plot()

    plot: so.Plot = so.Plot(data=df, x="cop_x", y="cop_y")  # type: ignore
    plot = plot.add(so.Path())

    plot = plot.label(
        title="Center of Pressure",
        x="Offset, cm",
        y="Offset, cm",
    )

    plot = plot.on(sfig01)
    plot.plot()

    plot.show()


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


def main() -> None:
    acrobats()
    handball()


if __name__ == "__main__":
    main()
