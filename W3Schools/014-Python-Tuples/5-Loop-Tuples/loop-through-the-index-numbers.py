# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

# Example
# Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# $ python3 loop-through-the-index-numbers.py 
# apple
# banana
# cherry