from typing import Dict


def print_salaries(employees: Dict[str, int]) -> None:
    for name, salary in employees.items():
        print(f"{name} has salary of ${salary}")


print_salaries({"alice": 420, "bob": 420})

# $ python dict-1.py
# alice has salary of $420
# bob has salary of $420

# $ pyright dict-1.py
# 0 errors, 0 warnings, 0 informations

# $ mypy dict-1.py
# Success: no issues found in 1 source file
