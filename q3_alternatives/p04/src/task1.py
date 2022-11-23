from types import MappingProxyType

import numpy as np
import pandas as pd
from numpy import typing as npt

RANDOM_CONSISTENCY_INDEX: MappingProxyType[int, float] = MappingProxyType(
    mapping={
        1: 0,
        2: 0,
        3: 0.58,
        4: 0.9,
        5: 1.12,
        6: 1.24,
        7: 1.32,
        8: 1.41,
        9: 1.45,
        10: 1.49,
        11: 1.51,
        12: 1.54,
        13: 1.56,
        14: 1.57,
        15: 1.58,
    },
)


def geometric_mean(array: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    # np.prod(array) ** (1 / array.size) may overflow
    return np.exp(np.log(array).mean())


def is_consistent(df: pd.DataFrame) -> bool:
    sigma: pd.Series = df.sum(axis=0)
    priority_vector: pd.Series = (df / sigma).mean(axis=1)
    eigen_value: np.float64 = (sigma * priority_vector).sum()
    consistency_index: np.float64 = (eigen_value - df.index.size) / (df.index.size - 1)
    consistency_ratio: np.float64 = consistency_index / RANDOM_CONSISTENCY_INDEX[df.index.size]
    return np.abs(consistency_ratio) < 0.1


def vector_component(df: pd.DataFrame) -> pd.Series:
    if not is_consistent(df):
        print("WARNING: Inconsistent matrix")

    series: pd.Series = df.apply(geometric_mean, axis=1)
    return series / series.sum()


def main() -> None:
    alternatives: list[str] = ["d1", "d2", "d3", "d4"]
    criteria: list[str] = ["c1", "c2", "c3", "c4", "c5"]

    criterion_priorities: pd.DataFrame = pd.DataFrame(
        columns=criteria,
        index=criteria,
        data=[
            [1, 3, 1.5, 3, 2.1],
            [0.33, 1, 0.5, 1, 0.7],
            [0.67, 2, 1, 2, 1.4],
            [0.33, 1, 0.5, 1, 0.7],
            [0.48, 1.43, 0.71, 1.43, 1],
        ],
        dtype=np.float64,
    )

    alternative_priorities: list[pd.DataFrame] = [
        pd.DataFrame(
            columns=alternatives,
            index=alternatives,
            data=[
                [1, 0.5, 1.5, 1.05],
                [2, 1, 3, 2.1],
                [0.67, 0.33, 1, 0.7],
                [0.95, 0.48, 1.43, 1],
            ],
            dtype=np.float64,
        ),
        pd.DataFrame(
            columns=alternatives,
            index=alternatives,
            data=[
                [1, 2, 1, 3],
                [0.5, 1, 0.5, 1.5],
                [1, 2, 1, 3],
                [0.33, 0.67, 0.33, 1],
            ],
            dtype=np.float64,
        ),
        pd.DataFrame(
            columns=alternatives,
            index=alternatives,
            data=[
                [1, 2, 6, 12],
                [0.5, 1, 3, 6],
                [0.17, 0.33, 1, 2],
                [0.08, 0.17, 0.5, 1],
            ],
            dtype=np.float64,
        ),
        pd.DataFrame(
            columns=alternatives,
            index=alternatives,
            data=[
                [1, 3, 6, 9],
                [0.33, 1, 2, 3],
                [0.17, 0.5, 1, 1.5],
                [0.11, 0.33, 0.67, 1],
            ],
            dtype=np.float64,
        ),
        pd.DataFrame(
            columns=alternatives,
            index=alternatives,
            data=[
                [1, 0.2, 0.8, 1.6],
                [5, 1, 4, 8],
                [1.25, 0.25, 1, 2],
                [0.63, 0.13, 0.5, 1],
            ],
            dtype=np.float64,
        ),
    ]

    eigen_vectors: pd.DataFrame = pd.DataFrame(
        columns=alternatives,
        index=criteria,
        data=map(vector_component, alternative_priorities),
        dtype=np.float64,
    )

    ranking: pd.Series = pd.Series(
        index=alternatives,
        data=np.dot(vector_component(criterion_priorities), eigen_vectors),
        dtype=np.float64,
    ).sort_values(ascending=False)
    print(ranking)


if __name__ == "__main__":
    main()
