# Example

# Print the string passed into the function:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# $ python3 search-match-string.py 
# The rain in Spain