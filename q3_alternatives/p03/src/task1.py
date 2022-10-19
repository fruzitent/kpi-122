from matplotlib import pyplot as plt

from src.data import df, weights
from src.electre import electre1
from src.plot import plot_criteria, plot_dominance


def main() -> None:
    cim, dim, adm, rank = electre1(df, weights)
    print(f"Concordance Index Matrix:   \n{cim}")
    print(f"Discordance Index Matrix:   \n{dim}")
    print(f"Aggregate Dominance Matrix: \n{adm}")
    print(f"Ranking:                    \n{rank}")

    fig: plt.Figure = plt.figure(figsize=(11.8, 8.6), dpi=300)
    ax: plt.Axes = plot_criteria(fig, df, cols=3)
    plot_dominance(ax, adm, rank, title="Aggregate Dominance Matrix")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
