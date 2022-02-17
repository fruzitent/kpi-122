import turtle

from src.components.base_main import BaseMain


class Props(object):
    radius: int = 25
    repeat_times: int = 10
    rotate_degree: int = 90
    space_inbetween: int = 10


class Main(BaseMain):
    def start(self) -> None:
        self.cur.setheading(Props.rotate_degree)
        for itr in range(Props.repeat_times):
            radius: int = Props.radius + Props.space_inbetween * itr
            self.cur.circle(-radius)
            self.cur.circle(radius)


def main(title: str = __file__) -> Main:
    instance: Main = Main(title)
    instance.start()
    return instance


if __name__ == "__main__":
    main()
    turtle.exitonclick()
