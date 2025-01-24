# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# Example
# Set the values in the new list to upper case:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# $ python3 using-expression.py 
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']