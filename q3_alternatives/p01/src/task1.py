import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]

REDUCE_TO: int = 2000
SHOW_PLOTS: bool = True


def variation(x: ND) -> ND:
    return np.std(x, ddof=1) / np.mean(x) * 100


def main() -> None:
    df: pd.DataFrame = pd.read_excel("../assets/DATA_КП_1.xls", sheet_name="Лист1")
    df = df.iloc[:REDUCE_TO]  # given data is corrupt, reduce sample size to first n entries

    cv: pd.Series = df.apply(variation).apply(abs)
    if SHOW_PLOTS:
        cv.plot.bar(title="coefficient of variation")
        plt.show()

    signal: pd.Series = df[cv.idxmin()]
    if SHOW_PLOTS:
        df.plot.line(title=f"the most stable signal is: {signal.name}")
        plt.show()


if __name__ == "__main__":
    main()
