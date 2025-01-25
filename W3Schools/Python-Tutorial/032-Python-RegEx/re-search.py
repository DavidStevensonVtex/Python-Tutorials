# Python RegEx

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module

# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:

# import re

# RegEx in Python

# When you have imported the re module, you can start using regular expressions:

# Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x.span(), x.group(0))

# $ python3 re-search.py 
# (0, 17) The rain in Spain