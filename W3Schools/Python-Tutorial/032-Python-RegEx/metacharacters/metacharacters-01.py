import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

# $ python3 metacharacters-01.py
# ['h', 'e', 'a', 'i', 'i', 'a', 'i']