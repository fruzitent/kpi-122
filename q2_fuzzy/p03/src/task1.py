from math import exp

import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from numpy import arange, polyfit, polyval
from numpy import typing as npt
from skfuzzy import control as ctrl

TypeN = np.float64
ND = npt.NDArray[TypeN]

STEP: float = 0.25
MIN: float = 3
MAX: float = 6 + STEP

RESOLUTION: int = 1000


def get_yaxis(darr_x: ND) -> ND:
    darr_y: ND = np.zeros_like(darr_x)
    for itr, _ in enumerate(darr_x):
        a: float = 2 * exp(darr_x[itr])
        b: float = 1 + darr_x[itr]
        darr_y[itr] = a / b
    return darr_y


def main() -> None:
    darr_x: ND = arange(MIN, MAX, STEP, dtype=np.float64)
    darr_y: ND = get_yaxis(darr_x)

    inp = ctrl.Antecedent(darr_x, "inp")
    out = ctrl.Consequent(darr_y, "out")

    x_names: list[str] = [f"x{itr}" for itr, _ in enumerate(inp.universe)]
    inp.automf(names=x_names)

    y_names: list[str] = [f"y{itr}" for itr, _ in enumerate(out.universe)]
    abcs: list[list[int]] = [[0, num, num] for num in out.universe]
    for name, abc in zip(y_names, abcs):
        out[name] = fuzz.trimf(out.universe, abc)

    rules = [
        (ctrl.Rule(inp[x_name], out[y_name]))
        for x_name, y_name in zip(x_names, y_names)
    ]

    sys = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(sys)

    # TODO: skfuzzy does not support sugeno yet

    y_axis: ND = np.zeros_like(darr_y)
    error: float = 0

    for itr, num in enumerate(darr_x):
        sim.input[inp.label] = num
        sim.compute()
        y_axis[itr] = sim.output[out.label]
        error += abs(y_axis[itr] - darr_y[itr])

    pol = polyfit(darr_x, y_axis, 4)
    opt_y: ND = polyval(pol, darr_x)

    plt.plot(darr_x, darr_y)
    plt.plot(darr_x, opt_y)
    plt.show()

    print(f"{error=}")


if __name__ == "__main__":
    main()
