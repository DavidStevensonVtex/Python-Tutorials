# Even strings are iterable objects, and can return an iterator:

# Example

# Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# $ python3 strings.py
# b
# a
# n
# a
# n
# a