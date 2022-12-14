import numpy as np
import pandas as pd
from scipy.io import loadmat
from seaborn import objects as so

PLOT_SIZE: tuple[float, float] = 16, 5


def main() -> None:
    sample_rate: float = 151.51

    mat = loadmat("./assets/BOK_with_separate_trials.mat")["h"][0][0]
    tags: list[str] = [tag[0][0] for tag in mat[1] if tag[0][0] != "none"]

    df = pd.DataFrame(index=tags, data=mat[2]).transpose()
    df["timespan"] = df.index.values / sample_rate

    duration: np.float64 = df["timespan"].iloc[-1]
    print(f"Recording is {duration} seconds long")

    for tag in tags:
        plot: so.Plot = so.Plot(data=df, x="timespan", y=tag)  # type: ignore
        plot = plot.add(so.Line())

        plot = plot.label(
            title=tag,
            x="Time, s",
            y="",
        )

        plot = plot.layout(size=PLOT_SIZE)
        plot.show()


if __name__ == "__main__":
    main()
