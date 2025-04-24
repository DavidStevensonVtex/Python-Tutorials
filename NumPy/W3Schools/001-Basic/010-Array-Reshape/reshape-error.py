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
