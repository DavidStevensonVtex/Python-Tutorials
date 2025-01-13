# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

# Example
# Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i, thislist[i])

# $ python3 loop-through-the-index-numbers.py 
# 0 apple
# 1 banana
# 2 cherry