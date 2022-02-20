"""
Construct fuzzy set.

Let a set: /public/images/chrome_Bu0yI0f8vR.png
Make graph of this function.
"""

from matplotlib import pyplot as plt


def calc(itr: float, s1: float, s2: float, s3: float) -> float:
    if itr < s1:
        return 0
    elif itr <= s2:
        return (itr - 180) ** 2 / 200
    elif itr <= s3:
        return 1 - ((itr - 200) ** 2 / 200)
    return 1


def main() -> None:
    darr: list[float] = [179 + itr / 10 for itr in range(310)]
    line: list[float] = [calc(darr[itr], 180, 190, 200) for itr in range(len(darr))]
    plt.plot(darr, line)
    plt.show()


if __name__ == "__main__":
    main()
