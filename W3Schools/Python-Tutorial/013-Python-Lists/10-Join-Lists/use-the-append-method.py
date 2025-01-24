# Another way to join two lists is by appending all the items from 
# list2 into list1, one by one:

# Example
# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# $ python3 use-the-append-method.py 
# ['a', 'b', 'c', 1, 2, 3]