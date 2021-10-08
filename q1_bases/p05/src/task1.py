import math


def get_values(x0: float, xk: float, dk: float) -> list[list[float, float]]:
    result: list[list[float]] = []
    b: float = 2.5
    while x0 < xk:
        y0: float = x0 + 15 * math.sqrt(x0 ** 3 + b ** 3)
        x: float = round(x0, 4)
        y: float = round(9 * y0, 4)
        result.append([x, y])
        x0 += dk
    return result


def main() -> None:
    res: list[list[float]] = get_values(-2.4, 1, 0.2)
    print(f"{res=}")


if __name__ == "__main__":
    main()
