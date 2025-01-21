# Order the Result

# The json.dumps() method has parameters to order the keys in the result:

# Example

# Use the sort_keys parameter to specify if the result should be sorted or not:

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

s = json.dumps(x, indent=4, sort_keys=True)
print(s)

# $ python3 order-the-result.py 
# {
#     "age": 30,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ],
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "divorced": false,
#     "married": true,
#     "name": "John",
#     "pets": null
# }