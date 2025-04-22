# Make a copy, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# $ python copy-array.py 
# [42  2  3  4  5]
# [1 2 3 4 5]