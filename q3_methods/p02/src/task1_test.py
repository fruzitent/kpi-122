from math import isclose

from src.task1 import lagrange


def test_lagrange() -> None:
    assert isclose(lagrange([-1, 3], [-3, 2], 1), -0.5)
    assert isclose(lagrange([-3, -1, 1, 2], [3, 3, -13, -12], -4), -18)
    assert isclose(lagrange([0, 2, 3, 5], [1, 3, 2, 5], 4), 2.0666666666666664)
    assert isclose(lagrange([0.41, 1.55, 2.67, 3.84], [2.63, 3.75, 4.87, 5.03], 1.91), 4.153908736123033)
    assert isclose(lagrange([321, 322.8, 324.2, 325], [2.50651, 2.50893, 2.51081, 2.51188], 323.5), 2.50987083688447)
