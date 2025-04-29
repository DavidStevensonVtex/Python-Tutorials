from typing import TypeVar

AnyString = TypeVar("AnyString", str, bytes)


def triple(string: AnyString) -> AnyString:
    return string * 3


unicode_scream = triple("A") + "!"
bytes_scream = triple(b"A") + b"!"

# $ mypy triple-3.py
# Success: no issues found in 1 source file

# $ pyright triple-3.py
# 0 errors, 0 warnings, 0 informations
