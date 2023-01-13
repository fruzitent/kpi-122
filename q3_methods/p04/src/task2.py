from math import log10
from typing import Callable


def simpson(callback: Callable[[float], float], start: float, stop: float, nth: int) -> float:
    dx: float = (stop - start) / nth
    area: float = callback(start) + callback(stop)

    for idx in range(1, nth):
        point: float = start + idx * dx
        multiplier: int = 2 if idx % 2 == 0 else 4
        area += callback(point) * multiplier

    area *= dx / 3
    return area


def func(point: float) -> float:
    return log10(point**2 + 1) / point


def main() -> None:
    start: float = 0.8
    stop: float = 1.6
    nth: int = 8

    print(simpson(func, start, stop, nth))


if __name__ == "__main__":
    main()
