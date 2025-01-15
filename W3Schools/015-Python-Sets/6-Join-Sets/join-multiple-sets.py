# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets.

# When using a method, just add more sets in the parentheses, separated by commas:

# Example
# Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

secondset = set1 | set2 | set3 | set4
print(secondset)

# $ python3 join-multiple-sets.py 
# {1, 2, 3, 'John', 'bananas', 'b', 'a', 'cherry', 'c', 'Elena', 'apple'}
# {1, 2, 3, 'John', 'bananas', 'b', 'a', 'cherry', 'c', 'Elena', 'apple'}