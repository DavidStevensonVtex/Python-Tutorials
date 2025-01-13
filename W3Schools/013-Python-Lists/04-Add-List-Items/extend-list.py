# Extend List
# To append elements from another list to the current list, use the extend() method.

# Example
# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# $ python3 extend-list.py 
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']