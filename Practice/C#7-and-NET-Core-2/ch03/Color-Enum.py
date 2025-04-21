from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)        # Output: Color.RED
print(Color['RED'])      # Output: Color.RED
print(Color(1))          # Output: Color.RED

print(Color.RED.name)    # Output: RED
print(Color.RED.value)   # Output: 1

# $ python Color-Enum.py
# Color.RED
# Color.RED
# Color.RED
# RED
# 1