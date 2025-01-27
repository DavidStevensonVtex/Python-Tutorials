import re

txt = "The rain in Spain"

#Return a match at every non-digit character:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# $ python3 special-sequences-07.py 
# ['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']
# Yes, there is at least one match!