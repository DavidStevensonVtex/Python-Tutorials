from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def remove_falsey_from_list(items: list[T]) -> list[T]:
    return [item for item in items if item]


def remove_falsey(items: Iterable[T]) -> Iterator[T]:
    for item in items:
        if item:
            yield item


# $ mypy remove-falsey.py
# Success: no issues found in 1 source file

# $ pyright remove-falsey.py
# 0 errors, 0 warnings, 0 informations
