def calculate(a: int, x: int) -> float:
    if x > a:
        return (abs(x ** 2 - a)) ** (1 / 3) + x ** 2
    if x < a:
        return (a - x ** 2) ** 3 + x ** 2
    return (a + x ** 2) ** 2 + x ** 3


def main() -> None:
    res1: float = calculate(1, 42)
    res2: float = calculate(42, 1)
    res3: float = calculate(42, 42)
    print(f"{res1=}, {res2=}, {res3=}")


if __name__ == "__main__":
    main()
