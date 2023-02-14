import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt


def main() -> None:
    inp0: npt.NDArray[np.float64] = np.arange(-10, 10, 0.01, dtype=np.float64)
    out0: npt.NDArray[np.float64] = 2 * inp0 / 5 + 2

    with plt.style.context("seaborn"):
        plot(inp0, out0)


def plot(
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(inp0, out0)
    ax0.axhline(0, alpha=0.25, color="black", linestyle="dashed", zorder=0)
    ax0.axvline(0, alpha=0.25, color="black", linestyle="dashed", zorder=0)
    ax0.set_title("Linear Function")
    ax0.set_xlabel("x")
    ax0.set_ylabel("y")

    plt.show()


if __name__ == "__main__":
    main()
