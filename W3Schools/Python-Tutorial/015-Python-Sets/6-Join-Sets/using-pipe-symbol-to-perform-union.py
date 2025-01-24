# You can use the | operator instead of the union() method, and you will get the same result.

# Example
# Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# $ python3 using-pipe-symbol-to-perform-union.py 
# {1, 2, 3, 'c', 'b', 'a'}