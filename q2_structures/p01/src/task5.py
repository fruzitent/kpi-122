import turtle

from src.components.base_main import BaseMain


class Props(object):
    length_a: int = 25
    sides_min: int = 3
    sides_max: int = 15


class Main(BaseMain):
    def start(self) -> None:
        min_val: int = Props.length_a
        max_val: int = Props.length_a * Props.sides_max
        for index, radius in enumerate(range(min_val, max_val, min_val)):
            self._tp(0, -radius)
            self.cur.circle(radius, steps=index + 3)


def main(title: str = __file__) -> Main:
    instance: Main = Main(title)
    instance.start()
    return instance


if __name__ == "__main__":
    main()
    turtle.exitonclick()
