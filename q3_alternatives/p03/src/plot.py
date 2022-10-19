from math import ceil
from typing import Hashable

import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt

from src.electre import get_edge


def plot_graph(
    ax: plt.Axes,
    graph: nx.DiGraph,
    title: str = "",
    labels: dict[tuple[Hashable, Hashable], str] | None = None,
    widths: list[float] | None = None,
) -> None:
    if labels is None:
        labels = {}

    if widths is None:
        widths = [1]

    ax.set_title(title)
    ax.margins(0.1)
    ax.axis("off")

    kwargs: dict[str, object] = {
        "ax": ax,
        "G": graph,
        "pos": nx.shell_layout(graph),
    }

    nx.draw_networkx_nodes(**kwargs, node_color="#fffbe6")
    nx.draw_networkx_labels(**kwargs, font_color="#356859")
    nx.draw_networkx_edges(**kwargs, width=widths)
    nx.draw_networkx_edge_labels(**kwargs, edge_labels=labels, label_pos=0.3)


def plot_criteria(fig: plt.Figure, df: pd.DataFrame, cols: int = 1) -> plt.Axes:
    relationship: pd.DataFrame = df.apply(get_edge, axis=0)
    rows: int = ceil(relationship.columns.size / cols)

    for pid, (column, series) in enumerate(relationship.items()):
        series.dropna(inplace=True)

        ax: plt.Axes = fig.add_subplot(rows, cols, pid + 1)

        graph: nx.DiGraph = nx.DiGraph()
        graph.add_nodes_from(df.index)
        graph.add_weighted_edges_from(series, weight="weight")

        plot_graph(
            ax=ax,
            graph=graph,
            title=f"{column}",
        )

    return fig.add_subplot(rows, cols, rows * cols)


def plot_dominance(
    ax: plt.Axes,
    adm: pd.DataFrame,
    rank: pd.Series,
    title: str = "",
) -> None:
    graph: nx.DiGraph = nx.from_pandas_adjacency(adm, create_using=nx.DiGraph)

    labels: dict[tuple[Hashable, Hashable], str] = {}
    widths: list[float] = []

    for src, dst in graph.edges:
        label: str = f"{rank[src]} | {rank[dst]}"
        labels[(src, dst)] = label

        width: float = (rank[src] + rank[dst]) / max(rank)
        widths.append(width)

    plot_graph(
        ax=ax,
        graph=graph,
        title=title,
        labels=labels,
        widths=widths,
    )
