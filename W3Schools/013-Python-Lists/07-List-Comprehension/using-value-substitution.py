# Return "orange" instead of "banana":

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# $ python3 using-value-substitution.py 
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']