# Raise an exception

# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.

# Example

# Raise an error and stop the program if x is lower than 0:

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# $ python3 raise-an-exception.py 
# Traceback (most recent call last):
#   File "raise-an-exception.py", line 14, in <module>
#     raise Exception("Sorry, no numbers below zero")
# Exception: Sorry, no numbers below zero