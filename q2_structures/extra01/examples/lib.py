def bsearch(arr: list[int], size: int, key: int) -> int:
    """Standard binary search.

    Args:
        arr: input sorted array.
        size: size of array "arr".
        key: value to search in array "arr".

    Returns:
        index of element "key" in array "arr" or -1 if not exist.
    """
    left: int = 0
    right: int = size - 1
    while left <= right:
        middle: int = left + (right - left) // 2
        if arr[middle] < key:
            left = middle + 1
        elif key < arr[middle]:
            right = middle - 1
        else:
            return middle
    return -1


def _bsearch2_or_upper_bound(
    arr: list[int],
    key: int,
) -> tuple[int, int, int, list[int]]:
    left: int = -1
    right: int = len(arr)
    while left + 1 < right:
        middle: int = (left + right) // 2
        if key < arr[middle]:
            right = middle
        else:
            left = middle
    return left, right, key, arr


def bsearch2(arr: list[int], key: int) -> int:
    left, _, key, arr = _bsearch2_or_upper_bound(arr, key)
    return left if left >= 0 and arr[left] == key else -1


def bsearch_left(arr: list[int], size: int, key: int) -> int:
    """Leftmost boundary binary search.

    0 1 1 1 2 2 5 6 8 9 10, search for  1 gives index  1.
    0 1 1 1 2 2 5 6 8 9 10, search for -1 gives index  0.
    0 1 1 1 2 2 5 6 8 9 10, search for  0 gives index  0.
    0 1 1 1 2 2 5 6 8 9 10, search for 10 gives index 10.
    0 1 1 1 2 2 5 6 8 9 10, search for 11 or 13 or other gives index 11 (size + 1).
    10 11 11 11 12 12 15 16 18 19 110, search for 9 gives index 0.

    Args:
        arr:  input sorted array.
        size: size of array "arr".
        key:  value to search in array "arr".

    Returns:
        index of the left most element "key" in array "arr" or 0 if not exist.
    """
    left: int = 0
    right: int = size
    while left < right:
        middle: int = left + (right - left) // 2
        if arr[middle] < key:
            left = middle + 1
        else:
            right = middle
    return left


def bsearch_right(arr: list[int], size: int, key: int) -> int:
    """Rightmost boundary binary search.

    0 1 1 1 2 2 5 6 8 9 10, search for  1 gives index  3.
    0 1 1 1 2 2 5 6 8 9 10, search for -1 gives index -1.
    0 1 1 1 2 2 5 6 8 9 10, search for  0 gives index  0.
    0 1 1 1 2 2 5 6 8 9 10, search for 11 gives index 11,
    (index of last element right never changed).
    0 1 1 1 2 2 5 6 8 9 10, search for 10 gives index 11,
    (index of last element right never changed) Should be checked.
    10 11 11 11 12 12 15 16 18 19 110, search for 9 gives index -1.

    Args:
        arr:  input sorted array.
        size: size of array "arr".
        key:  value to search in array "arr".

    Returns:
        index of the left most element "key" in array "arr" or 0 if not exist
        (should check 0 probably our element first)
    """
    left: int = 0
    right: int = size
    while left < right:
        middle: int = left + (right - left) // 2
        if arr[middle] <= key:
            left = middle + 1
        else:
            right = middle
    return left - 1


def bsearch_right2(arr: list[int], size: int, key: int) -> int:
    """Rightmost boundary binary search.

    0 1 1 1 2 2 5 6 8 9 10, search for  1 gives index  3.
    0 1 1 1 2 2 5 6 8 9 10, search for -1 gives index -1.
    0 1 1 1 2 2 5 6 8 9 10, search for  0 gives index  0.
    0 1 1 1 2 2 5 6 8 9 10, search for 11 gives index 11,
    (index of last element right never changed).
    0 1 1 1 2 2 5 6 8 9 10, search for 10 gives index 11,
    (index of last element right never changed) Should be checked.
    10 11 11 11 12 12 15 16 18 19 110, search for 9 gives index -1.

    Args:
        arr: input sorted array.
        size: size of array "arr".
        key: value to search in array "arr".

    Returns:
        index of the left most element "key" in array "arr" or 0 if not exist
        (should check 0 probably our element first)
    """
    left: int = 0
    right: int = size
    while left < right:
        middle: int = left + (right - left) // 2
        if 0 <= arr[middle] <= key:
            left = middle + 1
        else:
            right = middle
    return left - 1


def lower_bound(arr: list[int], key: int) -> int:
    left: int = -1
    right: int = len(arr)
    while left + 1 < right:
        middle: int = (left + right) // 2
        if key <= arr[middle]:
            right = middle
        else:
            left = middle
    return right


def upper_bound(arr: list[int], key: int) -> int:
    _, right, _, _ = _bsearch2_or_upper_bound(arr, key)
    return right - 1
