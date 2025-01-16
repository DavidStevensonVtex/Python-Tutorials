# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Example
# Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# $ python3 else-in-for-loop-with-break.py 
# 0
# 1
# 2