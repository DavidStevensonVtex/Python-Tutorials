# The break Statement

# With the break statement we can stop the loop even if the while condition is true:

# Example
# Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# $ python3 break.py 
# 1
# 2
# 3