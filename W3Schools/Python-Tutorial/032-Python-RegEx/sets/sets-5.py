import re

txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# $  python3 sets-5.py 
# ['8', '1', '1', '4', '5']
# Yes, there is at least one match!