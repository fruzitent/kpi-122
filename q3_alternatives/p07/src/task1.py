from itertools import product

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt

MEMBERS: int = 100
ITERATIONS: int = 1000


def main() -> None:
    errors: list[float] = [0, 0.02, 0.04, 0.06, 0.08, 0.1]
    probabilities: npt.NDArray[np.float64] = np.zeros(shape=(MEMBERS, len(errors)), dtype=np.float64)

    probability_by_error: list[np.float64] = []
    step_by_probability: list[np.int64] = []

    for idx, error in enumerate(errors):
        for step, _ in product(range(1, MEMBERS), range(ITERATIONS)):
            criteria: npt.NDArray[np.int64] = np.random.randint(160, 190, size=MEMBERS)
            absolute_leader: np.int64 = np.max(criteria)
            conventional_leader: np.int64 = np.max(criteria[:step])

            for jdx in criteria[step:]:
                if jdx > conventional_leader:
                    if (np.abs(jdx - absolute_leader) / absolute_leader) <= error:
                        probabilities[step, idx] += 1
                    break

        probabilities[:, idx] /= ITERATIONS
        early_stopping: np.float64 = np.max(probabilities[:, idx])
        print(f"∆{error}:", early_stopping)

        probability_by_error.append(early_stopping)
        step_by_probability.append(probabilities[:, idx].argmax())

    with plt.style.context("seaborn"):
        plot(errors, probabilities, probability_by_error, step_by_probability)


def plot(
    errors: list[float],
    probabilities: npt.NDArray[np.float64],
    probability_by_error: list[np.float64],
    step_by_probability: list[np.int64],
) -> None:
    _, (ax0, ax1, ax2) = plt.subplots(figsize=(16, 15), ncols=1, nrows=3)

    ax0.plot(np.arange(MEMBERS), probabilities)
    ax0.legend([f"∆{error}" for error in errors])
    ax0.set_title("")
    ax0.set_xlabel("Step, $t$")
    ax0.set_ylabel("Probability")

    ax1.plot(errors, probability_by_error)
    ax1.set_title("")
    ax1.set_xlabel("$∆$ Error")
    ax1.set_ylabel("Probability")

    ax2.plot(errors, step_by_probability)
    ax2.set_title("")
    ax2.set_xlabel("$∆$ Error")
    ax2.set_ylabel("Step, $t$")

    plt.show()


if __name__ == "__main__":
    main()
