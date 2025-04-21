# [W3Schools NumPy](https://www.w3schools.com/python/numpy/default.asp)

## [NumPy Array Slicing](https://www.w3schools.com/python/numpy/numpy_array_slicing.asp)

### Slicing arrays

Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

Slice elements from index 1 to index 5 from the following array:

```
# Slice elements from index 1 to index 5 from the following array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

# $ python array-slice-1.py 
# [2 3 4 5]
```

Note: The result includes the start index, but excludes the end index.

Slice elements from index 4 to the end of the array:

```
# Slice elements from index 4 to the end of the array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

# $ python slice-to-end-of-array.py 
# [5 6 7]
```

```
# Slice elements from the beginning to index 4 (not included):

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

# $ python slice-from-beginning.py 
# [1 2 3 4]
```

### Negative Slicing

Use the minus operator to refer to an index from the end:

```
# Slice from the index 3 from the end to index 1 from the end:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

# $ python negative-slicing.py 
# [5 6]
```

### STEP

Use the step value to determine the step of the slicing:

```
# Return every other element from index 1 to index 5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

# $ python slice-using-step.py 
# [2 4]
```

```
# Return every other element from the entire array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

$ python slice-every-other-element.py 
# [1 3 5 7]
```