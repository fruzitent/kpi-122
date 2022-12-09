import numpy as npt
import pandas as pd
from matplotlib import pyplot as plt

from src.task6 import Signal


def main() -> None:
    df: pd.DataFrame = pd.read_csv("./assets/Subject7_SpO2Hr.csv")
    df.drop(columns=["Unnamed: 0"], inplace=True)
    # print(df)

    interval: int = 30

    fig: plt.Figure = plt.figure(figsize=(16, 10))
    fig_rows: int = 2
    fig_cols: int = 2

    spo2: Signal = Signal(df["Elapsed time(seconds)"], df["SpO2(%)"])
    spo2.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 1),
        title="Arterial blood saturation with oxygen",
    )

    spo2_avg: Signal = Signal(
        df["Elapsed time(seconds)"],
        spo2.samples.rolling(window=interval).mean(),
    )
    spo2_avg.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 3),
        title="Arterial blood saturation with oxygen interval",
    )

    hr: Signal = Signal(df["Elapsed time(seconds)"], df["hr (bpm)"])
    hr.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 2),
        title="Heart Rate",
    )

    hr_avg: Signal = Signal(
        df["Elapsed time(seconds)"],
        hr.samples.rolling(window=interval).mean(),
    )
    hr_avg.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 4),
        title="Heart Rate interval",
    )

    plt.show()


if __name__ == "__main__":
    main()
