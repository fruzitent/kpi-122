INPUT_PATH = "../assets/input.txt"
OUTPUT_PATH = "../assets/output.txt"


def get_input() -> tuple[int, list[int]]:
    with open(INPUT_PATH, "r") as file_input:
        lines: list[str] = file_input.read().split("\n")[:-1]
        nums: list[int] = [int(num) for num in lines]
        return nums[0], nums[1:]


def save_output(arr: list[int]) -> None:
    with open(OUTPUT_PATH, "w") as file_output:
        text = "\n".join([str(num) for num in arr])
        file_output.write(text)


def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    res: list[int] = []
    itr: int = 0
    jtr: int = 0

    while itr < len(arr1) and jtr < len(arr2):
        if arr1[itr] <= arr2[jtr]:
            res.append(arr1[itr])
            itr += 1
        else:
            res.append(arr2[jtr])
            jtr += 1

    return res + arr1[itr:] + arr2[jtr:]


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) > 1:
        mid: int = len(arr) // 2
        lf: list[int] = merge_sort(arr[:mid])
        rt: list[int] = merge_sort(arr[mid:])
        return merge(lf, rt)
    return arr


def main() -> None:
    size, nums = get_input()
    arr: list[int] = merge_sort(nums)
    save_output(arr)
    print(nums, arr, sep="\n")


if __name__ == "__main__":
    main()
