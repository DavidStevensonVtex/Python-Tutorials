# Change data type from integer to boolean:

import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)

# $ python convert-from-int-to-boolean.py 
# [ True False  True]
# bool