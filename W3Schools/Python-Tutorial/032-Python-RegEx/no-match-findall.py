# The list contains the matches in the order they are found.

# If no matches are found, an empty list is returned:

# Example

# Return an empty list if no match was found:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

if x:
    print("Portugal was found")
else:
    print("Portugal was NOT FOUND")

# $ python3 no-match-findall.py 
# []
# Portugal was NOT FOUND