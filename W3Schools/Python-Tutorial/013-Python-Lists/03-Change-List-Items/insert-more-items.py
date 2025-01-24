# If you insert more items than you replace, the new items will be inserted where you specified, 
# and the remaining items will move accordingly:

# Example
# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# $ python3 insert-more-items.py 
# ['apple', 'blackcurrant', 'watermelon', 'cherry']

