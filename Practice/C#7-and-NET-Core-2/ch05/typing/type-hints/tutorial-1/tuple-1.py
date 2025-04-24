from typing import Tuple


def print_salary_entry(entry: Tuple[str, int]) -> None:
    name, salary = entry
    print(f"Salary of {name}: {salary}")


print_salary_entry(("Joe Q. Employee", 123456))

# $ python tuple-1.py
# Salary of Joe Q. Employee: 123456
# $ pyright tuple-1.py
# 0 errors, 0 warnings, 0 informations
# $ mypy tuple-1.py
# Success: no issues found in 1 source file
