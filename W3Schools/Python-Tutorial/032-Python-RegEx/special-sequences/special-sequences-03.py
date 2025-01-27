import re

txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# $ python3 special-sequences-03.py
# ['ain', 'ain']
# Yes, there is at least one match!