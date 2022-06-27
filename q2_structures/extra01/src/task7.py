"""
Power function.

Implement pow(x, n)

NOTE: -100.0 < x < 100.0
NOTE: n - [-2^31, 2^31 - 1]

INPUT: 2.00000, 10
OUTPUT: 1024.00000

INPUT: 2.10000, 3
OUTPUT: 9.26100

INPUT: 2.00000, -2
OUTPUT: 0.25000
NOTE: 2^-2 = 1/2^2 = 1/4 = 0.25
"""


def power(base: float, exp: int) -> float:
    res: float = 1

    if exp == 0:
        return res

    if exp < 0:
        exp = -exp
        base = 1 / base

    while exp > 0:
        if exp % 2 == 1:
            res *= base

        base *= base
        exp //= 2

    return res


def main() -> None:
    res1: float = power(2, 10)
    res2: float = power(2.1, 3)
    res3: float = power(2, -2)
    print(res1, res2, res3)


if __name__ == "__main__":
    main()
