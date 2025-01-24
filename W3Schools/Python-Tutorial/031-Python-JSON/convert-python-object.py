# When you convert from Python to JSON, Python objects are converted 
# into the JSON (JavaScript) equivalent:

# Python	JSON
# * dict	Object
# * list	Array
# * tuple	Array
# * str	String
# * int	Number
# * float	Number
# * True	true
# * False	false
# * None	null

# Example
# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# $ python3 convert-python-object.py 
# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
