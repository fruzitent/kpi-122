import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, ifft


def main() -> None:
    sample_rate: float = 512
    time: float = 5

    amp: float = 1
    freq: float = 5
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    sig0: npt.NDArray[np.float64] = amp * np.sin((2 * np.pi * freq * timespan) - hshift) + vshift
    inp0: npt.NDArray[np.float64] = np.exp(-timespan) * sig0
    out0: npt.NDArray[np.float64] = np.real(ifft(fft(inp0)))

    with plt.style.context("seaborn"):
        plot(timespan, inp0, out0)


def plot(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0, label="Original")
    ax0.plot(timespan, out0, label="Restored", linestyle="dashed")
    ax0.legend()
    ax0.set_title("Fourier transform")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Amplitude, $V$")

    plt.show()


if __name__ == "__main__":
    main()
