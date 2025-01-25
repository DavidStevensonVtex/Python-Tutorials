# The split() Function

# The split() function returns a list where the string has been split at each match:

# Example

# Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# $ python3 split.py 
# ['The', 'rain', 'in', 'Spain']