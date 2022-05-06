def zfill(num: int, amount: int, *, is_left: bool) -> str:
    string: str = str(num)
    for _ in range(amount):
        string = f"0{string}" if is_left else f"{string}0"
    return string


def split_in_half(string: str) -> tuple[str, str]:
    mid: int = len(string) // 2
    return string[:mid], string[mid:]


def karatsuba(num1: int, num2: int) -> int:
    if num1 < 10 and num2 < 10:
        return num1 * num2

    str1, str2 = str(num1), str(num2)
    dif1: int = len(str1) - len(str2)
    if len(str1) < len(str2):
        str1 = zfill(num1, -dif1, is_left=True)
    else:
        str2 = zfill(num2, dif1, is_left=True)

    a, b, c, d = map(int, split_in_half(str1) + split_in_half(str2))
    len1, len2 = len(str1), len(str2)
    mid = max(len1, len2) // 2

    ac: int = karatsuba(a, c)
    bd: int = karatsuba(b, d)
    abcd: int = karatsuba(a + b, c + d)

    res1: str = zfill(ac, (len1 - mid) * 2, is_left=False)
    res2: str = zfill(abcd - bd - ac, len1 - mid, is_left=False)
    return int(res1) + int(res2) + bd


def main() -> None:
    num1: int = 21625695688898558125310188636840316594920403182768
    num2: int = 13306827740879180856696800391510469038934180115260
    res: int = karatsuba(num1, num2)
    is_equal: bool = res == num1 * num2
    print(f"{res=}", is_equal)


if __name__ == "__main__":
    main()
