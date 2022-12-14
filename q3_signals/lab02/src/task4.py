import numpy as np
import pandas as pd
from seaborn import objects as so

PLOT_SIZE: tuple[float, float] = 16, 5


def ecg_healthy() -> None:
    with np.load("./assets/ecg_healthy_7.npz") as npz:
        df: pd.DataFrame = pd.DataFrame()
        df["samples"] = npz["signal"]
        df["timespan"] = df.index.values / npz["fs"]
        df["peaks"] = dict(zip(npz["labels_indexes"], npz["labels"]))

        plot: so.Plot = so.Plot(data=df, x="timespan", y="samples")  # type: ignore
        plot = plot.add(so.Line({"zorder": 1}))
        plot = plot.add(so.Dot(color="red"), color="peaks", legend=None)
        plot = plot.add(so.Text(halign="left"), text="peaks")

        plot = plot.label(
            title="Electrocardiogram [Healthy]",
            x="Time, s",
            y=f"Voltage {npz['units']}",
        )

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

        plot = plot.layout(size=PLOT_SIZE)
        plot.show()


def main() -> None:
    ecg_healthy()
    ecg_anomaly()


if __name__ == "__main__":
    main()
