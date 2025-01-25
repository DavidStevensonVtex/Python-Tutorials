# More Modifiers

# At the beginning of this chapter we explained how to use the .2f modifier to format a 
# number into a fixed point number with 2 decimals.

# There are several other modifiers that can be used to format values:

# Example

# Use a comma as a thousand separator:

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# $ python3 use-comma-as-thousands-separator.py 
# The price is 59,000 dollars