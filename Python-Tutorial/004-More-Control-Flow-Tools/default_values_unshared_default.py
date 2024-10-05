# If you don’t want the default to be shared between subsequent calls,
# you can write the function like this instead:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

# Results
# [1]
# [2]
# [3]
