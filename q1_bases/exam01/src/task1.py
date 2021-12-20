def reduce_dicts(*args: dict[str, int]) -> dict[str, int]:
    new_obj: dict[str, int] = {}

    for obj in args:
        for key, value in obj.items():
            if new_obj.get(key):
                new_obj[key] += value
            else:
                new_obj[key] = value

    return new_obj


def main() -> None:
    d1: dict[str, int] = {"a": 200, "b": 200, "c": 300}
    d2: dict[str, int] = {"a": 200, "b": 200, "d": 400}
    d3: dict[str, int] = reduce_dicts(d1, d2)
    print(f"{d3=}")


if __name__ == "__main__":
    main()
