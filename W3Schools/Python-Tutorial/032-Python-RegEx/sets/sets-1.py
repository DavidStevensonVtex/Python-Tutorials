import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# $ python3 sets-1.py 
# ['r', 'a', 'n', 'n', 'a', 'n']
# Yes, there is at least one match!