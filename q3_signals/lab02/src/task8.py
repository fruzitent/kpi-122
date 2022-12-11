import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from src.common import Axis, Signal


def main() -> None:
    fig: Figure = plt.figure(figsize=(16, 10))  # type: ignore
    ax: plt.Axes = fig.add_subplot()  # type: ignore

    tbi: Signal = Signal(
        title="Traumatic Brain Injury",
        xaxis=Axis(
            label="Time, s",
            sample_rate=125,
        ),
        yaxis=Axis(
            label="Intracranial Pressure, mmHg",
            samples=np.loadtxt("./assets/intracranial_pressure.txt"),
        ),
    )
    tbi.plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
