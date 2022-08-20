from math import cos, pi

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]


def x_function(x1: float, x2: float) -> float:
    return abs(x1) - cos(pi / 3 * x2)


def inv_char(txt: str, pos: int) -> str:
    bit: str = "0" if txt[pos] == "1" else "1"
    return txt[:pos] + bit + txt[pos + 1 :]


def roulette(values: list[float], fitness: float) -> int:
    n_rand = np.random.rand() * fitness
    sum_fit = 0
    itr = 0
    for itr, num in enumerate(values):
        sum_fit += num
        if sum_fit >= n_rand:
            break
    return itr


def main() -> None:
    mut_prob: float = 0.5
    gens: int = 20
    pop_size: int = 4
    x_max: int = 32
    x_min: int = 0
    x_size: int = len(bin(x_max)[2:])

    gen1_fvalues: list[float] = []
    gen1_xvalues: list[float] = []
    gens_f: list[float] = []
    gens_x: list[float] = []
    fitness: float = 0

    for _ in range(pop_size):
        x_tmp: float = np.random.randint(0, x_max - x_min) + x_min
        fitness = x_function(x_tmp, x_tmp)
        gen1_xvalues.append(x_tmp)
        gen1_fvalues.append(fitness)

    min_f_gen1: float = 0
    min_x_gen1: float = 0

    for i in range(pop_size):
        if gen1_fvalues[i] >= min_f_gen1:
            min_f_gen1 = gen1_fvalues[i]
            min_x_gen1 = gen1_xvalues[i]

    for _ in range(gens):
        gen2_fvalues: list[float] = []
        gen2_xvalues: list[float] = []
        selected: list[float] = []

        for _ in range(pop_size):
            ind_sel: int = roulette(gen1_fvalues, fitness)
            selected.append(gen1_xvalues[ind_sel])

        for jtr in range(0, pop_size, 2):
            mid: float = np.random.randint(1, x_size)

            sel_inda: str = bin(selected[jtr])[2:].zfill(x_size)
            sel_indb: str = bin(selected[jtr + 1])[2:].zfill(x_size)
            ind_ab: str = sel_inda[:mid] + sel_indb[mid:]
            ind_ba: str = sel_indb[:mid] + sel_inda[mid:]

            if np.random.rand() < mut_prob:
                ind_ab: str = inv_char(ind_ab, np.random.randint(0, x_size))
                ind_ba: str = inv_char(ind_ba, np.random.randint(0, x_size))

            new_AB: int = int(ind_ab, 2)
            new_BA: int = int(ind_ba, 2)
            new_f_AB: float = x_function(new_AB, new_AB)
            new_f_BA: float = x_function(new_BA, new_BA)

            gen2_xvalues.extend([new_AB, new_BA])
            gen2_fvalues.extend([new_f_AB, new_f_BA])

        min_f_gen2: float = 0
        min_x_gen2: float = 0

        for jtr in range(pop_size):
            if gen2_fvalues[jtr] >= min_f_gen2:
                min_f_gen2 = gen2_fvalues[jtr]
                min_x_gen2 = gen2_xvalues[jtr]

        if min_f_gen1 < min_f_gen2:
            min_f_gen2 = min_f_gen1
            min_x_gen2 = min_x_gen1
            gen2_fvalues[0] = min_f_gen1
            gen2_xvalues[0] = min_x_gen1

        gen1_xvalues = gen2_xvalues
        gen1_fvalues = gen2_fvalues
        min_x_gen1 = min_x_gen2
        min_f_gen1 = min_f_gen2
        gens_x.append(min_x_gen2)
        gens_f.append(min_f_gen2)

        fitness: float = 0

        for jtr in range(pop_size):
            f_tmp = x_function(gen1_xvalues[jtr], gen1_xvalues[jtr])
            fitness += f_tmp

    ax0, ax1 = plt.subplots(nrows=2)[1]
    ax0.plot(gen2_xvalues, gen2_fvalues, marker="o", linestyle="None")
    ax1.plot(range(gens), gens_f, marker="o")
    plt.show()


if __name__ == "__main__":
    main()
