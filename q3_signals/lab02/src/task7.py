import pandas as pd
from seaborn import objects as so

PLOT_SIZE: tuple[float, float] = 16, 10


def main() -> None:
    window: int = 30

    df: pd.DataFrame = pd.read_csv("./assets/Subject7_SpO2Hr.csv")
    df.drop(columns=["Unnamed: 0"], inplace=True)
    df.columns = pd.Index(["timespan", "spo2_original", "hr_original"])
    df["spo2_rolling"] = df["spo2_original"].rolling(window).mean()
    df["hr_rolling"] = df["hr_original"].rolling(window).mean()

    df = pd.concat(
        objs=[
            df.melt(
                id_vars=["timespan"],
                value_name="spo2",
                value_vars=["spo2_original", "spo2_rolling"],
                var_name="signal",
            ),
            df.melt(
                id_vars=["timespan"],
                value_name="hr",
                value_vars=["hr_original", "hr_rolling"],
                var_name="signal",
            ),
        ],
        ignore_index=True,
    )

    df["signal"] = df["signal"].str.replace("spo2_", "")
    df["signal"] = df["signal"].str.replace("hr_", "")

    plot: so.Plot = so.Plot(data=df, x="timespan")  # type: ignore
    plot = plot.pair(y=["spo2", "hr"])
    plot = plot.add(so.Line(), color="signal")

    plot = plot.label(
        title="Arterial blood saturation with oxygen and Heart Rate",
        x="Time, s",
        y0="SpO2, %",
        y1="Rate, bpm",
    )

    plot = plot.layout(size=PLOT_SIZE)
    plot.show()


if __name__ == "__main__":
    main()
