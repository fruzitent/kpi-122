"""
Task 1.

The horse is on column zero.
What is the number of ways the horse has, to get to the column with index N,
if it can jump from 1 to k columns forward?
"""

from math import ceil
from random import SystemRandom


def main() -> None:
    rand: int = ceil(SystemRandom().random() * 10)
    dest: int = SystemRandom().randrange(rand)
    line: list[int] = [1 for _ in range(rand)]
    pos: int = 0


if __name__ == "__main__":
    main()
