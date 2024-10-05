# Important warning: The default value is evaluated only once.
# This makes a difference when the default is a mutable object
# such as a list, dictionary, or instances of most classes.
# For example, the following function accumulates the arguments
# passed to it on subsequent calls:


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

# Results
# [1]
# [1, 2]
# [1, 2, 3]
