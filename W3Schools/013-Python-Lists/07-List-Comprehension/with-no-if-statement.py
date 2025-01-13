# The condition if x != "apple"  will return True for all elements other than "apple", 
# making the new list contain all fruits except "apple".

# The condition is optional and can be omitted:

# Example
# With no if statement:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

# $ python3 with-no-if-statement.py 
# ['apple', 'banana', 'cherry', 'kiwi', 'mango']