from itertools import product


import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import typing as npt


TypeN = np.float64
ND = npt.NDArray[TypeN]

N: int = 2
EPOCH: int = 50

markers: tuple[str, ...] = "o", "x"


def distance(x: ND, centroid: ND) -> ND:
    return ((x - centroid) ** 2).sum(axis=x.ndim - 1)


def get_data(filepath: str) -> ND:
    with open(filepath, "r") as f:
        return np.array(
            [[float(num) for num in line[:-1].split(",")] for line in f.readlines()],
            dtype=TypeN,
        )


def main() -> None:
    darr_x: ND = get_data("../examples/newdata.txt")
    rand: ND = np.random.rand(N, len(darr_x))
    s: ND = [sum(arr) for arr in zip(*rand)]
    u: ND = np.divide(rand, s).transpose()
    v: ND = np.zeros([N, (len(darr_x[0]))], dtype=TypeN)
    d: ND = np.zeros([len(darr_x), N], dtype=TypeN)

    for _ in range(EPOCH):
        for itr, (jtr, _) in product(range(N), enumerate(darr_x[0])):
            t1: float = 0
            t2: float = 0
            for ktr, num in enumerate(darr_x):
                t1 += u[ktr, itr] ** 2 * num[jtr]
                t2 += u[ktr, itr] ** 2
            v[itr, jtr] = t1 / t2

        for (itr, num), jtr in product(enumerate(darr_x), range(N)):
            d[itr, jtr] = distance(num, v[jtr])

        for itr, jtr in product(range(N), range(N)):
            t3: float = sum((d[itr, jtr] ** 2) / (d[itr, ktr] ** 2) for ktr in range(N))
            u[itr, jtr] = 1 / t3

    groups: list[int] = []
    for itr, _ in enumerate(darr_x):
        for jtr in range(3):
            if u[itr, jtr] == max(u[itr]):
                groups.append(jtr)
                break

    fig = plt.figure()
    ax = fig.add_subplot(projection=Axes3D.name)
    for itr, arr in enumerate(darr_x):
        ax.scatter(arr[0], arr[1], arr[2], marker=markers[groups[itr]])

    plt.show()


if __name__ == "__main__":
    main()
