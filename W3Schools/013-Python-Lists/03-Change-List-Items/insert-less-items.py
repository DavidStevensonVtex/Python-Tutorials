# If you insert less items than you replace, the new items will be inserted where you specified, 
# and the remaining items will move accordingly:

# Example
# Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# $ python3 insert-less-items.py 
# ['apple', 'watermelon']