"""
Task 12.

Find the total area covered by two rectangles on the plane.
The rectangles are given by the coordinates of two opposing angles.
INPUT: [(0, 2), (5, 6)], [(3, 3), (7, 0)]
OUTPUT: area = 30
"""
from dataclasses import dataclass


@dataclass
class Point(object):
    x: int
    y: int


@dataclass
class Rectangle(object):
    lf: Point
    rt: Point

    @property
    def dx(self) -> int:
        return abs(self.lf.x - self.rt.x)

    @property
    def dy(self) -> int:
        return abs(self.lf.y - self.rt.y)

    @property
    def area(self) -> int:
        return self.dx * self.dy


def get_area(rect1: Rectangle, rect2: Rectangle) -> int:
    dx: int = min(rect1.rt.x, rect2.rt.x) - max(rect1.lf.x, rect2.lf.x)
    dy: int = min(rect1.rt.y, rect2.rt.y) - max(rect1.lf.y, rect2.lf.y)

    intersect: int = 0
    if dx > 0 and dy > 0:
        intersect = dx * dy

    return rect1.area + rect2.area - intersect


def main() -> None:
    rect1: Rectangle = Rectangle(Point(0, 2), Point(5, 6))
    rect2: Rectangle = Rectangle(Point(3, 3), Point(7, 0))
    area: int = get_area(rect1, rect2)
    print(f"{area=}")


if __name__ == "__main__":
    main()
