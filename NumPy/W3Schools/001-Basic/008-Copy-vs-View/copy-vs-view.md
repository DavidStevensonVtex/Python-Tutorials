# [W3Schools NumPy](https://www.w3schools.com/python/numpy/default.asp)

## [NumPy Array Copy vs View](https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp)

### The Difference Between Copy and View

The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

```
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
```

The copy SHOULD NOT be affected by the changes made to the original array.

```
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
```

The view SHOULD be affected by the changes made to the original array.

```
# Make Changes in the VIEW:
# Make a view, change the view, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

# $ python make-changes-in-view.py 
# [31  2  3  4  5]
# [31  2  3  4  5]
```

The original array SHOULD be affected by the changes made to the view.