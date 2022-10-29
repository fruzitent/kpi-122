from collections import defaultdict
from itertools import combinations, product
from typing import DefaultDict, Hashable

import numpy as np
import pandas as pd

Edge = tuple[Hashable, Hashable, float]
IndexSet = DefaultDict[tuple[int, int], set[int]]


def get_edge(series: pd.Series) -> pd.Series:
    edges: list[Edge] = []

    for src, dst in combinations(series.index, 2):
        if series[src] > series[dst]:
            edges.append((src, dst, 1))
        elif series[src] < series[dst]:
            edges.append((dst, src, 1))
        # else:
        #     edges.extend([(src, dst, 2), (dst, src, 2)])

    return pd.Series(edges, dtype=object)


def index_set(df: pd.DataFrame) -> tuple[IndexSet, IndexSet]:
    cis: IndexSet = defaultdict(set)
    dis: IndexSet = defaultdict(set)

    for src, dst in product(range(df.index.size), repeat=2):
        if src == dst:
            continue

        for criterion in range(df.columns.size):
            if df.iloc[src, criterion] >= df.iloc[dst, criterion]:
                cis[src, dst].add(criterion)
            else:
                dis[src, dst].add(criterion)

    return cis, dis


def concordance_matrix(
    df: pd.DataFrame,
    cis: IndexSet,
    weights: list[float],
) -> pd.DataFrame:
    cim: pd.DataFrame = pd.DataFrame(
        index=df.index,
        columns=df.index,
        dtype=np.float64,
    )

    for (src, dst), indices in cis.items():
        cim.iloc[src, dst] = sum(weights[criterion] for criterion in indices)

    return cim / sum(weights)


def discordance_matrix(
    df: pd.DataFrame,
    dis: IndexSet,
    is_threshold: bool,
) -> pd.DataFrame:
    dim: pd.DataFrame = pd.DataFrame(
        index=df.index,
        columns=df.index,
        dtype=np.float64,
    )

    for (src, dst), indices in dis.items():
        diff: pd.Series = (df.iloc[src] - df.iloc[dst]).abs()
        scale: float = diff.max() if is_threshold else df.iloc[src].ptp()
        dim.iloc[src, dst] = diff.iloc[list(indices)].max() / scale

    return dim


def threshold_value(
    df: pd.DataFrame,
    cim: pd.DataFrame,
    dim: pd.DataFrame,
) -> tuple[float, float]:
    threshold: float = df.index.size * (df.index.size - 1)
    p: float = cim.sum().sum() / threshold
    q: float = dim.sum().sum() / threshold
    return p, q


def electre1(
    df: pd.DataFrame,
    weights: list[float],
    p: float | None = None,
    q: float | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series]:
    is_threshold: bool = p is None and q is None

    cis, dis = index_set(df)
    cim: pd.DataFrame = concordance_matrix(df, cis, weights)
    dim: pd.DataFrame = discordance_matrix(df, dis, is_threshold)

    if is_threshold:
        p, q = threshold_value(df, cim, dim)
        adm: pd.DataFrame = (cim >= p) & (dim >= q)
    else:
        adm: pd.DataFrame = (cim >= p) & (dim <= q)

    rank: pd.Series = adm.sum(axis=1).sort_values(ascending=False)

    return cim, dim, adm.astype(np.int64), rank
