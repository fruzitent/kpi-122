from dataclasses import dataclass
from typing import Self

from matplotlib import pyplot as plt
from scipy.io import loadmat

from src.common import Signal


@dataclass(frozen=True)
class EEG(Signal):
    """Electroencephalogram."""

    @classmethod
    def from_mat(cls, filepath: str, key: str, *args, **kwargs) -> Self:
        kwargs["samples"] = loadmat(filepath)[key][0]
        return cls(*args, **kwargs)


def main() -> None:
    fig: plt.Figure = plt.figure(figsize=(16, 10))
    fig_rows: int = 2
    fig_cols: int = 1

    eeg_healthy: EEG = EEG.from_mat(
        filepath="./assets/eeg_healthy_7.mat",
        key="sig",
        sample_rate=2**8,
        units="μV",
    )
    eeg_healthy.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 1),
        title="EEG Healthy",
    )

    eeg_epilepsy: EEG = EEG.from_mat(
        filepath="./assets/eeg_epilepsy_7.mat",
        key="sig",
        sample_rate=2**8,
        units="μV",
    )
    eeg_epilepsy.plot(
        ax=fig.add_subplot(fig_rows, fig_cols, 2),
        title="EEG Epilepsy",
    )

    plt.show()


if __name__ == "__main__":
    main()
