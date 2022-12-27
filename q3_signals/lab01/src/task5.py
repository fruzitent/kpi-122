import numpy as np
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.signal import square


def main() -> None:
    square_wave_infinite()
    square_wave_buffer()
    square_pulse()


def square_wave_infinite() -> None:
    sample_rate: float = 256
    time: float = 10

    amp: float = 1

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = square(2 * np.pi * amp * timespan)

    with plt.style.context("seaborn"):
        plot_square_wave_infinite(timespan, inp0)


def plot_square_wave_infinite(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Square Wave [Infinite]")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Amplitude, V")

    plt.show()


def square_wave_buffer() -> None:
    time: float = 10000
    sample_rate: float = 256

    amp: float = 100
    width: float = 300

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = fill_square_buffer(timespan, sample_rate, width, amp)

    with plt.style.context("seaborn"):
        plot_square_wave_buffer(timespan, inp0)


def plot_square_wave_buffer(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Square Wave [Buffer]")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Amplitude, V")

    plt.show()


def square_pulse() -> None:
    sample_rate: float = 256
    time: float = 10000

    amp: float = 100
    center: float = 4000
    width: float = 300

    dt: float = 1 / sample_rate

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    inp0: npt.NDArray[np.float64] = make_square_pulse(timespan, sample_rate, center, width, amp)

    with plt.style.context("seaborn"):
        plot_square_pulse(timespan, inp0)


def plot_square_pulse(
    timespan: npt.NDArray[np.float64],
    inp0: npt.NDArray[np.float64],
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    ax0.plot(timespan, inp0)
    ax0.set_title("Square Pulse")
    ax0.set_xlabel("Time, s")
    ax0.set_ylabel("Amplitude, V")

    plt.show()


def make_square_pulse(
    timespan: npt.NDArray[np.float64],
    sample_rate: float,
    center: float,
    width: float,
    amp: float,
) -> npt.NDArray[np.float64]:
    inp0: npt.NDArray[np.float64] = np.zeros_like(timespan, dtype=np.float64)

    inp0_from: int = int(sample_rate * (center - width / 2))
    inp0_upto: int = int(sample_rate * (center + width / 2))
    if inp0_from < 0 or inp0_upto > len(timespan):
        raise ValueError("out of bounds")

    inp0[inp0_from:inp0_upto] = amp  # noqa: WPS362 Found assignment to a subscript slice
    return inp0


def fill_square_buffer(
    timespan: npt.NDArray[np.float64],
    sample_rate: float,
    width: float,
    amp: float,
) -> npt.NDArray[np.float64]:
    buffer: npt.NDArray[np.float64] = np.zeros_like(timespan, dtype=np.float64)

    idx: int = 1
    while True:
        try:
            buffer += make_square_pulse(timespan, sample_rate, width * idx, width, amp)
        except ValueError:
            return buffer
        idx += 2


if __name__ == "__main__":
    main()
