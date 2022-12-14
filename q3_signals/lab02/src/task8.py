import numpy as np
import pandas as pd
from seaborn import objects as so

PLOT_SIZE: tuple[float, float] = 16, 5


def main() -> None:
    sample_rate: float = 125

    df: pd.DataFrame = pd.DataFrame()
    df["samples"] = np.loadtxt("./assets/intracranial_pressure.txt")
    df["timespan"] = df.index.values / sample_rate

    plot: so.Plot = so.Plot(data=df, x="timespan", y="samples")  # type: ignore
    plot = plot.add(so.Line())

    plot = plot.label(
        title="Traumatic Brain Injury",
        x="Time, s",
        y="Intracranial Pressure, mmHg",
    )

    plot = plot.layout(size=PLOT_SIZE)
    plot.show()


if __name__ == "__main__":
    main()
