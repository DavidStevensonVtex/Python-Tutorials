# Example
# To change the value of a global variable inside a function, refer to the variable 
# by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# $ python3 global-keyword-2.py
# Python is fantastic