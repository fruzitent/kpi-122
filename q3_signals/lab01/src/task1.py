import numpy as np
from numpy import typing as npt


def main() -> None:
    inp0: npt.NDArray[np.float64] = np.matrix(
        data=[
            [1, 2, 3],
            [4, 5, 6],
        ],
        dtype=np.float64,
    )

    inp1: npt.NDArray[np.float64] = np.matrix(
        data=[
            [3, 3, 3],
            [2, 2, 2],
        ],
        dtype=np.float64,
    )

    inp2: npt.NDArray[np.float64] = np.matrix(
        data=[
            [2, 2, 2],
            [1, 1, 1],
        ],
        dtype=np.float64,
    )

    inp3: npt.NDArray[np.float64] = np.matrix(
        data=[
            [5, 5],
            [4, 4],
            [3, 3],
        ],
        dtype=np.float64,
    )

    scaling(inp0)
    addition(inp0, inp1)
    subtraction(inp0, inp1)
    multiplication(inp2, inp3)


def scaling(inp0: npt.NDArray[np.float64]) -> None:
    scale: int = 3
    print("Scaling:", scale * inp0, sep="\n")


def addition(
    inp0: npt.NDArray[np.float64],
    inp1: npt.NDArray[np.float64],
) -> None:
    print("Addition:", inp0 + inp1, sep="\n")


def subtraction(
    inp0: npt.NDArray[np.float64],
    inp1: npt.NDArray[np.float64],
) -> None:
    print("Subtraction:", inp0 - inp1, sep="\n")


def multiplication(
    inp0: npt.NDArray[np.float64],
    inp1: npt.NDArray[np.float64],
) -> None:
    print("Multiplication:", inp0 * inp1, sep="\n")


if __name__ == "__main__":
    main()
