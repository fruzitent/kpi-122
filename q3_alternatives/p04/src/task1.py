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
    alternatives: list[str] = ["d1", "d2", "d3"]
    criteria: list[str] = ["q1", "q2", "q3"]

    significance: pd.DataFrame = pd.DataFrame(
        columns=criteria,
        index=criteria,
        data=[
            [1, 2, 3],
            [0.5, 1, 0.5],
            [0.33, 2, 1],
        ],
        dtype=np.float64,
    )

    vectors: list[pd.DataFrame] = [
        pd.DataFrame(
            columns=alternatives,
            index=alternatives,
            data=[
                [1, 4, 3],
                [1 / 4, 1, 2],
                [1 / 3, 1 / 2, 1],
            ],
            dtype=np.float64,
        ),
        pd.DataFrame(
            columns=alternatives,
            index=alternatives,
            data=[
                [1, 1 / 4, 6],
                [4, 1, 1 / 2],
                [1 / 6, 2, 1],
            ],
            dtype=np.float64,
        ),
        pd.DataFrame(
            columns=alternatives,
            index=alternatives,
            data=[
                [1, 3, 1 / 5],
                [1 / 3, 1, 1 / 3],
                [5, 3, 1],
            ],
            dtype=np.float64,
        ),
    ]

    by_criteria: pd.DataFrame = pd.DataFrame(
        columns=alternatives,
        index=alternatives,
        data=map(vector_component, vectors),
        dtype=np.float64,
    )

    ranking: pd.Series = pd.Series(
        index=alternatives,
        data=np.dot(vector_component(significance), by_criteria),
        dtype=np.float64,
    ).sort_values(ascending=False)
    print(ranking)


if __name__ == "__main__":
    main()
