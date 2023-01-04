from math import isclose
from typing import Self

from src.task1 import BackwardNewton, ForwardNewton


class TestForwardNewton(object):
    def test_interpolate(self: Self) -> None:
        assert isclose(
            ForwardNewton(
                xs=[15, 20, 25, 30, 35, 40, 45, 50, 55],
                ys=[0.2588, 0.342, 0.4226, 0.5, 0.5736, 0.6428, 0.7071, 0.766, 0.8192],
            ).interpolate(56),
            0.8292262631423994,
        )
        assert isclose(
            ForwardNewton(
                xs=[1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2],
                ys=[0.8427, 0.8802, 0.9103, 0.934, 0.9523, 0.9661, 0.9763, 0.9838, 0.9891, 0.9928, 0.9953],
            ).interpolate(1.43),
            0.9568743986922327,
        )
        assert isclose(
            ForwardNewton(
                xs=[0, 0.2, 0.4, 0.6, 0.8, 1],
                ys=[1.2715, 2.4652, 3.6443, 4.8095, 5.9614, 7.1005],
            ).interpolate(0.1),
            1.8702226562499997,
        )


class TestBackwardNewton(object):
    def test_interpolate(self: Self) -> None:
        assert isclose(
            BackwardNewton(
                xs=[0, 0.2, 0.4, 0.6, 0.8, 1],
                ys=[1.2715, 2.4652, 3.6443, 4.8095, 5.9614, 7.1005],
            ).interpolate(0.9),
            6.53252265625,
        )
