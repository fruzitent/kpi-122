import numpy as np
import pandas as pd
from numpy import typing as npt
from scipy.interpolate import interp1d
from scipy.io import loadmat
from seaborn import objects as so

PLOT_SIZE: tuple[float, float] = 16, 5


def hr_healthy() -> None:
    sample_rate: float = 1

    df: pd.DataFrame = pd.DataFrame()
    df["original"] = loadmat("./assets/hr_healthy_7.mat")["hr_norm"].squeeze()[1:]
    df["timespan"] = df.index.values / sample_rate

    interpolator: interp1d = interp1d(  # type: ignore
        kind="cubic",
        x=np.cumsum(df["original"]) / 1000,
        y=df["original"],
    )
    timespan: npt.NDArray[np.float64] = np.arange(
        start=interpolator.x[0],
        stop=interpolator.x[-1],
        step=1 / sample_rate,
        dtype=np.float64,
    )
    df["interpolated"] = pd.Series(interpolator(timespan))

    df = df.melt(
        id_vars=["timespan"],
        value_name="samples",
        value_vars=["original", "interpolated"],
        var_name="signal",
    )

    plot: so.Plot = so.Plot(data=df, x="timespan", y="samples")  # type: ignore
    plot = plot.add(so.Line(), color="signal")

    plot = plot.label(
        title="Heart Rate [Healthy]",
        x="Time, s",
        y="Time, ms",
    )

    plot = plot.layout(size=PLOT_SIZE)
    plot.show()


def hr_apnea() -> None:
    sample_rate: float = 1

    df: pd.DataFrame = pd.DataFrame()
    df["original"] = loadmat("./assets/hr_apnea_7.mat")["hr_ap"].squeeze()
    df["timespan"] = df.index.values / sample_rate

    interpolator: interp1d = interp1d(  # type: ignore
        kind="cubic",
        x=np.cumsum(df["original"]) / 1000,
        y=df["original"],
    )
    timespan: npt.NDArray[np.float64] = np.arange(
        start=interpolator.x[0],
        stop=interpolator.x[-1],
        step=1 / sample_rate,
        dtype=np.float64,
    )
    df["interpolated"] = pd.Series(interpolator(timespan))

    df = df.melt(
        id_vars=["timespan"],
        value_name="samples",
        value_vars=["original", "interpolated"],
        var_name="signal",
    )

    plot: so.Plot = so.Plot(data=df, x="timespan", y="samples")  # type: ignore
    plot = plot.add(so.Line(), color="signal")

    plot = plot.label(
        title="Heart Rate [Apnea]",
        x="Time, s",
        y="Time, ms",
    )

    plot = plot.layout(size=PLOT_SIZE)
    plot.show()


def main() -> None:
    hr_healthy()
    hr_apnea()


if __name__ == "__main__":
    main()
