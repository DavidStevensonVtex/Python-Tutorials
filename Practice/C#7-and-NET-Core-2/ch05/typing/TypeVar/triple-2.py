from typing import TypeVar

AnyString = TypeVar("AnyString")


def triple(string: AnyString) -> AnyString:
    # Operator "*" not supported for types "AnyString@triple" and "Literal[3]"Pylance
    return string * 3
