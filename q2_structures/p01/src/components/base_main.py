import turtle

from config.config import Config


class BaseMain(object):
    def __init__(self, title: str) -> None:
        turtle.title(title)

        self.cur: turtle.Turtle = turtle.Turtle()
        self.cur.shape(Config.turtle_shape)
        self.cur.speed(Config.turtle_speed)

    def clear(self) -> None:
        self.cur.hideturtle()
        self.cur.clear()

    def _tp(self, coord_x: float, coord_y: float) -> None:
        self.cur.up()
        self.cur.goto(coord_x, coord_y)
        self.cur.down()
