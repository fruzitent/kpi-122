def calculate(x: int) -> float:
    a: int = 1
    b: int = 2
    c: int = 3
    lf: float = (a + b) ** c
    rt: float = x ** c + b ** c
    return lf / (1 + x / rt)


def main() -> None:
    res1: float = calculate(-10)
    res2: float = calculate(0)
    res3: float = calculate(25)
    print(f"{res1=}, {res2=}, {res3=}")


if __name__ == "__main__":
    main()
