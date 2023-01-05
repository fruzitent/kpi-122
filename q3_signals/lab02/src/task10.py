import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.io import loadmat


def main() -> None:
    sample_rate: float = 151.51

    mat = loadmat("./assets/BOK_with_separate_trials.mat")["h"][0][0]
    tags: list[str] = [tag[0][0] for tag in mat[1] if tag[0][0] != "none"]
    samples: npt.NDArray[np.float64] = mat[2]

    for idx, tag in enumerate(tags):
        inp0: npt.NDArray[np.float64] = samples[idx]
        timespan: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

        with plt.style.context("seaborn"):
            plot(timespan, inp0, tag)

        stats(timespan, tag)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    tag: str,
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title(tag)
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("")

    plt.show()


def stats(
    timespan: npt.NDArray[np.float64],
    tag: str,
) -> None:
    back: np.float64 = timespan[-1]
    print(f"Recording [{tag}] is {back} seconds long")


if __name__ == "__main__":
    main()
