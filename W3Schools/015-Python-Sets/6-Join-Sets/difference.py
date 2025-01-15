# Difference
# The difference() method will return a new set that will contain only the items 
# from the first set that are not present in the other set.

# Example
# Keep all items from set1 that are not in set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

# $ python3 difference.py 
# {'cherry', 'banana'}