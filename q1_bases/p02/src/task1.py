import math


def func(x: float, a: float) -> float:
    b: float = math.e ** a
    n: float = math.e ** (a / b)
    m: float = n - 1
    tmp: float = x / (x ** m + b ** (m - n))
    result: float = (a + b) ** n / (1 + tmp)
    return round(result.real, 10)


def main() -> None:
    res: float = func(0.81, math.log(0.083, 10))
    print(f"{res=}")


if __name__ == "__main__":
    main()
