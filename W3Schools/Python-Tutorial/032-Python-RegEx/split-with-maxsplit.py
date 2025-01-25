# You can control the number of occurrences by specifying the maxsplit parameter:

# Example

# Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# $ python3 split-with-maxsplit.py 
# ['The', 'rain in Spain']