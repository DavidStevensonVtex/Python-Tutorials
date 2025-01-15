# Example
# The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# $ python3 del-dictionary.py 
# Traceback (most recent call last):
#   File "del-dictionary.py", line 10, in <module>
#     print(thisdict) #this will cause an error because "thisdict" no longer exists.
# NameError: name 'thisdict' is not defined