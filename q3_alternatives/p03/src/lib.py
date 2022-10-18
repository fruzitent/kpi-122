from dataclasses import dataclass
from itertools import product
from typing import Callable

import numpy as np
import pandas as pd

T = float | str | None


@dataclass(frozen=True)
class Criterion(object):
    name: str
    description: str
    weight: float
    rules: dict[float, Callable[[T], bool]]

    def apply(self, x: T) -> float:
        for score, guard in self.rules.items():
            if guard(x):
                return score
        raise ValueError(f"Invalid value: {x}")


@dataclass(frozen=True)
class Alternative(object):
    name: str
    description: str
    values: dict[str, T]


def to_frame(
    criteria: list[Criterion],
    alternatives: list[Alternative],
) -> tuple[pd.DataFrame, list[float]]:
    data: list[float] = [
        criterion.apply(value)
        for criterion, alternative in product(criteria, alternatives)
        for key, value in alternative.values.items()
        if key == criterion.description
    ]

    df: pd.DataFrame = pd.DataFrame(
        columns=[criterion.name for criterion in criteria],
        index=[alternative.name for alternative in alternatives],
        data=np.array(data).reshape(len(criteria), len(alternatives)).T,
        dtype=np.float64,
    )

    weights: list[float] = [criterion.weight for criterion in criteria]

    # np.sqrt(np.sum(df ** 2, axis=0))
    df /= np.linalg.norm(df, axis=0, ord=2)
    df *= weights

    return df, weights
