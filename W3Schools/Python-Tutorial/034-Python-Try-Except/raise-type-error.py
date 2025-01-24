# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.

# Example
# Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

# $ python3 raise-type-error.py 
# Traceback (most recent call last):
#   File "raise-type-error.py", line 11, in <module>
#     raise TypeError("Only integers are allowed")
# TypeError: Only integers are allowed