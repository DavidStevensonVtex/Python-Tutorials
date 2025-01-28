import re

txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# $ python3 sets-2.py 
# ['h', 'e', 'a', 'i', 'n', 'i', 'n', 'a', 'i', 'n']
# Yes, there is at least one match!