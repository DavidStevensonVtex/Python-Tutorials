# Keyword-Only Arguments

# To specify that a function can have only keyword arguments, add *, before the arguments:

# Example

def my_function(*, x):
  print(x)

my_function(x = 3)

# $ python3 keyword-only-arguments.py 
# 3