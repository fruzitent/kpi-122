"""
Find the k the nearest elements.

Given a sorted array, two integers k and x, find k closest to x.
The result should also be sorted in ascending order.
Always prefer smaller items.

NOTE: The value of k is positive and will always be
less than the length of the sorted array.

NOTE: The length of this array is positive and
does not exceed 10 in the fourth.

NOTE: The absolute value of the elements of the array and
x will not exceed 10 in the fourth.

INPUT: [1, 2, 3, 4, 5], k = 4, x = 3
OUTPUT: [1, 2, 3, 4]

INPUT: [1, 2, 3, 4, 5], k = 4, x = -1
OUTPUT: [1, 2, 3, 4]
"""


def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    lf: int = 0
    rt: int = len(arr) - k

    while lf < rt:
        mid = (lf + rt) // 2

        if x - arr[mid] <= arr[mid + k] - x:
            rt = mid
        else:
            lf = mid + 1

    return arr[lf : lf + k]


def main() -> None:
    arr: list[int] = [1, 2, 3, 4, 5]
    k: int = 4
    x1: int = 3
    x2: int = -1
    res1: list[int] = find_closest_elements(arr, k, x1)
    res2: list[int] = find_closest_elements(arr, k, x2)
    print(res1, res2)


if __name__ == "__main__":
    main()
