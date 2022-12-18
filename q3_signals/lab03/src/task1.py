from __future__ import annotations

from time import time_ns

import numpy as np
import pandas as pd
from numpy import typing as npt
from scipy.signal import lfilter
from seaborn import objects as so

from src.common import as_db, get_lag, rms, sine

PLOT_SIZE: tuple[float, float] = 16, 5


def main() -> None:
    seed: int = time_ns() % 2**32
    np.random.seed(seed)
    print("Seed:", seed)

    # 3379786959 | max = 0.25, mean = 0.25
    # 899906383  | max = 0.60, mean = 0.25
    # 462902678  | max = 0.75, mean = 0.75
    # 4062541548 | max = 0.90, mean = 1.20
    # 3393353340 | max = 1.50, mean = 0.55
    # 4039093075 | max = 1.50, mean = 1.00

    d0: int = np.random.randint(0, 10)
    d1: int = np.random.randint(0, 10)
    m0: int = np.random.randint(0, 10)
    m1: int = np.random.randint(0, 10)
    p0: int = np.random.randint(0, 10)
    p1: int = np.random.randint(0, 10)
    p2: int = np.random.randint(0, 10)

    denumerator: npt.NDArray[np.float64] = np.array(
        [1, (d0 + d1) / 150, (p0 - d0) / 140, 0, -d1 / 130, -(m1 - d0) / 150],
        dtype=np.float64,
    )
    numerator: npt.NDArray[np.float64] = np.array(
        [m0 / 20, (p1 - d1) / 10, -(m1 - m0) / 20, -p2 / 20, d1 / 30, -m1 / 20],
        dtype=np.float64,
    )
    init: npt.NDArray[np.float64] = np.random.rand(np.maximum(denumerator.size, numerator.size) - 1)

    frequency: int = 10
    sample_rate: int = 256
    time: int = 1

    df: pd.DataFrame = pd.DataFrame()
    df["timespan"] = np.linspace(0, time, time * sample_rate)
    df["input"] = sine(2 * np.pi * frequency * df["timespan"])
    df["output_rand"] = lfilter(numerator, denumerator, df["input"], zi=init)[0]
    df["output_zero"] = lfilter(numerator, denumerator, df["input"])

    print("[output_rand] Gain, db:", as_db(rms(df["output_rand"]) / rms(df["input"])))
    print("[output_zero] Gain, db:", as_db(rms(df["output_zero"]) / rms(df["input"])))
    print("[output_rand] Horizontal offset, s:", get_lag(df["input"], df["output_rand"]) / sample_rate)
    print("[output_zero] Horizontal offset, s:", get_lag(df["input"], df["output_zero"]) / sample_rate)

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

    plot = plot.limit(x=(0, 1 / frequency))
    plot.show()


if __name__ == "__main__":
    main()
