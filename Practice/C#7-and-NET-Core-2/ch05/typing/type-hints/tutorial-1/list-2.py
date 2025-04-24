from typing import List


def zip_add(list1: List[int], list2: List[int]) -> List[int]:
    if len(list1) != len(list2):
        raise ValueError("Expected lists of the same length")

    return [a + b for a, b in zip(list1, list2)]


print(zip_add([1, 2, 3], [4, 5, 6]))


print(zip_add([1, 2, 3], [4, 5, "ghi"]))

# $ pyright list-2.py
# d:\drs\Python\GitHub\Python-Tutorials\Practice\C#7-and-NET-Core-2\ch05\typing\type-hints\tutorial-1\list-2.py
#   d:\drs\Python\GitHub\Python-Tutorials\Practice\C#7-and-NET-Core-2\ch05\typing\type-hints\tutorial-1\list-2.py:14:33 - error: Argument of type "list[int | str]" cannot be assigned to parameter "list2" of type "List[int]" in function "zip_add"
#     "Literal['ghi']" is not assignable to "int" (reportArgumentType)
# 1 error, 0 warnings, 0 informations

# $ mypy list-2.py
# list-2.py:14: error: List item 2 has incompatible type "str"; expected "int"  [list-item]
# Found 1 error in 1 file (checked 1 source file)
