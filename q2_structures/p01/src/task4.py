import turtle

from config.consts import Consts
from src.components.base_main import BaseMain


class Props(object):
    add_a: int = 25
    length_a: int = 50
    repeat_times: int = 10


class Main(BaseMain):
    def start(self) -> None:
        for _ in range(Props.repeat_times):
            self._loop()
            previous_length: int = Props.length_a
            Props.length_a += Props.add_a
            offset: float = (Props.length_a - previous_length) / 2
            coord_x, coord_y = self.cur.pos()
            self._tp(coord_x - offset, coord_y - offset)

    def _loop(self) -> None:
        for _ in range(4):
            self.cur.fd(Props.length_a)
            self.cur.lt(Consts.right_angle)


def main(title: str = __file__) -> Main:
    instance: Main = Main(title)
    instance.start()
    return instance


if __name__ == "__main__":
    main()
    turtle.exitonclick()
