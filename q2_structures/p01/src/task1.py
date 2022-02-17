import turtle

from src.components.base_main import BaseMain


class Props(object):
    add_a: int = 35
    add_b: int = 35
    length_a: int = 250
    length_b: int = 50
    repeat_times: int = 5
    rotate_degree: int = 90


class Main(BaseMain):
    def start(self) -> None:
        for _ in range(Props.repeat_times * 2):
            self.cur.fd(Props.length_a)
            self.cur.rt(Props.rotate_degree)
            self.cur.fd(Props.length_b)
            self.cur.rt(Props.rotate_degree)
            Props.length_a += Props.add_a
            Props.length_b += Props.add_b


def main(title: str = __file__) -> Main:
    instance: Main = Main(title)
    instance.start()
    return instance


if __name__ == "__main__":
    main()
    turtle.exitonclick()
