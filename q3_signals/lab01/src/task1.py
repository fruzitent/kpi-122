import numpy as np
from numpy import typing as npt


def main() -> None:
    arr0: npt.NDArray[np.float64] = np.matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
        ],
        dtype=np.float64,
    )

    arr1: npt.NDArray[np.float64] = np.matrix(
        [
            [3, 3, 3],
            [2, 2, 2],
        ],
        dtype=np.float64,
    )

    scaling(arr0)
    addition(arr0, arr1)
    subtraction(arr0, arr1)

    arr2: npt.NDArray[np.float64] = np.matrix(
        [
            [2, 2, 2],
            [1, 1, 1],
        ],
        dtype=np.float64,
    )

    arr3: npt.NDArray[np.float64] = np.matrix(
        [
            [5, 5],
            [4, 4],
            [3, 3],
        ],
        dtype=np.float64,
    )

    multiplication(arr2, arr3)


def scaling(arr0: npt.NDArray[np.float64]) -> None:
    scale: int = 3
    print(scale * arr0)


def addition(
    arr0: npt.NDArray[np.float64],
    arr1: npt.NDArray[np.float64],
) -> None:
    print(arr0 + arr1)


def subtraction(
    arr0: npt.NDArray[np.float64],
    arr1: npt.NDArray[np.float64],
) -> None:
    print(arr0 - arr1)


def multiplication(
    arr0: npt.NDArray[np.float64],
    arr1: npt.NDArray[np.float64],
) -> None:
    print(arr0 * arr1)


if __name__ == "__main__":
    main()
