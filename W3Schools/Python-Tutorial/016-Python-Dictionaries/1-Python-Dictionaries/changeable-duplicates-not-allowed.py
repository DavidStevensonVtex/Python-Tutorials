# Ordered or Unordered?

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and 
# earlier, dictionaries are unordered.

# When we say that dictionaries are ordered, it means that the items have a 
# defined order, and that order will not change.

# Unordered means that the items do not have a defined order, you cannot refer 
# to an item by using an index.

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items 
# after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# Example
# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# $ python3 changeable-duplicates-not-allowed.py 
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}