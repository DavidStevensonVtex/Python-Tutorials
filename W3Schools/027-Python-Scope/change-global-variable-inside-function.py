# Example

# To change the value of a global variable inside a function, refer to the variable 
# by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()
print(x)

# $ python3 change-global-variable-inside-function.py 
# 200