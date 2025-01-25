# Example

# Print the part of the string where there was a match.

# The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# $ python3 search-match-group.py 
# Spain