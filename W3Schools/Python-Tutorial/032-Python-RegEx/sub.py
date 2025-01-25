# The sub() Function

# The sub() function replaces the matches with the text of your choice:

# Example

# Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# $ python3 sub.py 
# The9rain9in9Spain