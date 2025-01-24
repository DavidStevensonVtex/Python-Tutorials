# The range() function defaults to 0 as a starting value, however it is possible to specify 
# the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 
# (but not including 6):

# Example
# Using the start parameter:

for x in range(2, 6):
  print(x)

# $ python3 range-start.py 
# 2
# 3
# 4
# 5