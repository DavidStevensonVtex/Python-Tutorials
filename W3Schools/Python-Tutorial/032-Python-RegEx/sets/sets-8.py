import re

txt = "8 times before 11:45 AM 1+2+3"

#Check if the string has any + characters:

x = re.findall("[+]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# $ python3 sets-8.py 
# ['+', '+']
# Yes, there is at least one match!