from random import SystemRandom
from timeit import Timer


class Comparator(object):
    def __init__(self) -> None:
        self._counter: int = 0

    @property
    def counter(self) -> int:
        return self._counter

    def dispatch(self, kind: str) -> None:
        match kind:
            case "increment":
                self._counter += 1
            case "decrement":
                self._counter -= 1
            case "reset":
                self._counter = 0
            case _:
                raise ValueError("incorrect dispatch type")

    def ge(self, num1: int, num2: int) -> bool:
        self.dispatch("increment")
        return num1 >= num2

    def gt(self, num1: int, num2: int) -> bool:
        self.dispatch("increment")
        return num1 > num2

    def lt(self, num1: int, num2: int) -> bool:
        self.dispatch("increment")
        return num1 < num2


comparator = Comparator()


def quick_sort(arr: list[int], lf: int, rt: int, pivot: int = 0) -> None:
    if lf >= rt:
        return

    match pivot:
        case 0:
            pivot = arr[lf + (rt - lf) // 2]
        case 1:
            pivot = arr[0]
        case _:
            pivot = arr[rt]

    itr: int = lf
    jtr: int = rt

    while True:
        while comparator.lt(arr[itr], pivot):
            itr += 1

        while comparator.gt(arr[jtr], pivot):
            jtr -= 1

        if comparator.ge(itr, jtr):
            break

        arr[itr], arr[jtr] = arr[jtr], arr[itr]
        itr += 1
        jtr -= 1

    quick_sort(arr, lf, jtr)
    quick_sort(arr, jtr + 1, rt)


def main() -> None:
    sample: int = 1000000
    for itr in range(3):
        arr: list[int] = SystemRandom().sample(range(sample), sample)
        size: int = len(arr) - 1
        timings = Timer(
            setup="from __main__ import quick_sort",
            stmt=f"quick_sort({arr}, 0, {size}, {itr})",
        ).autorange()
        print(comparator.counter, timings)
        comparator.dispatch("reset")


if __name__ == "__main__":
    main()
