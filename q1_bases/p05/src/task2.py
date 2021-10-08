def get_input() -> int | None:
    current = None
    while True:
        value: int = int(input('Enter value: '))
        if not value:
            break
        if current is None or value > current:
            current = value
    return current


def main() -> None:
    res: int | None = get_input()
    print(f"{res=}")


if __name__ == "__main__":
    main()
