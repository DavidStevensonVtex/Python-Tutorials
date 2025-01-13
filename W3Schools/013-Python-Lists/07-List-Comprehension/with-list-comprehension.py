# With list comprehension you can do all that with only one line of code:

# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# $ python3 with-list-comprehension.py 
# ['apple', 'banana', 'mango']