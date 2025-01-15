# Update
# The update() method inserts all items from one set into another.

# The update() changes the original set, and does not return a new set.

# Example
# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# $ python3 join-using-update-method.py 
# {1, 2, 3, 'b', 'c', 'a'}