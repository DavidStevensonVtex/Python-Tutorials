from typing import Union


def triple(string: Union[str, bytes]) -> Union[str, bytes]:
    return string * 3


scream = triple("A")
# Operator "+" not supported for types "str | bytes" and "Literal['!']"
#   Operator "+" not supported for types "bytes" and "Literal['!']"Pylance
scream_with_exlamation = triple("A") + "!"
