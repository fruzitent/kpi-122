from math import exp

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
from numpy import arange
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]

STEP: float = 0.2
MIN: float = 3
MAX: float = 6

EPOCH: int = 5000
NEURON_COUNT: int = 2
LR: float = 0.01


def sigmoid(x: float) -> float:
    return 1 / (1 + exp(-x))


def get_yaxis(darr_x: ND) -> ND:
    darr_y: ND = np.zeros_like(darr_x, dtype=TypeN)
    for itr, num in enumerate(darr_x):
        darr_y[itr] = 2 * exp(num) / (1 + num)
    return darr_y


def main() -> None:
    darr_x: ND = arange(MIN, MAX, STEP, dtype=TypeN)
    darr_y: ND = get_yaxis(darr_x)

    ss1: ND = np.zeros(NEURON_COUNT, dtype=TypeN)
    w10: ND = np.random.uniform(-1, 1, NEURON_COUNT)
    w20: ND = np.random.uniform(-1, 1, NEURON_COUNT)
    b10: ND = np.random.uniform(-1, 1, NEURON_COUNT)
    b20: TypeN = np.random.uniform(-1, 1)

    def compute(num: TypeN) -> tuple[ND, TypeN]:
        a1: ND = [sigmoid(w10[itr] * num + b10[itr]) for itr in range(NEURON_COUNT)]
        a2: TypeN = np.dot(w20, a1) + b20
        return a1, a2

    error_log: list[float] = []
    for _ in range(EPOCH):
        errors: float = 0

        for itr, num in enumerate(darr_x):
            a1, a2 = compute(num)

            error: TypeN = darr_y[itr] - a2
            ss2: TypeN = -2 * error

            for jtr in range(NEURON_COUNT):
                ss1[jtr] = (1 - a1[jtr]) * a1[jtr] * w20[jtr] * ss2
                w10[jtr] -= LR * ss1[jtr] * num
                w20[jtr] -= LR * ss2 * a1[jtr]
                b10[jtr] -= LR * ss1[jtr]

            b20 -= LR * ss2
            errors += error

        error_log.append(errors)

    approx_y = [compute(num)[1] for num in darr_x]

    fig = plt.figure()
    gs = GridSpec(2, 2)
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])
    ax2 = fig.add_subplot(gs[1, :])

    ax0.set_title("darr_y")
    ax0.plot(darr_x, darr_y)
    ax0.plot(darr_x, darr_y, marker="s")
    ax0.grid()

    ax1.set_title("approx_y")
    ax1.plot(darr_x, approx_y)
    ax1.plot(darr_x, approx_y, marker="s")
    ax1.grid()

    ax2.set_title("error_log")
    ax2.plot(range(EPOCH), error_log)
    ax2.grid()

    plt.tight_layout()  # type: ignore
    plt.show()

    print(f"{error_log.pop()}")
    print(f"{w10=}")
    print(f"{b10=}")
    print(f"{w20=}")
    print(f"{b20=}")


if __name__ == "__main__":
    main()
