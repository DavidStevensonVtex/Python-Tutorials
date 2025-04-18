#  [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)

## Learning Objectives

After reading, you should be able to:

* Understand the difference between one-, two- and n-dimensional arrays in NumPy;

* Understand how to apply some linear algebra operations to n-dimensional arrays without using for-loops;

* Understand axis and shape properties for n-dimensional arrays.

## The basics

NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called axes.

For example, the array for the coordinates of a point in 3D space, [1, 2, 1], has one axis. That axis has 3 elements in it, so we say it has a length of 3. In the example pictured below, the array has 2 axes. The first axis has a length of 2, the second axis has a length of 3.

```
[[1., 0., 0.],
 [0., 1., 2.]]
```

NumPy’s array class is called _ndarray_. It is also known by the alias _array_. Note that _numpy.array_ is not the same as the Standard Python Library class _array.array_, which only handles one-dimensional arrays and offers less functionality. The more important attributes of an ndarray object are:

* ndarray.ndim

    the number of axes (dimensions) of the array.

* ndarray.shape

    the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the number of axes, ndim.

* ndarray.size

    the total number of elements of the array. This is equal to the product of the elements of shape.

* ndarray.dtype

    an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.

* ndarray.itemsize

    the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.

* ndarray.data

    the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.

### An example

```
$ python3 
Python 3.10.9 (main, Mar  1 2023, 18:23:06) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np

a>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.dtype.name
'int64'
>>> a.itemsize
8
>>> a.size
15
>>> type(a)
<class 'numpy.ndarray'>
>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
<class 'numpy.ndarray'>
>>> type(a)
<class 'numpy.ndarray'>
>>> 
```

### Array creation

There are several ways to create arrays.

For example, you can create an array from a regular Python list or tuple using the array function. The type of the resulting array is deduced from the type of the elements in the sequences.

```
>>> import numpy as np
>>> a = np.array([2, 3, 4])
>>> a
array([2, 3, 4])
>>> a.dtype
dtype('int64')
>>> type(a)
<class 'numpy.ndarray'>
>>> b = np.array([1.2, 3.5, 5.1])
>>> b.dtype
dtype('float64')
>>> type(b)
<class 'numpy.ndarray'>
>>> 
```

A frequent error consists in calling array with multiple arguments, rather than providing a single sequence as an argument.

```
>>> a = np.array(1, 2, 3, 4)    # WRONG
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'np' is not defined
>>> import numpy as np
>>> a = np.array(1, 2, 3, 4)    # WRONG
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: array() takes from 1 to 2 positional arguments but 4 were given
>>> a = np.array([1, 2, 3, 4])  # RIGHT
```

array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.

```
>>> b = np.array([(1.5, 2, 3), (4, 5, 6)])
>>> b
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
```

The type of the array can also be explicitly specified at creation time:

```
>>> c = np.array([[1, 2], [3, 4]], dtype=complex)
>>> c
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j]])
```

Often, the elements of an array are originally unknown, but its size is known. Hence, NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation.

The function zeros creates an array full of zeros, the function ones creates an array full of ones, and the function empty creates an array whose initial content is random and depends on the state of the memory. By default, the dtype of the created array is float64, but it can be specified via the key word argument dtype.

```
>>> np.zeros((3, 4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.ones((2, 3, 4), dtype=np.int16)
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]], dtype=int16)
>>> np.empty((2, 3)) 
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
```

To create sequences of numbers, NumPy provides the arange function which is analogous to the Python built-in range, but returns an array.

```
>>> np.arange(10, 30, 5)
array([10, 15, 20, 25])
>>> np.arange(0, 2, 0.3)  # it accepts float arguments
array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
```

When arange is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. For this reason, it is usually better to use the function [linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) that receives as an argument the number of elements that we want, instead of the step:

```
>> from numpy import pi
>>> np.linspace(0, 2, 9)                   # 9 numbers from 0 to 2
array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])
>>> x = np.linspace(0, 2 * pi, 100)        # useful to evaluate function at lots of points
>>> f = np.sin(x)
```

#### See also

array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, random.Generator.random, random.Generator.normal, fromfunction, fromfile

### Printing arrays

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:

* the last axis is printed from left to right,

* the second-to-last is printed from top to bottom,

* the rest are also printed from top to bottom, with each slice separated from the next by an empty line.

One-dimensional arrays are then printed as rows, bidimensionals as matrices and tridimensionals as lists of matrices.

```
>>> a = np.arange(6)                    # 1d array
>>> print(a)
[0 1 2 3 4 5]
>>> b = np.arange(12).reshape(4, 3)     # 2d array
>>> print(b)
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
>>> c = np.arange(24).reshape(2, 3, 4)  # 3d array
>>> print(c)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
```

See below to get more details on reshape.

If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners:

