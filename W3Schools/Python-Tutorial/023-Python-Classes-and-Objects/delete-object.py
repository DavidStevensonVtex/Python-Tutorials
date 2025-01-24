# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# The self Parameter

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Example
# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)

# Delete Objects
# You can delete objects by using the del keyword:

# Example
# Delete the p1 object:

del p1
print(p1)

# $ python3 delete-object.py 
# Traceback (most recent call last):
#   File "delete-object.py", line 29, in <module>
#     print(p1)
# NameError: name 'p1' is not defined