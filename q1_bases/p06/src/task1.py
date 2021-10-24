import math


def func(i: int, n: int) -> int:
    return sum(math.sqrt(x ** 2 + 3 * x) - x for x in range(i, n + 1))


def main() -> None:
    res: int = func(1, 7 + 10)
    print(f"{res=}")


if __name__ == "__main__":
    main()
