from dataclasses import dataclass


@dataclass
class City(object):
    name: str = "city"

    def __str__(self) -> str:
        lines: list[str] = []
        for ist in self.__class__.mro()[-2::-1]:
            mro: int = len(ist.mro()) - 2
            padding: str = "".join(["  " for _ in range(mro)])
            lines.append(padding + ist.name)  # type: ignore
        return "\n".join(lines)


@dataclass
class Strasbourg(City):
    name: str = "Strasbourg"


@dataclass
class Toulouse(City):
    name: str = "Toulouse"


@dataclass
class Marseille(City):
    name: str = "Marseille"


@dataclass
class Birmingham(City):
    name: str = "Birmingham"


@dataclass
class Manchester(City):
    name: str = "Manchester"


@dataclass
class Canberra(City):
    name: str = "Canberra"


@dataclass
class Sydney(City):
    name: str = "Sydney"


@dataclass
class Melbourne(City):
    name: str = "Melbourne"


@dataclass
class France(Strasbourg, Toulouse, Marseille):
    name: str = "France"


@dataclass
class Britain(Birmingham, Manchester):
    name: str = "Britain"


@dataclass
class Australia(Canberra, Sydney, Melbourne):
    name: str = "Australia"


@dataclass
class Europe(France, Britain):
    name: str = "Europe"


def main() -> None:
    europe = Europe()
    print(europe)

    australia = Australia()
    print(australia)


if __name__ == "__main__":
    main()
