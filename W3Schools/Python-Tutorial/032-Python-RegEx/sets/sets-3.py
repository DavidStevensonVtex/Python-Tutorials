import re

txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# $ python3 sets-3.py 
# ['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']
# Yes, there is at least one match!