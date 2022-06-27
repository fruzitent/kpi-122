"""
Find the peak value.

A peak element is an element that is larger than its neighbors.
Given an input array nums, where nums [i] ≠ nums [i + 1].
Find the peak element and return its index.
The array can contain several peaks, in which case return index of the peaks.
You can imagine that nums [-1] = nums [n] = -∞.

NOTE: The complexity of the algorithm should be in the order of O (log n).

INPUT: nums = [1, 2, 3, 1]
OUTPUT: 2
NOTE: 3 is a peak value of array, so return 2.

INPUT: nums = [1, 2, 1, 3, 5, 6, 4]
OUTPUT: 1 or 5
NOTE: return either 1, where peak element is 2 or 5, where peak element is 6.
"""


def find_peaks(arr: list[int]) -> int:
    match len(arr):
        case 0:
            return -1
        case 1:
            return 0
        case 2:
            return 0 if arr[0] > arr[1] else 1

    lf: int = 0
    rt: int = len(arr) - 1

    while lf + 2 <= rt:
        mid: int = lf + (rt - lf) // 2

        if arr[mid - 1] > arr[mid]:
            rt = mid
        else:
            lf = mid

    return lf if arr[lf] > arr[rt] else rt


def main() -> None:
    arr1: list[int] = [1, 2, 3, 1]
    arr2: list[int] = [1, 2, 1, 3, 5, 6, 4]
    res1: int = find_peaks(arr1)
    res2: int = find_peaks(arr2)
    print(res1, res2)


if __name__ == "__main__":
    main()
