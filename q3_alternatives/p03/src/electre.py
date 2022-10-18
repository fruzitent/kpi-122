from itertools import product, combinations
from math import ceil
from typing import Hashable

import networkx as nx
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy import typing as npt

INDEX_SET = dict[tuple[int, int], set[int]]


def index_set(df: pd.DataFrame) -> tuple[INDEX_SET, INDEX_SET]:
    cis: INDEX_SET = {}
    dis: INDEX_SET = {}

    for src, dst in product(range(df.index.size), repeat=2):
        if src == dst:
            continue

        for criterion in range(df.columns.size):
            if df.iloc[src, criterion] >= df.iloc[dst, criterion]:
                cis.setdefault((src, dst), set()).add(criterion)
            else:
                dis.setdefault((src, dst), set()).add(criterion)

    return cis, dis


def concordance_matrix(
    df: pd.DataFrame,
    cis: INDEX_SET,
    weights: list[float],
) -> pd.DataFrame:
    cim: pd.DataFrame = pd.DataFrame(
        index=df.index,
        columns=df.index,
        dtype=np.float64,
    )

    for (src, dst), indices in cis.items():
        if src == dst:
            continue

        cim.iloc[src, dst] = sum(weights[criterion] for criterion in indices)

    cim /= sum(weights)

    return cim


def discordance_matrix(
    df: pd.DataFrame,
    dis: INDEX_SET,
    is_threshold: bool,
) -> pd.DataFrame:
    dim: pd.DataFrame = pd.DataFrame(
        index=df.index,
        columns=df.index,
        dtype=np.float64,
    )

    for src, dst in product(range(df.index.size), repeat=2):
        if src == dst:
            continue

        diff: pd.Series = abs(df.iloc[src] - df.iloc[dst])
        indices: list[int] = list(dis.get((src, dst), []))
        filtered: pd.Series = diff.iloc[indices]

        delta: float = df.iloc[src].max() - df.iloc[src].min()
        scale: float = max(diff) if is_threshold else delta

        dim.iloc[src, dst] = max(filtered, default=0) / scale

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


def plot_dominance(
    ax: plt.Axes,
    adm: pd.DataFrame,
    rank: pd.Series,
    title: str = "",
) -> None:
    ax.set_title(title)
    ax.margins(0.1)
    ax.axis("off")

    graph: nx.DiGraph = nx.from_pandas_adjacency(adm, create_using=nx.DiGraph)
    pos: dict[str, npt.NDArray[np.float64]] = nx.shell_layout(graph)

    kwargs: dict[str, object] = {
        "G": graph,
        "ax": ax,
        "pos": pos,
    }

    labels: dict[tuple[str, str], str] = {}
    widths: list[float] = []

    for src, dst in graph.edges:
        label: str = f"{rank[src]} | {rank[dst]}"
        labels[(src, dst)] = label

        width: float = (rank[src] + rank[dst]) / max(rank)
        widths.append(width)

    nx.draw_networkx_nodes(**kwargs, node_color="#fffbe6")
    nx.draw_networkx_labels(**kwargs, font_color="#356859")
    nx.draw_networkx_edges(**kwargs, width=widths)
    nx.draw_networkx_edge_labels(**kwargs, edge_labels=labels, label_pos=0.3)


def get_edge_relp(series: pd.Series) -> pd.Series:
    edges: dict[tuple[Hashable, Hashable], float] = {}

    for src, dst in combinations(series.index, 2):
        if series[src] == series[dst]:
            edges[src, dst] = 2
            edges[dst, src] = 2
        elif series[src] > series[dst]:
            edges[src, dst] = 1
        else:
            edges[dst, src] = 1

    return pd.Series(
        data=[(src, dst, weight) for (src, dst), weight in edges.items()],
        dtype=object,
    )


def plot_bin_relp(fig: plt.Figure, df: pd.DataFrame, cols: int = 1) -> None:
    bin_relp: pd.DataFrame = df.apply(get_edge_relp, axis=0, result_type="expand")
    nodes: list[Hashable] = df.index.to_list()
    rows: int = ceil(bin_relp.columns.size / cols)

    for pid, (column, series) in enumerate(bin_relp.items()):
        series.dropna(inplace=True)

        ax: plt.Axes = fig.add_subplot(rows, cols, pid + 1)
        ax.set_title(f"{column}")
        ax.margins(0.1)
        ax.axis("off")

        graph: nx.DiGraph = nx.DiGraph()
        graph.add_nodes_from(nodes)
        graph.add_weighted_edges_from(series, weight="weight")
        pos: dict[str, npt.NDArray[np.float64]] = nx.shell_layout(graph)

        kwargs: dict[str, object] = {
            "G": graph,
            "ax": ax,
            "pos": pos,
        }

        widths: list[float] = []
        labels: dict[tuple[str, str], str] = {}

        for (src, dst), weight in nx.get_edge_attributes(graph, "weight").items():
            labels[(src, dst)] = f"{weight}"
            widths.append(weight)

        nx.draw_networkx_nodes(**kwargs, node_color="#fffbe6")
        nx.draw_networkx_labels(**kwargs, font_color="#356859")
        nx.draw_networkx_edges(**kwargs, width=widths)
        nx.draw_networkx_edge_labels(**kwargs, edge_labels=labels)

    fig.add_subplot(rows, cols, rows * cols)
