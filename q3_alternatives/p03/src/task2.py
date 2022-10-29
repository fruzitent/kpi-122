import operator
from dataclasses import dataclass
from itertools import combinations
from pprint import pprint
from typing import Callable, Hashable, Protocol

import numpy as np
import pandas as pd

pd.set_option("display.expand_frame_repr", 0)


class Comparable(Protocol):  # noqa: H601 class has low (0.00%) cohesion
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __gt__(self, other: object) -> bool:
        raise NotImplementedError

    def __lt__(self, other: object) -> bool:
        raise NotImplementedError


@dataclass(frozen=True)
class Op(object):
    callback: Callable[[Comparable, Comparable], bool]
    score: float
    view: str

    def __repr__(self) -> str:
        return self.view


GT: Op = Op(callback=operator.gt, view=">", score=1)
EQ: Op = Op(callback=operator.eq, view="=", score=0.5)
LT: Op = Op(callback=operator.lt, view="<", score=0)
OPS: tuple[Op, ...] = GT, EQ, LT
str2op: dict[str, Op] = {op.view: op for op in OPS}


@dataclass(frozen=True)
class Pair(object):
    op: Op
    src: Hashable
    dst: Hashable

    def __repr__(self) -> str:
        return f"{self.src} {self.op} {self.dst}"


def rank(alternatives: list[str]) -> list[Pair]:
    pairs: list[Pair] = []

    for src, dst in combinations(alternatives, 2):
        op: str = input(f"{src} vs {dst}?\n")
        if op not in str2op.keys():
            raise ValueError(f"Unexpected op '{op}'")
        pairs.append(Pair(src=src, dst=dst, op=str2op[op]))

    return pairs


def fill(df: pd.DataFrame, pairs: list[Pair]) -> None:
    for pair in pairs:
        if pair.op is GT:
            df.loc[pair.src, pair.dst] = GT.score
            df.loc[pair.dst, pair.src] = LT.score
        elif pair.op is EQ:
            df.loc[pair.src, pair.dst] = EQ.score
            df.loc[pair.dst, pair.src] = EQ.score
        elif pair.op is LT:
            df.loc[pair.src, pair.dst] = LT.score
            df.loc[pair.dst, pair.src] = GT.score
        else:
            raise ValueError(f"Unexpected op '{pair.op}'")


# TODO(p03): add transitivity and priority violation checks
def main() -> None:
    alternatives: list[str] = [
        "AeroVironment RQ-20 Puma",
        "Baykar Bayraktar TB2",
        "UA Dynamics Punisher",
        "UkrSpecSystems PD-2",
        "WB Electronics FlyEye",
    ]

    # pairs: list[Pair] = rank(alternatives)
    pairs: list[Pair] = [
        Pair(op=LT, src="AeroVironment RQ-20 Puma", dst="Baykar Bayraktar TB2"),
        Pair(op=GT, src="AeroVironment RQ-20 Puma", dst="UA Dynamics Punisher"),
        Pair(op=LT, src="AeroVironment RQ-20 Puma", dst="UkrSpecSystems PD-2"),
        Pair(op=LT, src="AeroVironment RQ-20 Puma", dst="WB Electronics FlyEye"),
        Pair(op=GT, src="Baykar Bayraktar TB2", dst="UA Dynamics Punisher"),
        Pair(op=GT, src="Baykar Bayraktar TB2", dst="UkrSpecSystems PD-2"),
        Pair(op=GT, src="Baykar Bayraktar TB2", dst="WB Electronics FlyEye"),
        Pair(op=LT, src="UA Dynamics Punisher", dst="UkrSpecSystems PD-2"),
        Pair(op=LT, src="UA Dynamics Punisher", dst="WB Electronics FlyEye"),
        Pair(op=EQ, src="UkrSpecSystems PD-2", dst="WB Electronics FlyEye"),
    ]
    pprint(pairs)

    df: pd.DataFrame = pd.DataFrame(
        columns=alternatives,
        index=alternatives,
        data=[],
        dtype=np.float64,
    )

    fill(df, pairs)
    df["Ranking"] = df.sum(axis=1)
    df.sort_values(by="Ranking", ascending=False, inplace=True)
    print(df)


if __name__ == "__main__":
    main()
