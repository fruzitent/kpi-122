from tempfile import TemporaryFile
from typing import IO

import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    temp_file: IO[bytes] = TemporaryFile()
    np.savez_compressed(temp_file, data=np.random.randint(-10, 10, size=100))
    temp_file.seek(0)

    sample_rate: float = 128

    inp0: npt.NDArray[np.float64] = np.load(temp_file)["data"]
    time: float = inp0.size / sample_rate
    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    half: int = round(timespan.size / 2)
    freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

    out0: npt.NDArray[np.float64] = np.abs((fft(inp0) / timespan.size)[:half]) ** 2

    with plt.style.context("seaborn"):
        plot(timespan, freqs, inp0, out0)


def plot(
    timespan: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 10), ncols=1, nrows=2)

    ax0.plot(timespan, inp0)
    ax0.set_title("Signal")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Amplitude, $V$")

    ax1.stem(freqs, out0)
    ax1.set_title("Power desity")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Power, $W/m^3$")

    plt.show()


if __name__ == "__main__":
    main()
