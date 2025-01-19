# Global Scope

# A variable created in the main body of the Python code is a global variable and 
# belongs to the global scope.

# Global variables are available from within any scope, global and local.

# Example

# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()
print(x)

# $ python3 global-scope.py 
# 300
# 300