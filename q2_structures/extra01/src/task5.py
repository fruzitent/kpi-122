"""
Range search.

Given an array of nums integers, sorted in ascending order.
Find the start and end positions of the specified target value.
If the target is not found in the array, return [-1, -1].

NOTE: The complexity of the algorithm should be in the order of O (log n).

INPUT: nums = [5, 7, 7, 8, 8, 10], target = 8
OUTPUT: [3, 4]

INPUT: nums = [5, 7, 7, 8, 8, 10], target = 6
OUTPUT: [-1, -1]
"""
from examples.lib import bsearch_left, bsearch_right


def find_range(arr: list[int], key: int) -> tuple[int, int]:
    size: int = len(arr)
    lf: int = bsearch_left(arr, size, key)
    rt: int = bsearch_right(arr, size, key)
    if arr[lf] == key and arr[rt] == key:
        return lf, rt
    return -1, -1


def main() -> None:
    arr: list[int] = [5, 7, 7, 8, 8, 10]
    key1: int = 8
    key2: int = 6
    res1: tuple[int, int] = find_range(arr, key1)
    res2: tuple[int, int] = find_range(arr, key2)
    print(res1, res2)


if __name__ == "__main__":
    main()
