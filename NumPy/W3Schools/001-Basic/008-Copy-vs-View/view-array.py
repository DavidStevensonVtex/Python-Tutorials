# Make a view, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# $ python view-array.py 
# [42  2  3  4  5]
# [42  2  3  4  5]