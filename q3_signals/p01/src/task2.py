import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt


def main() -> None:
    arange()
    distribution()


def arange() -> None:
    inp0: npt.NDArray[np.float64] = np.arange(2, 100, 3, dtype=np.float64)
    print("Arange:", inp0, sep="\n")


def distribution() -> None:
    inp0: npt.NDArray[np.float64] = np.random.normal(0, 100, 10000)
    inp1: npt.NDArray[np.float64] = np.random.uniform(0, 100, 10000)

    with plt.style.context("seaborn"):
        bins: int = 300
        plot_distribution(inp0, inp1, bins)


def plot_distribution(
    inp0: npt.NDArray[np.float64],
    inp1: npt.NDArray[np.float64],
    bins: int,
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 5), ncols=2, nrows=1)

    ax0.hist(inp0, bins=bins)
    ax0.set_title("Normal Distribution")
    ax0.set_xlabel("Z-score")
    ax0.set_ylabel("Frequency")

    ax1.hist(inp1, bins=bins)
    ax1.set_title("Uniform Distribution")
    ax1.set_xlabel("Values")
    ax1.set_ylabel("Frequency")

    plt.show()


if __name__ == "__main__":
    main()
