# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Example
# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# $ python3 add-any-iterable.py 
# ['apple', 'banana', 'cherry', 'kiwi', 'orange']