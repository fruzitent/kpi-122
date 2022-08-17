from itertools import product
from math import pi, sin

import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, linspace, meshgrid
from numpy import typing as npt
from skfuzzy import control as ctrl
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

TypeN = np.float64
ND = npt.NDArray[TypeN]


MIN: float = 1
MAX: float = 4

TERMS_A: int = 5
TERMS_B: int = 4
TERMS: int = TERMS_A * TERMS_B

RESOLUTION: int = 100


def func(a: float, b: float) -> float:
    return b * sin(a * pi / 6) ** 2


def get_range(start: float, end: float, step: int) -> ND:
    delta: float = (end - start) / (step - 1)
    return arange(start, end + delta, delta, dtype=TypeN)


def get_yaxis(darr_a: ND, darr_b: ND) -> tuple[ND, ND]:
    darr_y: ND = np.zeros(TERMS, dtype=TypeN)
    for idx, (num_a, num_b) in enumerate(product(darr_a, darr_b)):
        darr_y[idx] = func(num_a, num_b)
    return darr_y, np.sort(darr_y)


def main() -> None:
    darr_a: ND = get_range(MIN, MAX, TERMS_A)
    darr_b: ND = get_range(MIN, MAX, TERMS_B)
    darr_y, darr_y_sorted = get_yaxis(darr_a, darr_b)

    inp_a = ctrl.Antecedent(darr_a, "inp_a")
    inp_b = ctrl.Antecedent(darr_b, "inp_b")
    out_y = ctrl.Consequent(darr_y, "out_y")

    inp_a.automf(names=[f"a{itr}" for itr, _ in enumerate(inp_a.universe)])
    inp_b.automf(names=[f"b{itr}" for itr, _ in enumerate(inp_b.universe)])
    for itr, _ in enumerate(out_y.universe):
        abc: list[float] = [0, darr_y_sorted[itr], darr_y_sorted[itr]]
        out_y[f"y{itr}"] = fuzz.trimf(out_y.universe, abc)

    rules = []
    for idx, (itr, jtr) in enumerate(product(range(TERMS_A), range(TERMS_B))):
        rule = ctrl.Rule()
        rule.antecedent = inp_a[f"a{itr}"] & inp_b[f"b{jtr}"]
        for ktr in range(TERMS):
            if darr_y[idx] == darr_y_sorted[ktr]:
                rule.consequent = out_y[f"y{ktr}"]
                break
        rules.append(rule)

    sys = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(sys)

    unsampled: ND = linspace(MIN, MAX, RESOLUTION, dtype=TypeN)
    x_set, y_set = meshgrid(unsampled, unsampled)
    z_set: ND = np.zeros_like(x_set)

    ep: float = 0
    for itr, jtr in product(range(RESOLUTION), range(RESOLUTION)):
        sim.input[inp_a.label] = x_set[itr, jtr]
        sim.input[inp_b.label] = y_set[itr, jtr]
        sim.compute()
        z_set[itr, jtr] = sim.output[out_y.label]
        ep += z_set[itr, jtr] / RESOLUTION

    # TODO: make sure that anfis is correct

    x_train, x_test, y_train, y_test = train_test_split(x_set, y_set, random_state=1)

    sc = StandardScaler()
    sc.fit(x_train)
    x_train_scaled: list[list[float]] = sc.transform(x_train)
    x_test_scaled: list[list[float]] = sc.transform(x_test)

    mlp = MLPRegressor(max_iter=1000, random_state=1, verbose=True)
    mlp.fit(x_train_scaled, y_train)
    y_pred: list[list[float]] = mlp.predict(x_test_scaled)

    score: float = mlp.score(x_test, y_test)
    mae: float = mean_absolute_error(y_test, y_pred)
    mse: float = mean_squared_error(y_test, y_pred)
    rmse: float = np.sqrt(mse)

    fig = plt.figure()
    ax = fig.add_subplot(projection=Axes3D.name)
    ax.plot_surface(x_set, y_set, z_set, cmap="coolwarm")  # type: ignore
    ax.set_xlabel("x_set")
    ax.set_ylabel("y_set")
    ax.set_zlabel("z_set")  # type: ignore
    plt.show()

    print(f"{ep=}")
    print(f"{mae=}")
    print(f"{mse=}")
    print(f"{rmse=}")
    print(f"{score=}")


if __name__ == "__main__":
    main()
