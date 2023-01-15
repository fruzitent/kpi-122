import numpy as np
from numpy import typing as npt


def get_response(
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
) -> npt.NDArray[np.float64]:
    return np.convolve(inp0, out0, mode="same")
