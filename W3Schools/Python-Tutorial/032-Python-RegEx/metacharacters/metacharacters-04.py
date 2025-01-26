import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
print(x)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

# $ python3 metacharacters-04.py
# ['hello']
# Yes, the string starts with 'hello'