def double(x: int) -> int:
    return x + "FizzBuzz"  # error!


# $ mypy double-type-hint-error.py
# double-type-hint-error.py:2: error: Unsupported operand types for + ("int" and "str")  [operator]
# Found 1 error in 1 file (checked 1 source file)
