# Removing Items
# There are several methods to remove items from a dictionary:

# ExampleGet your own Python Server
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# $ python3 remove-items-using-pop.py 
# {'brand': 'Ford', 'year': 1964}