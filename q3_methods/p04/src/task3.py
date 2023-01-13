from math import sqrt
from typing import Callable


def trapezoid(callback: Callable[[float], float], start: float, stop: float, nth: int) -> float:
    dx: float = (stop - start) / nth
    area: float = callback(start) + callback(stop)

    for idx in range(1, nth):
        point: float = start + idx * dx
        area += 2 * callback(point)

    area *= dx / 2
    return area


def func(point: float) -> float:
    return 1 / sqrt(0.2 * point**2 + 1)


def main() -> None:
    start: float = 1.3
    stop: float = 2.5
    nth: int = 20

    print(trapezoid(func, start, stop, nth))


if __name__ == "__main__":
    main()
