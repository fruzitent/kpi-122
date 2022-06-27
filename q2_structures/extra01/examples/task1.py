from examples.lib import (
    bsearch,
    bsearch2,
    bsearch_left,
    bsearch_right,
    bsearch_right2,
    lower_bound,
    upper_bound,
)


def part1(arr: list[int], size: int, key: int) -> str:
    idx1: int = bsearch(arr, size, key)
    idx2: int = bsearch2(arr, key)
    return f"""
    bsearch:  Search1 for {key}, found {arr[idx1]} at position {idx1}
    bsearch2: Search2 for {key}, found {arr[idx2]} at position {idx2}
    """


def part2(arr: list[int], size: int, key: int) -> str:
    jdx1: int = bsearch_left(arr, size, key)
    jdx2: int = lower_bound(arr, key)
    value2: int = arr[jdx2 - 1] if jdx2 >= len(arr) else arr[jdx2]
    return f"""
    bsearch_left: Search1 for {key}, found {arr[jdx1]} at position {jdx1}
    lower_bound:  Search2 for {key}, found {value2} at position {jdx2}
    """


def part3(arr: list[int], size: int, key: int) -> str:
    kdx1: int = bsearch_right(arr, size, key)
    kdx2: int = bsearch_right2(arr, size, key)
    kdx3: int = upper_bound(arr, key)
    value3: int = arr[kdx3 - 1] if kdx3 >= size else arr[kdx3]
    return f"""
    bsearch_right:  Search1 for {key}, found {arr[kdx1]} at position {kdx1}
    bsearch_right2: Search2 for {key}, found {arr[kdx2]} at position {kdx2}
    upper_bound:    Search3 for {key}, found {value3} at position {kdx3}
    """


def main() -> None:
    arr: list[int] = [10, 11, 11, 11, 12, 12, 15, 16, 18, 19, 110]
    size: int = len(arr)
    res1: str = part1(arr, size, 1)
    res2: str = part2(arr, size, 0)
    res3: str = part3(arr, size, 120)
    print(res1, res2, res3)


if __name__ == "__main__":
    main()
