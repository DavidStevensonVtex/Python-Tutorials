# Or, use the same function definition to make a function that always triples the number you send in:

# Example
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# $ python3 tripler.py 
# 33