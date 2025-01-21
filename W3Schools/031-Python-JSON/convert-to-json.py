# Example
# Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# $ python3 convert-to-json.py 
# {"name": "John", "age": 30}
# ["apple", "bananas"]
# ["apple", "bananas"]
# "hello"
# 42
# 31.76
# true
# false
# null