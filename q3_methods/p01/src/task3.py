from src.task2 import BroadSense, NarrowSense, Sense


def main() -> None:
    stats(NarrowSense("0.374"))
    print("---")
    stats(BroadSense("4.348"))


def stats(number: Sense) -> None:
    print("x:", number)
    print("Δx:", number.maximum_absolute_error)
    print("δx:", number.maximum_relative_error)


if __name__ == "__main__":
    main()
