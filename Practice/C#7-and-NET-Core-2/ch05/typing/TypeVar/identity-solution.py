from typing import TypeVar

T = TypeVar("T")


def identity(arg: T) -> T:
    return arg


number = identity(42)
# Operator "+" not supported for types "int" and "Literal['!']"Pylance
print(number + "!")

# $ mypy identity-solution.py
# identity-solution.py:12: error: Unsupported operand types for + ("int" and "str")  [operator]
# Found 1 error in 1 file (checked 1 source file)

# $ pyright identity-solution.py
# d:\drs\Python\GitHub\Python-Tutorials\Practice\C#7-and-NET-Core-2\ch05\typing\TypeVar\identity-solution.py
#   d:\drs\Python\GitHub\Python-Tutorials\Practice\C#7-and-NET-Core-2\ch05\typing\TypeVar\identity-solution.py:12:7 - error: Operator "+" not supported for types "int" and "Literal['!']" (reportOperatorIssue)
# 1 error, 0 warnings, 0 informations
