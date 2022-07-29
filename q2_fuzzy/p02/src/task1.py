from itertools import product

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, linspace, meshgrid
from numpy import typing as npt
from skfuzzy import control as ctrl

TypeN = np.float64
ND = npt.NDArray[TypeN]

STEP: float = 0.1
MIN: float = 0
MAX: float = 1 + STEP

X0: float = 0.2
X1: float = 1 - X0


def main() -> None:
    universe: ND = arange(MIN, MAX, STEP, dtype=TypeN)

    inp0 = ctrl.Antecedent(universe, "inp0")
    inp1 = ctrl.Antecedent(universe, "inp1")
    out0 = ctrl.Consequent(universe, "out0")

    inp0.automf(names=["inp0_lvl_low", "inp0_lvl_hgh"])
    inp1.automf(names=["inp1_lvl_low", "inp1_lvl_hgh"])
    out0.automf(names=["out0_lvl_low", "out0_lvl_hgh"])

    inp0.view()
    inp1.view()
    out0.view()

    rules = [
        ctrl.Rule(inp0["inp0_lvl_low"] & inp1["inp1_lvl_low"], out0["out0_lvl_hgh"]),
        ctrl.Rule(inp0["inp0_lvl_low"] & inp1["inp1_lvl_hgh"], out0["out0_lvl_low"]),
        ctrl.Rule(inp0["inp0_lvl_hgh"] & inp1["inp1_lvl_low"], out0["out0_lvl_low"]),
        ctrl.Rule(inp0["inp0_lvl_hgh"] & inp1["inp1_lvl_hgh"], out0["out0_lvl_hgh"]),
    ]

    sys = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(sys)

    sim.input[inp0.label] = X0
    sim.input[inp1.label] = X1
    sim.compute()
    print(sim.output[out0.label])

    resolution: int = len(universe) - 1
    unsampled = linspace(MIN, MAX, resolution, dtype=TypeN)
    x_axis, y_axis = meshgrid(unsampled, unsampled)
    z_axis: ND = np.zeros_like(x_axis)

    for itr, jtr in product(range(resolution), range(resolution)):
        sim.input[inp0.label] = x_axis[itr, jtr]
        sim.input[inp1.label] = y_axis[itr, jtr]
        sim.compute()
        z_axis[itr, jtr] = sim.output[out0.label]

    fig = plt.figure()
    ax = fig.add_subplot(projection=Axes3D.name)
    ax.plot_surface(x_axis, y_axis, z_axis)  # type: ignore

    ax.set_xlabel(inp0.label)
    ax.set_ylabel(inp1.label)
    ax.set_zlabel(out0.label)  # type: ignore

    plt.show()


if __name__ == "__main__":
    main()
