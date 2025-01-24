# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

# Example
# Get a list of the keys:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print("x", x)

# The list of the keys is a view of the dictionary, meaning that any changes 
# done to the dictionary will be reflected in the keys list.

# $ python3 get-keys.py 
# x dict_keys(['brand', 'model', 'year'])