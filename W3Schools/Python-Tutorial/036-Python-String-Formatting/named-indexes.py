# Named Indexes

# You can also use named indexes by entering a name inside the curly brackets {carname}, 
# but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

# Example

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# $ python3 named-indexes.py 
# I have a Ford, it is a Mustang.