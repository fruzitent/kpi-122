"""
Search in inverse array.

Assume that an array sorted in ascending order rotates to some unknown value.
[0,1,2,4,5,6,7] may become [4,5,6,7,0,1,2].
You are given a search target.
If it is found in an array, you must return its index, otherwise return -1.
You can assume that there is no duplicate in the array.

NOTE: The complexity of the algorithm should be in the order of O (log n).

INPUT: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
OUTPUT: 4

INPUT: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
OUTPUT: -1
"""


def search(arr: list[int], key: int) -> int:
    lf: int = 0
    rt = len(arr) - 1

    while lf <= rt:
        mid = (lf + rt) // 2

        if arr[mid] == key:
            return mid

        if arr[lf] <= arr[mid]:
            if arr[lf] <= key < arr[mid]:
                rt = mid - 1
            else:
                lf = mid + 1
        elif arr[mid] < key <= arr[rt]:
            lf = mid + 1
        else:
            rt = mid - 1

    return -1


def main() -> None:
    arr: list[int] = [4, 5, 6, 7, 0, 1, 2]
    key1: int = 0
    key2: int = 3
    res1: int = search(arr, key1)
    res2: int = search(arr, key2)
    print(res1, res2)


if __name__ == "__main__":
    main()
