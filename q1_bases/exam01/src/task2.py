def get_median(*nums: int) -> int:
    middle: int = len(nums) // 2
    return (nums[middle] + nums[~middle]) // 2


def main() -> None:
    num1: int = 15
    num2: int = 26
    num3: int = 29
    res: int = get_median(num1, num2, num3)
    print(f"{res=}")


if __name__ == "__main__":
    main()
