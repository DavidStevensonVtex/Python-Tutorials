# Using a While Loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

# Example
# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(i, thislist[i])
  i = i + 1

# $ python3 using-a-while-loop.py 
# 0 apple
# 1 banana
# 2 cherry