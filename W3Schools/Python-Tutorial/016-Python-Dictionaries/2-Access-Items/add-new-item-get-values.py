# Example
# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# $ python3 add-new-item-get-values.py 
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 2020])