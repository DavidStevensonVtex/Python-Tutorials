# [W3Schools NumPy](https://www.w3schools.com/python/numpy/default.asp)

## [NumPy Array Reshaping](https://www.w3schools.com/python/numpy/numpy_array_reshape.asp)

### Reshaping arrays

Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.

#### Reshape From 1-D to 2-D

Convert the following 1-D array with 12 elements into a 2-D array.

The outermost dimension will have 4 arrays, each with 3 elements:

```
# Convert the following 1-D array with 12 elements into a 2-D array.

# The outermost dimension will have 4 arrays, each with 3 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

# $ python reshape-1d-to-2d.py
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
```

#### Reshape From 1-D to 3-D

Convert the following 1-D array with 12 elements into a 3-D array.

The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

```
# Convert the following 1-D array with 12 elements into a 3-D array.

# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

# $ python reshape-1d-to-3d.py
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]
```

### Can We Reshape Into any Shape?

Yes, as long as the elements required for reshaping are equal in both shapes.

We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

```

```