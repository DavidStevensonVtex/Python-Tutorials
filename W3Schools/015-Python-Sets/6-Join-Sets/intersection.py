# Intersection

# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains the items
# that are present in both sets.

# Example
# Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# $ python3 intersection.py 
# {'apple'}