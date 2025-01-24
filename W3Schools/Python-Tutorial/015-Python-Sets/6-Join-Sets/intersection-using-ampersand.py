# You can use the & operator instead of the intersection() method, 
# and you will get the same result.

# Example
# Use & to join two sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# Note: The & operator only allows you to join sets with sets, and not with other 
# data types like you can with the intersection() method.

# $ python3 intersection-using-ampersand.py 
# {'apple'}