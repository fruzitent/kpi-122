from itertools import product
from math import exp

import numpy as np
from matplotlib import pyplot as plt
from numpy import arange, linspace
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]

STEP: float = 0.2
MIN: float = 3
MAX: float = 6

EPOCH: int = 10**5
NEURON_COUNT: int = 2
LR: float = 0.001


def get_yaxis(darr_x: ND) -> ND:
    darr_y: ND = np.zeros_like(darr_x, dtype=TypeN)
    for itr, num in enumerate(darr_x):
        darr_y[itr] = 2 * exp(num) / (1 + num)
    return darr_y


def main() -> None:
    darr_x: ND = arange(MIN, MAX, STEP, dtype=TypeN)
    darr_y: ND = get_yaxis(darr_x)
    c: list[float] = [float(num) for num in darr_x]
    sig: ND = np.full(NEURON_COUNT, 10, dtype=TypeN)
    w: ND = np.random.uniform(-1, 1, NEURON_COUNT)
    x_size: int = len(darr_x)

    for _ in range(EPOCH):
        u: ND = np.zeros([x_size, NEURON_COUNT], dtype=TypeN)
        f: ND = np.zeros([x_size, NEURON_COUNT], dtype=TypeN)
        de_dc: ND = np.zeros(NEURON_COUNT, dtype=TypeN)
        de_dsig: ND = np.zeros(NEURON_COUNT, dtype=TypeN)
        de_dw: ND = np.zeros(NEURON_COUNT, dtype=TypeN)
        approx_y: list[float] = []

        for itr, num in enumerate(darr_x):
            error: float = 0

            for jtr in range(NEURON_COUNT):
                u[itr, jtr] += (num - c[jtr]) ** 2 / (sig[jtr] ** 2)
                f[itr, jtr] = exp(-0.5 * u[itr, jtr])
                error += w[jtr] * f[itr, jtr]

            approx_y.append(error)

        for itr in range(NEURON_COUNT):
            for jtr, x_num in enumerate(darr_x):
                tmp0: TypeN = (approx_y[jtr] - darr_y[jtr]) * exp(-0.5 * u[jtr, itr])
                tmp1: TypeN = x_num - c[itr]

                de_dc[itr] += tmp0 * w[itr] * tmp1 / sig[itr] ** 2
                de_dsig[itr] += tmp0 * w[itr] * tmp1**2 / sig[itr] ** 3
                de_dw[itr] += tmp0

            c[itr] -= LR * de_dc[itr]
            sig[itr] -= LR * de_dsig[itr]
            w[itr] -= LR * de_dw[itr]

    p2: ND = linspace(-1, 1, x_size, dtype=TypeN)
    yy: ND = np.zeros([NEURON_COUNT, x_size], dtype=TypeN)
    for itr, jtr in product(range(NEURON_COUNT), range(x_size)):
        yy[itr, jtr] = exp(-0.5 * (p2[jtr] - c[itr]) ** 2 / (sig[itr] ** 2))

    t1: ND = [(1 + exp(1 + num)) / num for num in darr_x]
    y1: ND = np.dot(np.transpose(w), yy)

    res_train: float = sum((np.dot(f, w) - darr_y) ** 2) / x_size
    res_test: float = sum((y1 - t1) ** 2) / x_size

    ax0, ax1 = plt.subplots(ncols=2)[1]
    ax2, ax3 = plt.subplots(nrows=2)[1]

    ax0.plot(darr_x, darr_y)
    ax0.plot(darr_x, darr_y, marker="o")
    ax0.grid()

    ax1.plot(darr_x, approx_y)
    ax1.plot(darr_x, approx_y, marker="s")
    ax1.grid()

    for itr in range(NEURON_COUNT):
        ax2.plot(p2, yy[itr, :])
    ax2.grid()

    ax3.plot(p2, t1, marker="*")
    ax3.plot(p2, y1, marker="o")
    ax3.grid()

    plt.tight_layout()  # type: ignore
    plt.show()

    print(f"{c=}")
    print(f"{sig=}")
    print(f"{w=}")
    print(f"{res_train=}")
    print(f"{res_test=}")


if __name__ == "__main__":
    main()
