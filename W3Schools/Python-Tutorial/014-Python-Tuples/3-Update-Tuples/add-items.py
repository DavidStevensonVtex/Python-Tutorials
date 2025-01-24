# Add Items
# Since tuples are immutable, they do not have a built-in append() method, 
# but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple, 
# you can convert it into a list, add your item(s), and convert it back 
# into a tuple.

# Example
# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# $ python3 add-items.py
# ('apple', 'banana', 'cherry', 'orange')