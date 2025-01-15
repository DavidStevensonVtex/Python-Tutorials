# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.

# The result will be a set.

# Example
# Join a set with a tuple:

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# $ python3 join-a-set-and-a-tuple.py 
# {1, 2, 'c', 3, 'b', 'a'}