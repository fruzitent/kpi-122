import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from numpy import arange
from numpy import typing as npt
from skfuzzy import control as ctrl

TypeN = np.float64
ND = npt.NDArray[TypeN]

X1: float = 0.2
X2: float = 1 - X1

STEP: float = 0.2
MIN: float = 0
MAX: float = 1 + STEP


def main() -> None:
    universe: ND = arange(MIN, MAX, STEP, dtype=TypeN)

    inp0 = ctrl.Antecedent(universe, "inp0")
    inp1 = ctrl.Antecedent(universe, "inp1")
    out0 = ctrl.Consequent(universe, "out0")

    inp0.automf(names=["a10", "a11"])
    inp1.automf(names=["a20", "a21"])
    out0.automf(names=["b0", "b1"])

    rules = [
        ctrl.Rule(inp0["a10"] & inp1["a20"], out0["b0"]),
        ctrl.Rule(inp0["a10"] & inp1["a21"], out0["b0"]),
        ctrl.Rule(inp0["a11"] & inp1["a20"], out0["b1"]),
        ctrl.Rule(inp0["a11"] & inp1["a21"], out0["b1"]),
    ]

    sys = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(sys)

    sim.input[inp0.label] = X1
    sim.input[inp1.label] = X2
    sim.compute()
    print(sim.output[out0.label])


if __name__ == "__main__":
    main()
