import asyncio
import sys
from types import TracebackType
from typing import Self
from unittest.mock import Mock

import numpy as np
from cffi.backend_ctypes import CTypesData
from matplotlib import pyplot as plt
from numpy import typing as npt
from scipy.io import wavfile

is_sd_mocked: bool = False

try:
    import sounddevice as sd
except OSError:
    sd = Mock()
    is_sd_mocked = True


def main() -> None:
    if is_sd_mocked:
        main_file()
    else:
        try:
            with asyncio.Runner() as runner:
                runner.run(main_record())
        except KeyboardInterrupt:
            print("Interrupted")
            exit(0)


async def main_record() -> None:
    channels: int = 2
    downsample: int = 100
    sample_rate: float = 44100
    time: float = 5

    dt: float = 1 / sample_rate
    samples: int = round(time * sample_rate)

    timespan: npt.NDArray[np.float64] = np.arange(0, time, dt, dtype=np.float64)
    buffer: npt.NDArray[np.float64] = np.empty(
        shape=(samples, channels),
        dtype=np.float64,
    )

    with Recorder(buffer) as recorder:
        await recorder.record(channels, sample_rate)

    with plt.style.context("seaborn"):
        plot(timespan, buffer, downsample)


def main_file() -> None:
    downsample: int = 100

    sample_rate, buffer = wavfile.read("./assets/HNS4 HiTECH BassLine Loops 39 C 175 BPM.wav")
    timespan: npt.NDArray[np.float64] = np.arange(buffer.shape[0], dtype=np.float64) / sample_rate

    with plt.style.context("seaborn"):
        plot(timespan, buffer, downsample)


def plot(
    timespan: npt.NDArray[np.float64],
    buffer: npt.NDArray[np.float64],
    downsample: int = 1,
) -> None:
    _, (ax0) = plt.subplots(figsize=(16, 5), ncols=1, nrows=1)

    for idx in range(buffer.shape[-1]):
        signal: npt.NDArray[np.float64] = buffer[..., idx]
        label: str = f"Channel {idx}"

        ax0.plot(
            timespan[::downsample],
            signal[::downsample],
            label=label,
        )

    ax0.legend(loc="upper right")
    ax0.set_title("Recording")
    ax0.set_xlabel("Time, $s$")
    ax0.set_ylabel("Amplitude, $V$")

    plt.show()


class Recorder(object):
    def __init__(self: Self, buffer: npt.NDArray[np.float64]) -> None:
        self.buffer: npt.NDArray[np.float64] = buffer

        self._idx: int = 0
        self._event: asyncio.Event = asyncio.Event()
        self._loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

    def __enter__(self: Self) -> Self:
        return self

    def __exit__(self: Self, error: Exception, message: str, traceback: TracebackType) -> bool:
        return True

    def callback(
        self: Self,
        inp: npt.NDArray[np.float64],
        frames: int,
        latency: CTypesData,  # https://files.portaudio.com/docs/v19-doxydocs/structPaStreamCallbackTimeInfo.html
        status: sd.CallbackFlags,
    ) -> None:
        if status:
            print(status, file=sys.stderr)

        remainder: int = self.buffer.shape[0] - self._idx
        if remainder == 0:
            self._loop.call_soon_threadsafe(self._event.set)
            raise sd.CallbackStop

        inp = inp[:remainder]
        buf_from: int = self._idx
        buf_upto: int = self._idx + inp.shape[0]
        self.buffer[buf_from:buf_upto] = inp  # noqa: WPS362 Found assignment to a subscript slice
        self._idx += inp.shape[0]

    async def record(
        self: Self,
        channels: int,
        sample_rate: float,
    ) -> None:
        with sd.InputStream(
            callback=self.callback,
            channels=channels,
            samplerate=sample_rate,
        ):
            await self._event.wait()


if __name__ == "__main__":
    main()
