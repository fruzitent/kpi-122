import numpy as np
import pandas as pd
from numpy import typing as npt
from scipy.signal import lfilter
from seaborn import objects as so

from src.common import as_db, rng, sine
from src.task1 import get_coefficients
from src.task3 import gain, periods

PLOT_SIZE: tuple[float, float] = 16, 5


def main() -> None:
    denumerator, numerator = get_coefficients()
    init: npt.NDArray[np.float64] = rng.random(np.maximum(denumerator.size, numerator.size) - 1)

    freq: int = 10
    sample_rate: int = 256
    time: int = 1

    df: pd.DataFrame = pd.DataFrame()
    df["timespan"] = np.linspace(0, time, time * sample_rate)
    df["input"] = sine(2 * np.pi * freq * df["timespan"])
    df["output_rand"] = lfilter(numerator, denumerator, df["input"], zi=init)[0]
    df["output_zero"] = lfilter(numerator, denumerator, df["input"])

    print("[output_rand] Gain, db:", as_db(gain(df["input"], df["output_rand"])))
    print("[output_zero] Gain, db:", as_db(gain(df["input"], df["output_zero"])))
    print("[output_rand] Horizontal offset, s:", periods(df["input"], df["output_rand"]) / sample_rate)
    print("[output_zero] Horizontal offset, s:", periods(df["input"], df["output_zero"]) / sample_rate)

    df = df.melt(
        id_vars=["timespan"],
        value_name="samples",
        value_vars=["input", "output_rand", "output_zero"],
        var_name="signal",
    )

    plot: so.Plot = so.Plot(data=df, x="timespan", y="samples")  # type: ignore
    plot = plot.add(so.Line(marker="o"), color="signal")

    plot = plot.label(
        title="System response",
        x="Time, s",
        y="Voltage, V",
    )

    plot = plot.layout(size=PLOT_SIZE)
    plot.show()

    plot = plot.limit(x=(0, 1 / freq))
    plot.show()


if __name__ == "__main__":
    main()
