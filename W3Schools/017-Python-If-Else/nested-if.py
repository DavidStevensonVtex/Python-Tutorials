# Nested If
# You can have if statements inside if statements, this is called nested if statements.

# Example
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# $ python3 nested-if.py 
# Above ten,
# and also above 20!
