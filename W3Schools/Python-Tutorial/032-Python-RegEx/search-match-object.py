# Match Object

# A Match Object is an object containing information about the search and the result.

# Note: If there is no match, the value None will be returned, instead of the Match Object.

# Example

# Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

