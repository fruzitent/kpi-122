import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from numpy import typing as npt

from src.common import Axis, Signal


def main() -> None:
    fig: Figure = plt.figure(figsize=(16, 10))  # type: ignore
    fig_rows: int = 2
    fig_cols: int = 2

    ax0: plt.Axes = fig.add_subplot(fig_rows, fig_cols, 1)  # type: ignore
    ax1: plt.Axes = fig.add_subplot(fig_rows, fig_cols, 2)  # type: ignore
    ax2: plt.Axes = fig.add_subplot(fig_rows, fig_cols, 3)  # type: ignore
    ax3: plt.Axes = fig.add_subplot(fig_rows, fig_cols, 4)  # type: ignore

    df: pd.DataFrame = pd.read_csv("./assets/Subject7_SpO2Hr.csv")
    df.drop(columns=["Unnamed: 0"], inplace=True)
    elapsed_time: npt.NDArray[np.float64] = df["Elapsed time(seconds)"].to_numpy()

    spo2: Signal = Signal(
        title="Arterial blood saturation with oxygen",
        xaxis=Axis(
            label="Time, s",
            samples=elapsed_time,
        ),
        yaxis=Axis(
            label="SpO2, %",
            samples=df["SpO2(%)"].to_numpy(),
        ),
    )
    spo2.plot(ax0)

    spo2_avg = spo2
    spo2_avg.title = f"{spo2.title} [Rolling Average]"
    spo2_avg.xaxis.samples = elapsed_time
    spo2_avg.yaxis.samples = pd.Series(spo2.yaxis.samples).rolling(window=30).mean().to_numpy()
    spo2_avg.plot(ax2)

    hr: Signal = Signal(
        title="Heart Rate",
        xaxis=Axis(
            label="Time, s",
            samples=elapsed_time,
        ),
        yaxis=Axis(
            label="Rate, bpm",
            samples=df["hr (bpm)"].to_numpy(),
        ),
    )
    hr.plot(ax1)

    hr_avg = hr
    hr_avg.title = f"{hr.title} [Rolling Average]"
    hr_avg.xaxis.samples = elapsed_time
    hr_avg.yaxis.samples = pd.Series(hr.yaxis.samples).rolling(window=30).mean().to_numpy()
    hr_avg.plot(ax3)

    plt.show()


if __name__ == "__main__":
    main()
