# Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple.

# Example
# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# <class 'tuple'>
# <class 'str'>