import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.fft import fft, fftfreq


def main() -> None:
    sample_rate: int = 256
    time0: int = 10
    time1: int = 2 * time0

    amp0: float = 1
    amp1: float = 2 * amp0
    freq0: float = 10
    freq1: float = 100
    hshift: float = 0
    vshift: float = 0

    dt: float = 1 / sample_rate

    timespan0: npt.NDArray[np.float64] = np.arange(0, time0, dt, dtype=np.float64)
    timespan1: npt.NDArray[np.float64] = np.arange(0, time1, dt, dtype=np.float64)
    half0: int = round(timespan0.size / 2)
    half1: int = round(timespan1.size / 2)
    freqs0: npt.NDArray[np.float64] = fftfreq(timespan0.size, dt)[:half0]
    freqs1: npt.NDArray[np.float64] = fftfreq(timespan1.size, dt)[:half1]

    sig0: npt.NDArray[np.float64] = amp0 * np.sin((2 * np.pi * freq0 * timespan0) - hshift) + vshift
    sig1: npt.NDArray[np.float64] = amp0 * np.sin((2 * np.pi * freq1 * timespan0) - hshift) + vshift
    sig2: npt.NDArray[np.float64] = amp1 * sig0
    sig3: npt.NDArray[np.float64] = amp1 * sig1

    inp0: npt.NDArray[np.float64] = sig0 + sig1
    inp1: npt.NDArray[np.float64] = np.append(sig2, sig3)
    inp2: npt.NDArray[np.float64] = np.append(sig3, sig2)

    out0: npt.NDArray[np.float64] = (2 * np.abs(fft(inp0)) / timespan0.size)[:half0]
    out1: npt.NDArray[np.float64] = (2 * np.abs(fft(inp1)) / timespan1.size)[:half1]
    out2: npt.NDArray[np.float64] = (2 * np.abs(fft(inp2)) / timespan1.size)[:half1]

    with plt.style.context("seaborn"):
        title0: str = f"Sine {freq0} Hz + Sine {freq1} Hz"
        title1: str = f"Sine {amp1} * {freq0} Hz | Sine {amp1} * {freq1} Hz"
        title2: str = f"Sine {amp1} * {freq1} Hz | Sine {amp1} * {freq0} Hz"
        plot(timespan0, freqs0, inp0, out0, title0)
        plot(timespan1, freqs1, inp1, out1, title1)
        plot(timespan1, freqs1, inp2, out2, title2)


def plot(
    timespan: npt.NDArray[np.float64],
    freqs: npt.NDArray[np.float64],
    inp: npt.NDArray[np.float64],
    out: npt.NDArray[np.float64],
    title: str,
) -> None:
    _, (ax0, ax1) = plt.subplots(figsize=(16, 10), ncols=1, nrows=2)

    ax0.plot(timespan, inp)
    ax0.set_title(title)
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Amplitude, V")

    ax1.stem(freqs, out)
    ax1.set_title("Amplitude Spectrum")
    ax1.set_xlabel("Frequency, Hz")
    ax1.set_ylabel("Amplitude, V")

    plt.show()


if __name__ == "__main__":
    main()
