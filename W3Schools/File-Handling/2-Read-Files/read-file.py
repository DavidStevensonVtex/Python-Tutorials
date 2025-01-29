# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")
print(f.read())

# $ python3 read-file.py 
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!