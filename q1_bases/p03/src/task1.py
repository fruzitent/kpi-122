def calculate(b: float) -> float:
    a: int = 1000
    lf: float = (a - b) ** 3 - a ** 3
    rt: float = b ** 3 - 3 * a * b ** 2 - 3 * a ** 2 * b
    return lf / rt


def main() -> None:
    res1: float = calculate(10 ** -12)
    res2: float = calculate(10 ** -14)
    res3: float = calculate(10 ** -16)
    print(f"{res1=}, {res2=}, {res3=}")


if __name__ == "__main__":
    main()
