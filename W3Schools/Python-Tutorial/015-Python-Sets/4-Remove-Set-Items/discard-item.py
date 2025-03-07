# Example
# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# $ python3 discard-item.py 
# {'apple', 'cherry'}

# Note: If the item to remove does not exist, discard() will NOT raise an error.