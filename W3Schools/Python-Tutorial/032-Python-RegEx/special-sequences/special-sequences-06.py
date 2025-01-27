import re

txt = "The rain 123 in Spain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# $ python3 special-sequences-06.py 
# ['1', '2', '3']
# Yes, there is at least one match!