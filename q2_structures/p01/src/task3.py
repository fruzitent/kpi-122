import turtle
from typing import Callable

from config.consts import Consts
from src.components.base_main import BaseMain


class Props(object):
    length_a: int = 100
    length_b: int = 20
    center_offset: float = length_b / 2
    repeat_times: int = 4


class Main(BaseMain):
    def start(self) -> None:
        self._tp(Props.center_offset, 0)
        self.cur.lt(Consts.right_angle)
        self._loop()
        self._tp(-Props.center_offset, Props.length_a)
        self.cur.rt(Consts.right_angle)
        self._loop()

    def _loop(self) -> None:
        for itr in range(Props.repeat_times):
            for jtr in range(4):
                if itr == Props.repeat_times - 1 and jtr == 3:
                    return

                side_length: int = Props.length_a if jtr % 2 == 0 else Props.length_b
                self.cur.fd(side_length)

                rotate_direction: Callable[[float], None] = (
                    self.cur.rt if jtr <= 1 else self.cur.lt
                )
                rotate_direction(Consts.right_angle)


def main(title: str = __file__) -> Main:
    instance: Main = Main(title)
    instance.start()
    return instance


if __name__ == "__main__":
    main()
    turtle.exitonclick()
