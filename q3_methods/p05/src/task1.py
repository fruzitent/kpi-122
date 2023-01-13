from typing import Callable


def derivative(callback: Callable[[float], float], point: float, error: float) -> float:
    return (callback(point + error) - callback(point - error)) / (2 * error)


def bisect(callback: Callable[[float], float], start: float, stop: float, error: float) -> float:
    while True:
        middle: float = (start + stop) / 2

        if callback(start) * callback(middle) < 0:
            stop = middle
        else:
            start = middle

        if abs(callback(middle)) < error:
            break

    return middle


def newton(callback: Callable[[float], float], point: float, error: float) -> float:
    if abs(callback(point)) < error:
        return point
    approximation: float = point - callback(point) / derivative(callback, point, error)
    return newton(callback, approximation, error)


def func(point: float) -> float:
    return point**4 + 2 * point**3 + 2 * point**2 + 6 * point - 5


def main() -> None:
    error: float = 0.0001
    print(newton(func, -3, error))
    print(bisect(func, -1.5, 1, error))


if __name__ == "__main__":
    main()
