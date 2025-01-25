# The findall() Function

# The findall() function returns a list containing all matches.

# Example

# Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# $ python3 findall.py 
# ['ai', 'ai']