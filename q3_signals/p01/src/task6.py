from tempfile import TemporaryFile
from typing import IO

import numpy as np
from numpy import typing as npt


def main() -> None:
    time: float = 1
    sample_rate: float = 256

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = np.zeros_like(timespan, dtype=np.float64)

    temp_file: IO[bytes] = TemporaryFile()
    np.savez_compressed(
        temp_file,
        timespan=timespan,
        inp0=inp0,
    )

    temp_file.seek(0)

    npz_file: dict[str, npt.NDArray[np.float64]] = np.load(temp_file)
    for npz_key, npz_value in npz_file.items():
        print(npz_key, npz_value)


if __name__ == "__main__":
    main()
