# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

# Example
# Keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

# $ python3 symmetric-differences.py 
# {'banana', 'microsoft', 'cherry', 'google'}