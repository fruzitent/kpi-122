import math


def get_values(a: float, b: float, h: float) -> list[float]:
    current_value: float = a
    result: list[float] = []
    while current_value <= b:
        current_sin_value: float = math.sin(current_value)
        result.append(current_sin_value)
        current_value += h
    return result


def main() -> None:
    res: list[float] = get_values(0, math.pi * 2, math.pi / 4)
    print(f"{res=}")


if __name__ == "__main__":
    main()
