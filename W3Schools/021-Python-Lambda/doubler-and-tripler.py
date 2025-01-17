# Or, use the same function definition to make both functions, in the same program:

# Example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# $ python3 why-use-lambda-functions.py 
# 22