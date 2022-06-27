"""
SQRT. Implement int sqrt (int x).

Calculate and return the square root of x,
where x is a guaranteed non-negative integer.
Because the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

NOTE: Try to consider all integers.
NOTE: Use the sorted property of integers to reduce search space.

INPUT: 4
OUTPUT: 2

INPUT: 8
OUTPUT: 2
NOTE: sqrt(8) = 2.82842
"""


def isqrt(num: int) -> int:
    if num < 0:
        raise ValueError("math domain error")

    if num < 2:
        return num

    lf: int = 1
    rt: int = num // 2
    res: int = 0

    while lf <= rt:
        mid: int = (lf + rt) // 2
        sqr: int = mid**2

        if sqr == num:
            return mid

        if sqr < num:
            lf = mid + 1
            res = mid
        else:
            rt = mid - 1

    return res


def main() -> None:
    res1: int = isqrt(4)
    res2: int = isqrt(8)
    print(res1, res2)


if __name__ == "__main__":
    main()
