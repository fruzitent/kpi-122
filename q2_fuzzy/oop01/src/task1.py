from dataclasses import dataclass


@dataclass
class Vegetable(object):
    name: str
    price: float
    weight: float
    _kind: str = "vegetable"

    def __str__(self) -> str:
        lines: list[str] = [
            f"[{self._kind}] : [{self.__class__._kind}] : <{self.name}>",
            f"  price:  {self.price}",
            f"  weight: {self.weight}",
            f"  total:  {self.total}",
        ]
        return "\n".join(lines)

    @property
    def total(self) -> float:
        return self.price * self.weight


@dataclass
class Bulbous(Vegetable):
    _kind = "bulbous"


@dataclass
class Cabbage(Vegetable):
    _kind = "cabbage"


@dataclass
class Leafy(Vegetable):
    _kind = "leafy"


@dataclass
class Legumes(Vegetable):
    _kind = "legumes"


@dataclass
class Nightshade(Vegetable):
    _kind = "nightshade"


@dataclass
class Pumpkin(Vegetable):
    _kind = "pumpkin"


@dataclass
class Roots(Vegetable):
    _kind = "roots"


@dataclass
class Tubers(Vegetable):
    _kind = "tubers"


VEGETABLES = (
    Bulbous,
    Cabbage,
    Leafy,
    Legumes,
    Nightshade,
    Pumpkin,
    Roots,
    Tubers,
)


def get_vegetable() -> Vegetable:
    while True:
        idx: int = int(input("class id: "))
        if idx in range(len(VEGETABLES) - 1):
            break
    name: str = input("name: ")
    price: float = float(input("price: "))
    weight: float = float(input("weight: "))
    return VEGETABLES[idx](name, price, weight)


def main() -> None:
    for itr, vegetable in enumerate(VEGETABLES):
        print(itr, vegetable.__name__)

    veg: Vegetable = get_vegetable()
    print(veg)


if __name__ == "__main__":
    main()
