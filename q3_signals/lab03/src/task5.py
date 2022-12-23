import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import lfilter, unit_impulse

from src.task1 import get_coefficients


def main() -> None:
    samples: int = 30

    rng: np.random.Generator = np.random.default_rng()
    denumerator, numerator = get_coefficients(rng)

    inp0: npt.NDArray[np.float64] = unit_impulse(samples)
    out0: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp0)

    with plt.style.context("seaborn"):
        _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

        ax0.stem(inp0, label="x[n]", linefmt="--b")
        ax0.stem(out0, label="y[n]", linefmt="--g")
        ax0.legend()
        ax0.set_title("Impulse Response")
        ax0.set_xlabel("Samples, n")
        ax0.set_ylabel("")

        plt.show()


if __name__ == "__main__":
    main()
