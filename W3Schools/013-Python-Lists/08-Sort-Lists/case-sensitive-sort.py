# Case Insensitive Sort

# By default the sort() method is case sensitive, resulting in all capital letters 
# being sorted before lower case letters:

# Example
# Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# $ python3 case-sensitive-sort.py 
# ['Kiwi', 'Orange', 'banana', 'cherry']