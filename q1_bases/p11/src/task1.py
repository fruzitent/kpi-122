import json
from datetime import datetime

PATH: str = '../assets/task1.json'


def main():
    date = datetime.now().month - 1

    with open(PATH) as f:
        db = json.load(f)

        for obj in db:
            if obj.get('month') != date:
                continue

            print(obj)


if __name__ == '__main__':
    main()
