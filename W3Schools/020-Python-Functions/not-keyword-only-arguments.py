# Without the *, you are allowed to use positionale arguments even if the 
# function expects keyword arguments:

# Example
def my_function(x):
  print(x)

my_function(3)
my_function(x = 5)

# $ python3 not-keyword-only-arguments.py 
# 3
# 5