import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import TransferFunction, dimpulse, lfilter, unit_impulse

from src.task1 import get_coefficients


def main() -> npt.NDArray[np.float64]:
    samples: int = 30

    rng: np.random.Generator = np.random.default_rng()
    denumerator, numerator = get_coefficients(rng)

    timespan: npt.NDArray[np.float64] = np.arange(samples, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = unit_impulse(samples)
    out0: npt.NDArray[np.float64] = lfilter(numerator, denumerator, inp0)

    system: TransferFunction = TransferFunction(numerator, denumerator, dt=1)
    timespan, impulse = dimpulse(system, t=timespan)
    out1: npt.NDArray[np.float64] = np.squeeze(impulse)

    with plt.style.context("seaborn"):
        plot(timespan, inp0, out0, out1)

    return out0


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
    out1: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.stem(timespan, inp0, linefmt="--b", label="Input")
    ax0.stem(timespan, out0, linefmt="--g", label="Output: Lfilter")
    ax0.stem(timespan, out1, linefmt="--r", label="Output: Dimpulse")
    ax0.legend()
    ax0.set_title("Impulse Response")
    ax0.set_xlabel("Samples, $n$")
    ax0.set_ylabel("$x[n]$, $y[n]$")

    plt.show()


if __name__ == "__main__":
    main()
