def get_clock(num: int) -> str:
    hours: str = str(num // 60 % 24).zfill(2)
    minutes: str = str(num % 60).zfill(2)
    return f"{hours}:{minutes}"


def main() -> None:
    res1: str = get_clock(150)
    res2: str = get_clock(1441)
    print(f"{res1=}, {res2=}")


if __name__ == "__main__":
    main()
