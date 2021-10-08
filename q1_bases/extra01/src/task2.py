from functools import reduce


def sum_up(a: int, b: int) -> int:
    return a + b


def get_rarity(num: str) -> str:
    mid: int = len(num) // 2
    lf: list[int] = [int(x) for x in num[:mid]]
    rt: list[int] = [int(x) for x in num[mid:]]
    if reduce(sum_up, lf) == reduce(sum_up, rt):
        return "Rare"
    return "Common"


def main() -> None:
    res1: str = get_rarity("090234")
    res2: str = get_rarity("123456")
    print(f"{res1=}, {res2=}")


if __name__ == "__main__":
    main()
