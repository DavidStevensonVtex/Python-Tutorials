import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

# $ python3 metacharacters-02.py
# ['5', '9']
