# Get Values
# The values() method will return a list of all the values in the dictionary.

# Example
# Get a list of the values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print("x", x)

# The list of the values is a view of the dictionary, meaning that any 
# changes done to the dictionary will be reflected in the values list.

# $ python3 get-values.py 
# x dict_values(['Ford', 'Mustang', 1964])