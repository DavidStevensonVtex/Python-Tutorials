# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

# Example
# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# $ python3 True-and-1-are-the-same-value.py 
# {True, 2, 'banana', 'apple', 'cherry'}