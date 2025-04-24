from typing import Tuple, Optional


def print_salary_entry(entry: Tuple[str, Optional[int]]) -> None:
    name, salary = entry
    if salary is None:
        print(f"{name} is a volunteer")
    else:
        print(f"Salary of {name}: {salary}")


print_salary_entry(("Joe Q. Employee", 123456))
print_salary_entry(("Joe Q. Employee", None))

# $ python tuple-2.py
# Salary of Joe Q. Employee: 123456
# Joe Q. Employee is a volunteer
# $ pyright tuple-2.py
# 0 errors, 0 warnings, 0 informations
# $ mypy tuple-2.py
# Success: no issues found in 1 source file
