RAINBOW_COLORS: list[dict[str, str | int]] = [
    {'id': 0, 'name': 'red', 'temp': 'hot'},
    {'id': 1, 'name': 'orange', 'temp': 'hot'},
    {'id': 2, 'name': 'yellow', 'temp': 'hot'},
    {'id': 3, 'name': 'green', 'temp': 'hot'},
    {'id': 4, 'name': 'light-blue', 'temp': 'cold'},
    {'id': 5, 'name': 'blue', 'temp': 'cold'},
    {'id': 6, 'name': 'purple', 'temp': 'cold'}
]


def find_obj(arr: list[dict], value: str | int, prop: str) -> str:
    for x in arr:
        if x[prop] == value:
            return x['temp']


def get_temp(value: str | int) -> str:
    value: str = str(value)
    try:
        return find_obj(RAINBOW_COLORS, int(value), 'id')
    except ValueError:
        return find_obj(RAINBOW_COLORS, value, 'name')


def main() -> None:
    res1 = get_temp('red')
    res2 = get_temp('2')
    res3 = get_temp(4)
    print(f"{res1=}, {res2=}, {res3=}")


if __name__ == "__main__":
    main()
