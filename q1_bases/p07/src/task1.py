import secrets


def func():
    m = int(input('m: '))

    current = None
    sequence = range(77, 127)

    while m:
        m -= 1

        value = secrets.choice(sequence)
        if current is None or value < current:
            current = value

    return current


def main() -> None:
    res = func()
    print(f"{res=}")


if __name__ == "__main__":
    main()
