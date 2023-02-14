from __future__ import annotations

import pandas as pd
from matplotlib import pyplot as plt


def main() -> None:
    steady()
    walking()
    running()


def steady() -> None:
    df: pd.DataFrame = pd.read_csv("./assets/Sensor_record_20230105_221851_AndroSensor.csv")

    timespan: pd.Series[float] = df.iloc[:, 3] / 1000
    inp0: pd.Series[float] = df.iloc[:, 0]
    inp1: pd.Series[float] = df.iloc[:, 1]
    inp2: pd.Series[float] = df.iloc[:, 2]

    with plt.style.context("seaborn"):
        plot_steady(timespan, inp0, inp1, inp2)


def plot_steady(
    timespan: pd.Series[float],
    inp0: pd.Series[float],
    inp1: pd.Series[float],
    inp2: pd.Series[float],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0, label="X")
    ax0.plot(timespan, inp1, label="Y")
    ax0.plot(timespan, inp2, label="Z")
    ax0.legend()
    ax0.set_title("Steady")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Acceleration, $m/s^2$")

    plt.show()


def walking() -> None:
    df: pd.DataFrame = pd.read_csv("./assets/Sensor_record_20230105_220434_AndroSensor.csv")

    timespan: pd.Series[float] = df.iloc[:, 3] / 1000
    inp0: pd.Series[float] = df.iloc[:, 0]
    inp1: pd.Series[float] = df.iloc[:, 1]
    inp2: pd.Series[float] = df.iloc[:, 2]

    with plt.style.context("seaborn"):
        plot_walking(timespan, inp0, inp1, inp2)


def plot_walking(
    timespan: pd.Series[float],
    inp0: pd.Series[float],
    inp1: pd.Series[float],
    inp2: pd.Series[float],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0, label="X")
    ax0.plot(timespan, inp1, label="Y")
    ax0.plot(timespan, inp2, label="Z")
    ax0.legend()
    ax0.set_title("Walking")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Acceleration, $m/s^2$")

    plt.show()


def running() -> None:
    df: pd.DataFrame = pd.read_csv("./assets/Sensor_record_20230105_220523_AndroSensor.csv")

    timespan: pd.Series[float] = df.iloc[:, 3] / 1000
    inp0: pd.Series[float] = df.iloc[:, 0]
    inp1: pd.Series[float] = df.iloc[:, 1]
    inp2: pd.Series[float] = df.iloc[:, 2]

    with plt.style.context("seaborn"):
        plot_running(timespan, inp0, inp1, inp2)


def plot_running(
    timespan: pd.Series[float],
    inp0: pd.Series[float],
    inp1: pd.Series[float],
    inp2: pd.Series[float],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0, label="X")
    ax0.plot(timespan, inp1, label="Y")
    ax0.plot(timespan, inp2, label="Z")
    ax0.legend()
    ax0.set_title("Running")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Acceleration, $m/s^2$")

    plt.show()


if __name__ == "__main__":
    main()
