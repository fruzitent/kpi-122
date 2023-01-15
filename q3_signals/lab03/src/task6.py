import numpy as np
from numpy import typing as npt
from scipy.signal import TransferFunction, dimpulse


def get_system(
    numerator: npt.NDArray[np.float64],
    denumerator: npt.NDArray[np.float64],
    timespan: npt.NDArray[np.float64],
) -> npt.NDArray[np.float64]:
    system: TransferFunction = TransferFunction(numerator, denumerator, dt=1)
    timespan, impulse = dimpulse(system, t=timespan)
    return np.squeeze(impulse)  # type: ignore
