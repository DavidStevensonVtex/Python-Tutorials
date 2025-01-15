# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

# Example
# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# $ python3 False-and-0-are-the-same-value.py 
# {False, True, 'banana', 'apple', 'cherry'}