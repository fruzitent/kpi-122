import math


def calculate(*args: int) -> int:
    return sum(math.ceil(x / 2) for x in args)


def main() -> None:
    res1: int = calculate(20, 21, 22)
    res2: int = calculate(25, 27, 26)
    print(f"{res1=}, {res2=}")


if __name__ == "__main__":
    main()