```
>>> print(np.arange(10000))
[   0    1    2 ... 9997 9998 9999]
>>> print(np.arange(10000).reshape(100, 100))
[[   0    1    2 ...   97   98   99]
 [ 100  101  102 ...  197  198  199]
 [ 200  201  202 ...  297  298  299]
 ...
 [9700 9701 9702 ... 9797 9798 9799]
 [9800 9801 9802 ... 9897 9898 9899]
 [9900 9901 9902 ... 9997 9998 9999]]
```

To disable this behaviour and force NumPy to print the entire array, you can change the printing options using set_printoptions.

```
>>> import sys
>>> np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported
```

### Basic Operations

Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.

```
>>> import numpy as np
>>> a = np.array([20, 30, 40, 50])
>>> b = np.arange(4)
>>> b
array([0, 1, 2, 3])
>>> c = a - b
>>> c
array([20, 29, 38, 47])
>>> b**2
array([0, 1, 4, 9])
>>> 10 * np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a < 35
array([ True,  True, False, False])
```

Unlike in many matrix languages, the product operator \* operates elementwise in NumPy arrays. The matrix product can be performed using the \@ operator (in python >=3.5) or the dot function or method:

```
>>> A = np.array([[1, 1],
...               [0, 1]])
>>> B = np.array([[2, 0],
...               [3, 4]])
>>> A * B     # elementwise product
array([[2, 0],
       [0, 4]])
>>> A @ B     # matrix product
array([[5, 4],
       [3, 4]])
>>> A.dot(B)  # another matrix product
array([[5, 4],
       [3, 4]])
```



[what is a matrix product](https://www.google.com/search?q=what+is+a+matrix+product&oq=what+is+a+matrix+product&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDMxMDNqMGo3qAIIsAIB8QUpw1SR20dvAvEFKcNUkdtHbwI&sourceid=chrome&ie=UTF-8)

#### Why is a matrix product useful

Matrix products are useful because they allow efficient representation and manipulation of linear transformations, solving systems of equations, and processing data in various fields like computer graphics, machine learning, and network theory. 

--

Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.

```
>>> rg = np.random.default_rng(1)  # create instance of default random number generator
>>> a = np.ones((2, 3), dtype=int)
>>> b = rg.random((2, 3))
>>> a *= 3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> b += a
>>> b
array([[3.51182162, 3.9504637 , 3.14415961],
       [3.94864945, 3.31183145, 3.42332645]])
>>> a += b  # b is not automatically converted to integer type
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
```

When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).

```
>>> from math import pi
>>> a = np.ones(3, dtype=np.int32)
>>> b = np.linspace(0, pi, 3)
>>> b.dtype.name
'float64'
>>> b
array([0.        , 1.57079633, 3.14159265])
>>> a
array([1, 1, 1], dtype=int32)
>>> c = a + b
>>> c
array([1.        , 2.57079633, 4.14159265])
>>> c.dtype.name
'float64'
>>> d = np.exp(c * 1j)
>>> d
array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
```

The numpy.exp() function calculates the exponential of all elements in an input array. When dealing with complex numbers, numpy.exp() correctly applies the exponential function, leveraging Euler's formula to handle the imaginary component.

Euler's formula states that e^(ix) = cos(x) + i*sin(x), where e is the base of the natural logarithm, i is the imaginary unit, and x is a real number. When applied to a complex number z = a + bi, the exponential function becomes:

`e^z = e^(a + bi) = e^a * e^(bi) = e^a * (cos(b) + i*sin(b))`.

Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the ndarray class.

```
>>> a = rg.random((2, 3))
>>> a
array([[0.82770259, 0.40919914, 0.54959369],
       [0.02755911, 0.75351311, 0.53814331]])
>>> a.sum()
3.1057109529998157
>>> a.min()
0.027559113243068367
>>> a.max()
0.8277025938204418
```

By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However, by specifying the axis parameter you can apply an operation along the specified axis of an array:

```
>>> b = np.arange(12).reshape(3, 4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> b.sum(axis=0)     # sum of each column
array([12, 15, 18, 21])
>>> b.min(axis=1)     # min of each row
array([0, 4, 8])
>>> b.cumsum(axis=1)  # cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])
```

### Universal functions

NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions” (ufunc). Within NumPy, these functions operate elementwise on an array, producing an array as output.

```
>>> B = np.arange(3)
>>> B
array([0, 1, 2])
>>> np.exp(B)
array([1.        , 2.71828183, 7.3890561 ])
>>> np.sqrt(B)
array([0.        , 1.        , 1.41421356])
>>> C = np.array([2., -1., 4.])
>>> np.add(B, C)
array([2., 0., 6.])
```

#### See also

all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, invert, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where

### Indexing, slicing and iterating

One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences.

