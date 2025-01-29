# By calling readline() two times, you can read the two first lines:

# Example
# Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# $ python3 read-lines-2.py 
# Hello! Welcome to demofile.txt
#
# This file is for testing purposes.
#