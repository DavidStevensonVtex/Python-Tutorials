import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

# $ python create-5d-array.py 
# [[[[[1 2 3 4]]]]]
# number of dimensions : 5