```
>>> a = np.arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64])
>>> # equivalent to a[0:6:2] = 1000;
>>> # from start to position 6, exclusive, set every 2nd element to 1000
>>> a[:6:2] = 1000
>>> a
array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])
>>> a[::-1]  # reversed a
array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000])
>>> a
array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])
>>> for i in a:
...     print(i**(1 / 3.))
... 
9.999999999999998
1.0
9.999999999999998
3.0
9.999999999999998
4.999999999999999
5.999999999999999
6.999999999999999
7.999999999999999
8.999999999999998
```

Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:

```
>>> def f(x, y):
...     return 10 * x + y
... 
>>> b = np.fromfunction(f, (5, 4), dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2, 3]
23
>>> b[0:5, 1]  # each row in the second column of b
array([ 1, 11, 21, 31, 41])
>>> b[:, 1]    # equivalent to the previous example
array([ 1, 11, 21, 31, 41])
>>> b[1:3, :]  # each column in the second and third row of b
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
```

When fewer indices are provided than the number of axes, the missing indices are considered complete slices:

```
>>> b[-1]   # the last row. Equivalent to b[-1, :]
array([40, 41, 42, 43])
```

The expression within brackets in b[i] is treated as an i followed by as many instances of : as needed to represent the remaining axes. NumPy also allows you to write this using dots as b[i, ...].

The dots (...) represent as many colons as needed to produce a complete indexing tuple. For example, if x is an array with 5 axes, then

* x[1, 2, ...] is equivalent to x[1, 2, :, :, :],

* x[..., 3] to x[:, :, :, :, 3] and

* x[4, ..., 5, :] to x[4, :, :, 5, :].

```
>>> c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
...                [ 10, 12, 13]],
...               [[100, 101, 102],
...                [110, 112, 113]]])
>>> c.shape
(2, 2, 3)
>>> c[1, ...]  # same as c[1, :, :] or c[1]
array([[100, 101, 102],
       [110, 112, 113]])
>>> c[..., 2]  # same as c[:, :, 2]
array([[  2,  13],
       [102, 113]])
```

Iterating over multidimensional arrays is done with respect to the first axis:

```
>>> for row in b:
...     print(row)
... 
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
```

