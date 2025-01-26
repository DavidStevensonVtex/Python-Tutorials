import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
print(x)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

# $ python3 metacharacters-05.py
# ['planet']
# Yes, the string ends with 'planet'