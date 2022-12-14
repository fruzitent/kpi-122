import numpy as np
import pandas as pd
from scipy.io import loadmat
from seaborn import objects as so

PLOT_SIZE: tuple[float, float] = 16, 5


def hr_apnea() -> None:
    sample_rate: float = 100

    df: pd.DataFrame = pd.DataFrame()
    df["samples"] = loadmat("./assets/hr_apnea_7.mat")["hr_ap"].squeeze()
    df["timespan"] = df.index.values / sample_rate

    plot: so.Plot = so.Plot(data=df, x="timespan", y="samples")  # type: ignore
    plot = plot.add(so.Line())

    plot = plot.label(
        title="Heart Rate [Apnea]",
        x="Time, s",
        y="Time, ms",
    )

    plot = plot.limit(x=(20, 23))
    plot = plot.layout(size=PLOT_SIZE)
    plot.show()


def ecg_anomaly() -> None:
    with np.load("./assets/ecg_anomaly_7.npz") as npz:
        df: pd.DataFrame = pd.DataFrame()
        df["samples"] = npz["signal"]
        df["timespan"] = df.index.values / npz["fs"]
        df["peaks"] = dict(zip(npz["labels_indexes"], npz["labels"]))

        plot: so.Plot = so.Plot(data=df, x="timespan", y="samples")  # type: ignore
        plot = plot.add(so.Line({"zorder": 1}))
        plot = plot.add(so.Dot(color="red"), color="peaks", legend=None)
        plot = plot.add(so.Text(halign="left"), text="peaks")

        plot = plot.label(
            title="Electrocardiogram [Anomaly]",
            x="Time, s",
            y=f"Voltage {npz['units']}",
        )

        plot = plot.limit(x=(0, 5))
        plot = plot.layout(size=PLOT_SIZE)
        plot.show()


def main() -> None:
    hr_apnea()
    ecg_anomaly()


if __name__ == "__main__":
    main()
