# String format()

# Before Python 3.6 we used the format() method to format strings.

# The format() method can still be used, but f-strings are faster and the preferred way to format strings.

# The next examples in this page demonstrates how to format strings with the format() method.

# The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:

# Example
# Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# $ python3 format-method.py 
# The price is 49 dollars