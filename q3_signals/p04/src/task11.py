import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    sample_rate: int = 128

    low: float = 1.5
    high: float = 3

    dt: float = 1 / sample_rate

    inp0: npt.NDArray[np.float64] = np.random.randint(-128, 128, size=1024).astype(np.float64)
    timespan: npt.NDArray[np.float64] = np.arange(inp0.size, dtype=np.float64) / sample_rate

    mask: npt.NDArray[np.bool_] = cut(timespan, low, high)
    inp0 = inp0[mask]
    timespan = timespan[mask]

    half: int = round(timespan.size / 2)
    freqs: npt.NDArray[np.float64] = fftfreq(timespan.size, dt)[:half]

    out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0) / timespan.size))[:half]
    out1: npt.NDArray[np.float64] = np.angle(fft(inp0))[:half]

    with plt.style.context("seaborn"):
        plot(timespan, freqs, inp0, out0, out1)


def plot(
    timespan: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
    out0: npt.NDArray[np.float64],
    out1: npt.NDArray[np.float64],
) -> None:
    _, (ax0, ax1, ax2) = plt.subplots(figsize=(16, 15), ncols=1, nrows=3)

    ax0.plot(timespan, inp0)
    ax0.set_title("Signal")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Amplitude, $V$")

    ax1.stem(freqs, out0)
    ax1.set_title("Amplitude spectrum")
    ax1.set_xlabel("Frequency, $Hz$")
    ax1.set_ylabel("Amplitude, $V$")

    ax2.stem(freqs, out1)
    ax2.set_title("Phase spectrum")
    ax2.set_xlabel("Frequency, $Hz$")
    ax2.set_ylabel("Phase, $rad$")

    plt.show()


def cut(samples: npt.NDArray[np.float64], t0: float, t1: float) -> npt.NDArray[np.bool_]:
    if t0 < 0:
        raise ValueError("t0 must be equal or greater than 0")

    if t0 > t1:
        raise ValueError("t0 must be equal or less than t1")

    back: np.float64 = samples[-1]
    if t1 > back:
        raise ValueError(f"t1 must be equal or less than {back}")

    cond0: npt.NDArray[np.bool_] = samples >= t0
    cond1: npt.NDArray[np.bool_] = samples <= t1
    return cond0 & cond1


if __name__ == "__main__":
    main()
