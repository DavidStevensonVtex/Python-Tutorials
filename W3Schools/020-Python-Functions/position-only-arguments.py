# Positional-Only Arguments

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

# To specify that a function can have only positional arguments, add , / after the arguments:

# Example
def my_function(x, /):
  print(x)

my_function(3)

# $ python3 position-only-arguments.py 
# 3