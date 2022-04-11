from functools import cache


@cache  # type: ignore
def sum_func(num: int) -> float:
    sigma: float = (num + 1) / (2 * num + 5)
    return sigma if num == 1 else sigma + sum_func(num - 1)


def main() -> None:
    num: int = 10
    res: float = sum_func(num)
    print(f"{res=}")


if __name__ == "__main__":
    main()
