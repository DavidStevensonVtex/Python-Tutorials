# Or you can use the extend() method, where the purpose is to add elements 
# from one list to another list:

# Example
# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# $ python3 use-the-extend-method.py 
# ['a', 'b', 'c', 1, 2, 3]