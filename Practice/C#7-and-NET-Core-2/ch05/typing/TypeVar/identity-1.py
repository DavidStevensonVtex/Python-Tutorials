from typing import Any


def identity(arg: Any) -> Any:
    return arg


number = identity(42)
print(number + "!")

# $ python identity-1.py
# Traceback (most recent call last):
#   File "D:\drs\Python\GitHub\Python-Tutorials\Practice\C#7-and-NET-Core-2\ch05\typing\TypeVar\identity-1.py", line 9, in <module>
#     print(number + "!")
#           ~~~~~~~^~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
