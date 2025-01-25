# You can perform if...else statements inside the placeholders:

# Example

# Return "Expensive" if the price is over 50, otherwise return "Cheap":

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

# $ python3 format-with-ternary.py 
# It is very Cheap