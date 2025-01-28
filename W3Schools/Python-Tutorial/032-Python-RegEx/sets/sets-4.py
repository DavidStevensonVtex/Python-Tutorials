import re

txt = "The rain 0123456789 in Spain"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# $ python3 sets-4.py 
# ['0', '1', '2', '3']
# Yes, there is at least one match!