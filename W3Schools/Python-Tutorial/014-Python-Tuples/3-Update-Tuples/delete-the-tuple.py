# Or you can delete the tuple completely:

# Example
# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# $ python3 delete-the-tuple.py 
# Traceback (most recent call last):
#   File "delete-the-tuple.py", line 8, in <module>
#     print(thistuple) #this will raise an error because the tuple no longer exists
# NameError: name 'thistuple' is not defined