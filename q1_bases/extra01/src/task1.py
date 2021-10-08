ENDINGS: list[str] = ["ов", "", "а", "а", "а", "ов", "ов", "ов", "ов", "ов"]


def main() -> None:
    for x in range(1000):
        ending: str = ENDINGS[x % 10]
        print(f"количество присутствующих: {x} студент{ending}")


if __name__ == "__main__":
    main()
