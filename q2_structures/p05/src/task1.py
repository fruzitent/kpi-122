from typing import Sequence


def linear_search(num: float, arr: Sequence[float]) -> int:
    itr = (index for index, elem in enumerate(arr) if num == elem)
    return next(itr, -1)


def binary_search(num: float, arr: Sequence[float]) -> int:
    lf: int = 0
    rt: int = len(arr) - 1
    while lf <= rt:
        mid = (lf + rt) // 2
        if arr[mid] < num:
            lf = mid + 1
        elif arr[mid] > num:
            rt = mid - 1
        else:
            return mid
    return -1


def get_result(res: int) -> str:
    return "yes" if ~res else "no"


def main() -> None:
    arr1: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2: list[int] = [-2, 0, 4, 9, 12]

    for num in arr2:
        res1: str = get_result(linear_search(num, arr1))
        res2: str = get_result(binary_search(num, arr1))
        print(f"{num} | {res1}, {res2}")


if __name__ == "__main__":
    main()