However, if one wants to perform an operation on each element in the array, one can use the flat attribute which is an [iterator](https://docs.python.org/3/tutorial/classes.html#iterators) over all the elements of the array:

```
>>> for element in b.flat:
...     print(element)
... 
0
1
2
3
10
11
12
13
20
21
22
23
30
31
32
33
40
41
42
43
```

#### See also

Indexing on ndarrays, Indexing routines (reference), newaxis, ndenumerate, indices

### Shape manipulation

#### Changing the shape of an array

An array has a shape given by the number of elements along each axis:

```
>>> import numpy as np
>>> rg = np.random.default_rng(1)
>>> a = np.floor(10 * rg.random((3, 4)))
>>> a
array([[5., 9., 1., 9.],
       [3., 4., 8., 4.],
       [5., 0., 7., 5.]])
>>> a.shape
(3, 4)
>>> a.dtype
dtype('float64')
```

The shape of an array can be changed with various commands. Note that the following three commands all return a modified array, but do not change the original array:

```
>>> a.ravel()  # returns the array, flattened
array([5., 9., 1., 9., 3., 4., 8., 4., 5., 0., 7., 5.])
>>> a.reshape(6, 2)  # returns the array with a modified shape
array([[5., 9.],
       [1., 9.],
       [3., 4.],
       [8., 4.],
       [5., 0.],
       [7., 5.]])
>>> a.T  # returns the array, transposed
array([[5., 3., 5.],
       [9., 4., 0.],
       [1., 8., 7.],
       [9., 4., 5.]])
>>> a.T.shape
(4, 3)
>>> a.shape
(3, 4)
```

The order of the elements in the array resulting from ravel is normally “C-style”, that is, the rightmost index “changes the fastest”, so the element after a[0, 0] is a[0, 1]. If the array is reshaped to some other shape, again the array is treated as “C-style”. NumPy normally creates arrays stored in this order, so ravel will usually not need to copy its argument, but if the array was made by taking slices of another array or created with unusual options, it may need to be copied. The functions ravel and reshape can also be instructed, using an optional argument, to use FORTRAN-style arrays, in which the leftmost index changes the fastest.

The [reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape) function returns its argument with a modified shape, whereas the [ndarray.resize](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html#numpy.ndarray.resize) method modifies the array itself:

```
>>> a
array([[5., 9., 1., 9.],
       [3., 4., 8., 4.],
       [5., 0., 7., 5.]])
>>> a.resize((2, 6))
>>> a
array([[5., 9., 1., 9., 3., 4.],
       [8., 4., 5., 0., 7., 5.]])
```

If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:

```
>>> a.reshape(3, -1)
array([[5., 9., 1., 9.],
       [3., 4., 8., 4.],
       [5., 0., 7., 5.]])
```

#### See also

ndarray.shape, reshape, resize, ravel

#### Stacking together different arrays

Several arrays can be stacked together along different axes:

```
>>> a = np.floor(10 * rg.random((2, 2)))
>>> a
array([[3., 7.],
       [3., 4.]])
>>> b = np.floor(10 * rg.random((2, 2)))
>>> b
array([[1., 4.],
       [2., 2.]])
>>> np.vstack((a, b))
array([[3., 7.],
       [3., 4.],
       [1., 4.],
       [2., 2.]])
>>> np.hstack((a, b))
array([[3., 7., 1., 4.],
       [3., 4., 2., 2.]])
```

The function [column_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack) stacks 1D arrays as columns into a 2D array. It is equivalent to [hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack) only for 2D arrays:

```
>>> from numpy import newaxis
>>> np.column_stack((a, b))  # with 2D arrays
array([[3., 7., 1., 4.],
       [3., 4., 2., 2.]])
>>> a = np.array([4., 2.])
>>> b = np.array([3., 8.])
>>> np.column_stack((a, b))  # returns a 2D array
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a, b))        # the result is different
array([4., 2., 3., 8.])
>>> a[:, newaxis]  # view `a` as a 2D column vector
array([[4.],
       [2.]])
>>> np.column_stack((a[:, newaxis], b[:, newaxis]))
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a[:, newaxis], b[:, newaxis]))  # the result is the same
array([[4., 3.],
       [2., 8.]])
```

In general, for arrays with more than two dimensions, [hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack) stacks along their second axes, [vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack) stacks along their first axes, and [concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate) allows for an optional arguments giving the number of the axis along which the concatenation should happen.

In NumPy, axes are the dimensions of an array. For a 2D array, the first axis (axis 0) runs vertically downwards across rows, and the second axis (axis 1) runs horizontally across columns. The number of axes is referred to as the rank of the array. For higher-dimensional arrays, the axes are numbered starting from 0, with each axis corresponding to a dimension of the array. For example, in a 3D array, axis 0 represents depth, axis 1 represents rows, and axis 2 represents columns.

[Understanding axes in NumPy](https://stackoverflow.com/questions/46855793/understanding-axes-in-numpy)

Note

In complex cases, [r_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_) and [c_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_) are useful for creating arrays by stacking numbers along one axis. They allow the use of range literals :.

```
>>> np.r_[1:4, 0, 4]
array([1, 2, 3, 0, 4])
```

When used with arrays as arguments, [r_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_) and [c_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_) are similar to [vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack) and [hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack) in their default behavior, but allow for an optional argument giving the number of the axis along which to concatenate.

##### See also

hstack, vstack, column_stack, concatenate, c_, r_


#### Splitting one array into several smaller ones

Using [hsplit](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit), you can split an array along its horizontal axis, either by specifying the number of equally shaped arrays to return, or by specifying the columns after which the division should occur:

```
>>> a = np.floor(10 * rg.random((2, 12)))
>>> a
array([[7., 2., 4., 9., 9., 7., 5., 2., 1., 9., 5., 1.],
       [6., 7., 6., 9., 0., 5., 4., 0., 6., 8., 5., 2.]])
>>> # Split `a` into 3
>>> np.hsplit(a, 3)
[array([[7., 2., 4., 9.],
       [6., 7., 6., 9.]]), array([[9., 7., 5., 2.],
       [0., 5., 4., 0.]]), array([[1., 9., 5., 1.],
       [6., 8., 5., 2.]])]
>>> # Split `a` after the third and the fourth column
>>> np.hsplit(a, (3, 4))
[array([[7., 2., 4.],
       [6., 7., 6.]]), array([[9.],
       [9.]]), array([[9., 7., 5., 2., 1., 9., 5., 1.],
       [0., 5., 4., 0., 6., 8., 5., 2.]])]
```

[vsplit](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit) splits along the vertical axis, and [array_split](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split) allows one to specify along which axis to split.

### Copies and Views

When operating and manipulating arrays, their data is sometimes copied into a new array and sometimes not. This is often a source of confusion for beginners. There are three cases:

#### No copy at all

Simple assignments make no copy of objects or their data.

```
>>> a = np.array([[ 0,  1,  2,  3],
...               [ 4,  5,  6,  7],
...               [ 8,  9, 10, 11]])
>>> b = a            # no new object is created
>>> b is a 
True
```

Python passes mutable objects as references, so function calls make no copy.

```
>>> def f(x):
...     print(id(x))
... 
>>> id(a)  # id is a unique identifier of an object
139932100777552
>>> f(a) 
139932100777552
```

#### View or shallow copy

Different array objects can share the same data. The view method creates a new array object that looks at the same data.

```

```