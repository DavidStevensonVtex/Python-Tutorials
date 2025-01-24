# Loop Through a Dictionary

# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Print all key names in the dictionary, one by one:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

# $ python3 loop-thru-a-dictionary.py 
# brand
# model
# year