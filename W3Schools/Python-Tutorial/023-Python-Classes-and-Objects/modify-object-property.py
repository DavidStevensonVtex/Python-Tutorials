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

# Modify Object Properties
# You can modify properties on objects like this:

# Example
# Set the age of p1 to 40:

p1.age = 40
print(p1.name, p1.age)

# $ python3 modify-object-property.py 
# John 40