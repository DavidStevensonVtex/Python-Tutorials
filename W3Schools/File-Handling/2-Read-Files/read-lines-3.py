# By looping through the lines of the file, you can read the whole file, line by line:

# Example
# Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  x = x.strip()
  print(x)

# $ python3 read-lines-3.py 
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!