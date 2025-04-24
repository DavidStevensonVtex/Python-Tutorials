from typing import Any


def double(x: int) -> int:
    return x + x


def myprint(*args: Any, end: str = " ") -> None:
    for arg in args:
        print(arg, end=" ")
    print()


myprint("The", "rain", "in", "Spain", "falls", "mainly", "in", "the", "plain")
