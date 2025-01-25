# If no matches are found, the value None is returned:

# Example

# Make a search that returns no match:

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

