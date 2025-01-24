# There is also a method called get() that will give you the same result:

# Example
# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print("x", x)

# $ python3 access-items-using-get.py 
# x Mustang