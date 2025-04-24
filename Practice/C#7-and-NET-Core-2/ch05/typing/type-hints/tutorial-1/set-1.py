from typing import Set


def extract_bits(numbers: Set[int]) -> Set[int]:
    return numbers & {0, 1}


print(extract_bits({0, 1, 2, 3, 4, 5}))

# $ python set-1.py
# {0, 1}

# $ pyright set-1.py
# 0 errors, 0 warnings, 0 informations
# $ mypy set-1.py
# Success: no issues found in 1 source file
