# [W3Schools NumPy](https://www.w3schools.com/python/numpy/default.asp)

## [NumPy Data Types](https://www.w3schools.com/python/numpy/numpy_data_types.asp)

### Data Types in Python

By default Python have these data types:

* strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
* integer - used to represent integer numbers. e.g. -1, -2, -3
* float - used to represent real numbers. e.g. 1.2, 42.42
* boolean - used to represent True or False.
* complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
* Data Types in NumPy
* NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

* i - integer
* b - boolean
* u - unsigned integer
* f - float
* c - complex float
* m - timedelta
* M - datetime
* O - object
* S - string
* U - unicode string
* V - fixed chunk of memory for other type ( void )

### Checking the Data Type of an Array

The NumPy array object has a property called dtype that returns the data type of the array:

```
# Get the data type of an array object:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

# $ python array-data-type.py 
# int64
```

```
# Get the data type of an array containing strings:

import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

# $ python array-data-type-string.py 
# <U6
```

### Creating Arrays With a Defined Data Type

We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:

```
# Create an array with data type string:

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

# $ python defined-data-type.py 
# [b'1' b'2' b'3' b'4']
# |S1
```

For i, u, f, S and U we can define size as well.

```
# Create an array with data type 4 bytes integer:

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

# $ python i4-data-type.py 
# [1 2 3 4]
# int32
```

### What if a Value Can Not Be Converted?

If a type is given in which elements can't be casted then NumPy will raise a ValueError.

ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

```
# A non integer string like 'a' can not be converted to integer (will raise an error):

import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')

# $ python value-error.py 
#     arr = np.array(['a', '2', '3'], dtype='i')
# ValueError: invalid literal for int() with base 10: 'a'
```