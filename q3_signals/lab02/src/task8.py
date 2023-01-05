import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt


def main() -> None:
    sample_rate: float = 125

    inp0: npt.NDArray[np.float64] = np.loadtxt("./assets/intracranial_pressure.txt")
    timespan: npt.NDArray[np.float64] = np.arange(inp0.size) / sample_rate

    with plt.style.context("seaborn"):
        plot(timespan, inp0)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Traumatic Brain Injury")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Intracranial Pressure, $mmHg$")

    plt.show()


if __name__ == "__main__":
    main()
