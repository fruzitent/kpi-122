from math import sqrt
from typing import Callable


def rectangular_left(callback: Callable[[float], float], start: float, stop: float, nth: int) -> float:
    dx: float = (stop - start) / nth
    return sum(callback(start + idx * dx) * dx for idx in range(nth))


def rectangular_middle(callback: Callable[[float], float], start: float, stop: float, nth: int) -> float:
    dx: float = (stop - start) / nth
    return sum(callback(start + (idx + 1 / 2) * dx) * dx for idx in range(nth))


def rectangular_right(callback: Callable[[float], float], start: float, stop: float, nth: int) -> float:
    dx: float = (stop - start) / nth
    return sum(callback(start + (idx + 1) * dx) * dx for idx in range(nth))


def func(point: float) -> float:
    return 1 / (sqrt(3 * point - 1))


def main() -> None:
    start: float = 1.4
    stop: float = 2.1
    nth: int = 10

    print(rectangular_left(func, start, stop, nth))
    print(rectangular_middle(func, start, stop, nth))
    print(rectangular_right(func, start, stop, nth))


if __name__ == "__main__":
    main()
