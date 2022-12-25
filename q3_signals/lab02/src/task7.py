from __future__ import annotations

import pandas as pd
from matplotlib import pyplot as plt


def main() -> None:
    window: int = 30

    df: pd.DataFrame = pd.read_csv("./assets/Subject7_SpO2Hr.csv")

    timespan: pd.Series[float] = df.iloc[:, 1]
    inp0: pd.Series[float] = df.iloc[:, 2]
    inp1: pd.Series[float] = df.iloc[:, 3]
    out0: pd.Series[float] = inp0.rolling(window).mean()
    out1: pd.Series[float] = inp1.rolling(window).mean()

    with plt.style.context("seaborn"):
        plot(timespan, inp0, inp1, out0, out1)


def plot(
    timespan: pd.Series[float],
    inp0: pd.Series[float],
    inp1: pd.Series[float],
    out0: pd.Series[float],
    out1: pd.Series[float],
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 10), ncols=1, nrows=2)

    ax0.plot(timespan, inp0, label="Original")
    ax0.plot(timespan, out0, label="Rolling")
    ax0.legend()
    ax0.set_title("Arterial blood saturation with oxygen")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("SpO2, %")

    ax1.plot(timespan, inp1, label="Original")
    ax1.plot(timespan, out1, label="Rolling")
    ax1.legend()
    ax1.set_title("Heart Rate")
    ax1.set_xlabel("Time, s")
    ax1.set_ylabel("Rate, bpm")

    plt.show()


if __name__ == "__main__":
    main()
