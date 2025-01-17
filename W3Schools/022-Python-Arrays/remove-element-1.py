# Removing Array Elements
# You can use the pop() method to remove an element from the array.

# Example
# Delete the second element of the cars array:

cars = ["Ford", "Volvo", "BMW"]
print("before pop", cars)
cars.pop(1)
print("after pop(1)", cars)

# $ python3 remove-element-1.py 
# before pop ['Ford', 'Volvo', 'BMW']
# after pop(1) ['Ford', 'BMW']