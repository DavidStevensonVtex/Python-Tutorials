# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# Condition
# The condition is like a filter that only accepts the items that valuate to True.

# Example
# Only accept items that are not "apple":

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# $ python3 the-syntax.py 
# ['banana', 'cherry', 'kiwi', 'mango']