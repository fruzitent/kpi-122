"""
Find the minimum in the inverted sorted array.

Suppose an array sorted in ascending order rotates.
[0,1,2,4,5,6,7] may become [4,5,6,7,0,1,2].
Find the minimum item.
You can assume that there is no duplicate in the array.

NOTE: The array was originally in ascending order.
Now that the array is rotating, there will be a point in the array
where there is a deviation from increasing sequence.
The array would be something like [4, 5, 6, 7, 0, 1, 2].

NOTE: You can divide the search space in two and see in which direction to move.
Can you think of an algorithm that has a search complexity of O (logN)?

NOTE: All elements to the left of inflection point > first element of the array.
NOTE: All elements to the right of inflection point < first element of the array.

INPUT: [3, 4, 5, 1, 2]
OUTPUT: 1

INPUT: [4, 5, 6, 7, 0, 1, 2]
OUTPUT: 0
"""


def find_min(arr: list[int]) -> int:
    if not arr:
        return -1

    lf: int = 0
    rt: int = len(arr) - 1

    while lf < rt:
        mid: int = (lf + rt) // 2

        if arr[mid] > arr[rt]:
            lf = mid + 1
        else:
            rt = mid

    return arr[lf]


def main() -> None:
    arr1: list[int] = [3, 4, 5, 1, 2]
    arr2: list[int] = [4, 5, 6, 7, 0, 1, 2]
    res1: int = find_min(arr1)
    res2: int = find_min(arr2)
    print(res1, res2)


if __name__ == "__main__":
    main()
