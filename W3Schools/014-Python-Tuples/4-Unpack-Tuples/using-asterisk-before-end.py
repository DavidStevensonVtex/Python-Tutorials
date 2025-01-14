# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

# Example
# Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# $ python3 using-asterisk-before-end.py 
# apple
# ['mango', 'papaya', 'pineapple']
# cherry