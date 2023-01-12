from collections import deque
from itertools import product

import numpy as np
from numpy import typing as npt


def init_frame(
    input_data: npt.NDArray[np.int64],
    frame: npt.NDArray[np.int64],
) -> None:
    rows, cols = input_data.shape

    for idx in reversed(range(cols)):
        subcols: npt.NDArray[np.int64] = input_data[0, idx:]
        frame[0, idx] = np.sum(subcols)

    for jdx in range(rows):
        subrows: npt.NDArray[np.int64] = input_data[: jdx + 1, cols - 1]
        frame[jdx, cols - 1] = np.sum(subrows)


def fill_frame(
    input_data: npt.NDArray[np.int64],
    frame: npt.NDArray[np.int64],
) -> None:
    rows, cols = input_data.shape
    for idx, jdx in product(range(1, rows), reversed(range(cols - 1))):
        submatrix: npt.NDArray[np.int64] = frame[idx - 1 : idx + 1, jdx : jdx + 2]
        frame[idx, jdx] = input_data[idx, jdx] + np.max(submatrix)


def is_valid(frame: npt.NDArray[np.int64], pos: tuple[int, int]) -> bool:
    _, cols = frame.shape
    return (pos[0] >= 0) and (pos[1] < cols)


def find_route(frame: npt.NDArray[np.int64]) -> np.int64:
    route: npt.NDArray[np.int64] = np.zeros_like(frame)
    rows, cols = frame.shape

    root: tuple[int, int] = rows - 1, 0
    route[root] = frame[root]

    queue: deque[tuple[int, int]] = deque()
    queue.appendleft(root)

    while queue:
        node: tuple[int, int] = queue.pop()

        up: tuple[int, int] = node[0] - 1, node[1]
        if is_valid(frame, up):
            route[up] = max(route[up], frame[up] + route[node])
            queue.appendleft(up)

        right: tuple[int, int] = node[0], node[1] + 1
        if is_valid(frame, right):
            route[right] = max(route[right], frame[right] + route[node])
            queue.appendleft(right)

    return route[0, cols - 1]  # type: ignore


def main() -> None:
    input_data: npt.NDArray[np.int64] = np.random.randint(10, size=(5, 5))
    print(input_data)

    frame: npt.NDArray[np.int64] = np.zeros_like(input_data)
    init_frame(input_data, frame)
    fill_frame(input_data, frame)
    print(frame)

    route: np.int64 = find_route(frame)
    print(route)


if __name__ == "__main__":
    main()
