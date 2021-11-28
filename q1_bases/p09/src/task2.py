import json

INPUT_PATH: str = "../assets/db.json"


def main() -> None:
    with open(INPUT_PATH, "r") as file:
        db = json.load(file)

    for person in db:
        if person["phone"][-1] == '3':
            print(person)


if __name__ == "__main__":
    main()
