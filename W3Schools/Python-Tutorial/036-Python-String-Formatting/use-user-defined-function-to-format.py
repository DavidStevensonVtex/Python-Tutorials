# The function does not have to be a built-in Python method, you can create 
# your own functions and use them:

# Example

# Create a function that converts feet into meters:

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# $ python3 use-user-defined-function-to-format.py 
# The plane is flying at a 9144.0 meter altitude