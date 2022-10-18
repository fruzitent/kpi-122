from time import time_ns

from _testcapi import INT_MAX
from matplotlib import pyplot as plt

from src.data import df, weights
from src.electre import electre1, plot_dominance, plot_bin_relp


def main() -> None:
    cim, dim, adm, rank = electre1(df, weights)

    print(f"Concordance Index Matrix:   \n{cim}")
    print(f"Discordance Index Matrix:   \n{dim}")
    print(f"Aggregate Dominance Matrix: \n{adm}")
    print(f"Ranking:                    \n{rank}")

    fig: plt.Figure = plt.figure(dpi=300)
    ax: plt.Axes = fig.add_subplot(1, 1, 1)
    plot_dominance(ax, adm, rank, title="Aggregate Dominance Matrix")
    plt.show()


def main2() -> None:
    import numpy as np
    import pandas as pd

    x = time_ns() % INT_MAX
    print(x)

    np.random.seed(x)

    df: pd.DataFrame = pd.DataFrame(
        columns=[
            "Algorithms and Programming",
            "Alternative Approaches",
            "Calculation Methods",
            "Operation Systems",
            "Signal Theory",
        ],
        index=[
            "Student A",
            "Student B",
            "Student C",
            "Student D",
            "Student E",
        ],
        data=np.random.randint(60, 100, (5, 5)),
        dtype=np.int8,
    )

    weights: list[float] = np.random.random(df.columns.size)
    cim, dim, adm, rank = electre1(df, weights)

    fig: plt.Figure = plt.figure(figsize=(11.8, 8.6), dpi=300)
    plot_bin_relp(fig, df, cols=3)
    plot_dominance(plt.gca(), adm, rank, title="Aggregate Dominance Matrix")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main2()
