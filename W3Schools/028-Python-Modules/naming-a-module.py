# Naming a Module

# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module

# You can create an alias when you import a module, by using the as keyword:

# Example

# Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

# $ python3 naming-a-module.py 
# 36