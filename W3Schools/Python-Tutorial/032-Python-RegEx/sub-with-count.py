# You can control the number of replacements by specifying the count parameter:

# Example

# Replace the first 2 occurrences:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# $ python3 sub-with-count.py 
# The9rain9in Spain