
#   Example
# Print all values in the dictionary, one by one:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

# Example
# You can also use the values() method to return values of a dictionary:
print()
for x in thisdict.values():
  print(x)

# $ python3 loop-thru-values.py 
# Ford
# Mustang
# 1964

# Ford
# Mustang
# 1964