import pandas as pd
from scipy.io import loadmat
from seaborn import objects as so

PLOT_SIZE: tuple[float, float] = 16, 5


def eeg_healthy() -> None:
    sample_rate: float = 256

    df: pd.DataFrame = pd.DataFrame()
    df["samples"] = loadmat("./assets/eeg_healthy_7.mat")["sig"][0]
    df["timespan"] = df.index.values / sample_rate

    plot: so.Plot = so.Plot(data=df, x="timespan", y="samples")  # type: ignore
    plot = plot.add(so.Line())

    plot = plot.label(
        title="Electroencephalogram [Healthy]",
        x="Time, s",
        y="Voltage, μV",
    )

    plot = plot.layout(size=PLOT_SIZE)
    plot.show()


def eeg_epilepsy() -> None:
    sample_rate: float = 256

    df: pd.DataFrame = pd.DataFrame()
    df["samples"] = loadmat("./assets/eeg_epilepsy_7.mat")["sig"][0]
    df["timespan"] = df.index.values / sample_rate

    plot: so.Plot = so.Plot(data=df, x="timespan", y="samples")  # type: ignore
    plot = plot.add(so.Line())

    plot = plot.label(
        title="Electroencephalogram [Epilepsy]",
        x="Time, s",
        y="Voltage, μV",
    )

    plot = plot.layout(size=PLOT_SIZE)
    plot.show()


def main() -> None:
    eeg_healthy()
    eeg_epilepsy()


if __name__ == "__main__":
    main()
