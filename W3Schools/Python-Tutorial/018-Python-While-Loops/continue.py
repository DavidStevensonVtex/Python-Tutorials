# The continue Statement

# With the continue statement we can stop the current iteration, and continue with the next:

# Example
# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# $ python3 continue.py 
# 1
# 2
# 4
# 5
# 6