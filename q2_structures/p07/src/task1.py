def sort_and_count_inv(res: list[int]) -> tuple[list[int], int]:
    if len(res) != 1:
        mid: int = len(res) // 2
        lf, num1 = sort_and_count_inv(res[:mid])
        rt, num2 = sort_and_count_inv(res[mid:])
        res, num3 = merge_and_count_split_inv(lf, rt)
        return res, num1 + num2 + num3
    return res, 0


def merge_and_count_split_inv(
    lf: list[int],
    rt: list[int],
) -> tuple[list[int], int]:
    res: list[int] = []
    inv_count: int = 0
    itr: int = 0
    jtr: int = 0

    while itr < len(lf) and jtr < len(rt):
        if lf[itr] < rt[jtr]:
            res.append(lf[itr])
            itr += 1
        else:
            res.append(rt[jtr])
            inv_count += len(lf) - itr
            jtr += 1

    res.extend(lf[itr:])
    res.extend(rt[jtr:])
    return res, inv_count


def main() -> None:
    arr1: list[int] = [1, 2, 3, 6, 8]  # 00
    arr2: list[int] = [2, 3, 8, 6, 1]  # 05
    arr3: list[int] = [8, 6, 3, 2, 1]  # 10
    print(sort_and_count_inv(arr1))
    print(sort_and_count_inv(arr2))
    print(sort_and_count_inv(arr3))


if __name__ == "__main__":
    main()
