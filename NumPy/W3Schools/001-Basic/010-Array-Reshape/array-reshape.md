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
# Try converting 1D array with 8 elements to a 2D array with 3 elements
# in each dimension (will raise an error):

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)

print(newarr)

# $ python reshape-error.py
# Traceback (most recent call last):
#   File "/home/dstevenson/Python/GitHub/Python-Tutorials/NumPy/W3Schools/001-Basic/010-Array-Reshape/reshape-error.py", line 8, in <module>
#     newarr = arr.reshape(3, 3)
# ValueError: cannot reshape array of size 8 into shape (3,3)
```

### Returns Copy or View?

Check if the returned array is a copy or a view:

```
# Check if the returned array is a copy or a view:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

# $ python reshape-returns-copy-or-view.py
# [1 2 3 4 5 6 7 8]
# The example above returns the original array, so it is a view.
```

The example above returns the original array, so it is a view.

### Unknown Dimension

You are allowed to have one "unknown" dimension.

Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

Pass -1 as the value, and NumPy will calculate this number for you.

```
# Convert 1D array with 8 elements to 3D array with 2x2 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

# $ python unknown-dimension.py
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]
```

**Note:** We can not pass -1 to more than one dimension.

### Flattening the arrays

Flattening array means converting a multidimensional array into a 1D array.

We can use reshape(-1) to do this.

```
# Convert the array into a 1D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

# $ python flatten-the-arrays.py
# [1 2 3 4 5 6]
```

**Note:** There are a lot of functions for changing the shapes of arrays in numpy: flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.