import turtle

from config.consts import Consts
from src.components.base_main import BaseMain


class Props(object):
    length_a: int = 30
    left_counter: int = 3
    middle_counter: int = 3
    right_counter: int = 3


class Main(BaseMain):
    def start(self) -> None:
        self.cur.lt(Consts.right_angle)
        self._loop_left()
        self._loop_middle()
        self._loop_right()

    def _loop_left(self) -> None:
        self._base_length: int = Props.length_a
        self._base_offset_horizontal: int = Props.length_a
        for itr in range(Props.left_counter * 2):
            if itr % 2 == 0:
                coord_x, coord_y = 0, Props.length_a
            else:
                coord_x, coord_y = Props.length_a, 0
            self.cur.goto(coord_x, coord_y)
            self.cur.goto(coord_y, coord_x)
            Props.length_a += self._base_length

    def _loop_middle(self) -> None:
        self._rectangle_height: int = Props.length_a - self._base_length
        for jtr in range(Props.middle_counter * 2):
            if jtr % 2 == 0:
                coord_x, coord_z = self._base_offset_horizontal, Props.length_a
                coord_y, coord_w = self._rectangle_height, 0
            else:
                coord_x, coord_z = Props.length_a, self._base_offset_horizontal
                coord_y, coord_w = 0, self._rectangle_height
            self.cur.goto(coord_x, coord_y)
            self.cur.goto(coord_z, coord_w)
            Props.length_a += self._base_length
            self._base_offset_horizontal += self._base_length

    def _loop_right(self) -> None:
        self._rectangle_length: int = Props.length_a - self._base_length
        self._base_offset_vertical: int = self._base_length
        for ktr in range(Props.right_counter * 2):
            if ktr % 2 == 0:
                coord_x, coord_z = self._base_offset_horizontal, self._rectangle_length
                coord_y, coord_w = self._rectangle_height, self._base_offset_vertical
            else:
                coord_x, coord_z = self._rectangle_length, self._base_offset_horizontal
                coord_y, coord_w = self._base_offset_vertical, self._rectangle_height
            self.cur.goto(coord_x, coord_y)
            self.cur.goto(coord_z, coord_w)
            self._base_offset_vertical += self._base_length
            self._base_offset_horizontal += self._base_length


def main(title: str = __file__) -> Main:
    instance: Main = Main(title)
    instance.start()
    return instance


if __name__ == "__main__":
    main()
    turtle.exitonclick()
