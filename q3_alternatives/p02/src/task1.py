from dataclasses import dataclass
from typing import Any, Hashable

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import typing as npt

TypeN = np.float64
ND = npt.NDArray[TypeN]

SHOW_PLOTS: bool = True


@dataclass
class CPU(object):
    name: str
    cores: int
    threads: int
    frequency: float


@dataclass
class SSD(object):
    name: str
    capacity: int
    tbw: int
    price: int


# fmt: off
CPUs: tuple[CPU, ...] = (
    CPU(name="AMD Athlon 3000G",         cores=2,  threads=4,   frequency=3.5),
    CPU(name="AMD Ryzen 3 3300X",        cores=4,  threads=8,   frequency=4.3),
    CPU(name="AMD Ryzen 5 3600XT",       cores=6,  threads=12,  frequency=4.5),
    CPU(name="AMD Ryzen 7 3800XT",       cores=8,  threads=16,  frequency=4.7),
    CPU(name="AMD Ryzen 9 3590X",        cores=16, threads=32,  frequency=4.7),
    # CPU(name="AMD Threadripper 3990X",   cores=64, threads=128, frequency=4.3),
    CPU(name="Intel Core i3-12300",      cores=4,  threads=8,   frequency=4.4),
    CPU(name="Intel Core i5-12600",      cores=6,  threads=12,  frequency=4.8),
    CPU(name="Intel Core i7-12700",      cores=12, threads=20,  frequency=4.9),
    CPU(name="Intel Core i9-12900",      cores=16, threads=24,  frequency=5.1),
    CPU(name="Intel Pentium Gold G7400", cores=2,  threads=4,   frequency=3.7),
    # CPU(name="Intel Xeon Platinum 9282", cores=56, threads=112, frequency=3.8),
)

SSDs: tuple[SSD, ...] = (
    SSD(name="Apacer AST280",              capacity=256,  tbw=170,  price=1186),
    SSD(name="Apacer Panther AS350",       capacity=1000, tbw=600,  price=3438),
    SSD(name="Corsair MP600 Force",        capacity=1000, tbw=1800, price=5270),
    SSD(name="Gigabyte AORUS Gen4 7000s",  capacity=1000, tbw=700,  price=5571),
    SSD(name="GOODRAM CL100",              capacity=120,  tbw=90,   price=642),
    SSD(name="Intel 660p",                 capacity=2048, tbw=400,  price=8190),
    SSD(name="Kingston KC600",             capacity=256,  tbw=150,  price=1719),
    SSD(name="Kingston NV1",               capacity=500,  tbw=150,  price=1869),
    SSD(name="Patriot Memory Burst Elite", capacity=120,  tbw=50,   price=569),
    SSD(name="Samsung 980 PRO",            capacity=1000, tbw=600,  price=5705),
    SSD(name="WD Blue SSD",                capacity=250,  tbw=100,  price=1818),
)
# fmt: on


def count_diffs(
    a: Any,
    b: Any,
    to_min: list[str],
    to_max: list[str],
) -> tuple[int, int]:
    n_better: int = 0
    n_worse: int = 0

    for f in to_min:
        n_better += a[f] < b[f]
        n_worse += a[f] > b[f]

    for f in to_max:
        n_better += a[f] > b[f]
        n_worse += a[f] < b[f]

    return n_better, n_worse


def find_skyline_bnl(
    df: pd.DataFrame,
    to_min: list[str],
    to_max: list[str],
) -> pd.Series:
    """https://maxhalford.github.io/blog/skyline-queries"""

    rows: dict[Hashable, Any] = df.to_dict(orient="index")
    skyline: set[int] = {df.index[0]}

    for i in df.index[1:]:
        to_drop: set[int] = set()
        is_dominated: bool = False
        for j in skyline:
            n_better, n_worse = count_diffs(rows[i], rows[j], to_min, to_max)

            if n_worse > 0 and n_better == 0:
                is_dominated = True
                break

            if n_better > 0 and n_worse == 0:
                to_drop.add(j)

        if is_dominated:
            continue

        skyline = skyline.difference(to_drop)
        skyline.add(i)

    return pd.Series(df.index.isin(skyline), index=df.index)


def plot(
    df: pd.DataFrame,
    ax: plt.Axes,
    labels: list[str],
    title: str,
    check: str,
) -> None:
    if not SHOW_PLOTS:
        return

    for _, row in df.iterrows():
        color = "red" if row[check] else "blue"
        ax.scatter(*row[labels], c=color)
        ax.text(*row[labels], row[title])

    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])


def sort(df: pd.DataFrame, to_min: list[str], to_max: list[str]) -> pd.DataFrame:
    order: list[bool] = [False for _ in to_max] + [True for _ in to_min]
    return df.sort_values(
        by=to_max + to_min,
        ascending=order,
    )


def main() -> None:
    df0: pd.DataFrame = pd.DataFrame(CPUs)
    to_min0: list[str] = []
    to_max0: list[str] = ["cores", "frequency", "threads"]
    skyline0: pd.Series = find_skyline_bnl(df0, to_min0, to_max0)
    df0["isOptimal"] = skyline0.to_frame()
    print(sort(df0, to_min0, to_max0))

    df1: pd.DataFrame = pd.DataFrame(SSDs)
    to_min1: list[str] = ["price"]
    to_max1: list[str] = ["capacity", "tbw"]
    skyline1: pd.Series = find_skyline_bnl(df1, to_min1, to_max1)
    df1["isOptimal"] = skyline1.to_frame()
    print(sort(df1, to_min1, to_max1))

    fig: plt.Figure = plt.figure()
    ax0: plt.Axes = fig.add_subplot(121, projection=Axes3D.name)
    ax1: plt.Axes = fig.add_subplot(122, projection=Axes3D.name)

    plot(
        df=df0,
        ax=ax0,
        labels=to_max0 + to_min0,
        title="name",
        check="isOptimal",
    )

    plot(
        df=df1,
        ax=ax1,
        labels=to_max1 + to_min1,
        title="name",
        check="isOptimal",
    )

    plt.show()


if __name__ == "__main__":
    main()
