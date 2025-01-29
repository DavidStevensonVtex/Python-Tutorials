# Chapter 2: Data Structures

## [2.3 array — Sequence of Fixed-type Data](https://pymotw.com/3/array/index.html)

Purpose:	Manage sequences of fixed-type numerical data efficiently.

The array module defines a sequence data structure that looks very much like a list, except that all of the members have to be of the same primitive type. The types supported are all numeric or other fixed-size primitive types such as bytes.

Refer to the table below for some of the supported types. The standard library documentation for array includes a complete list of type codes.

Type Codes for array Members

Code	Type	Minimum size (bytes)

* b	int	1
* B	int	1
* h	signed short	2
* H	unsigned short	2
* i	signed int	2
* I	unsigned int	2
* l	signed long	4
* L	unsigned long	4
* q	signed long long	8
* Q	unsigned long long	8
* f	float	4
* d	double float	8

### 2.3.1 Initialization

An array is instantiated with an argument describing the type of data to be allowed, and possibly an initial sequence of data to store in the array.

```
# array_string.py
import array
import binascii

s = b'This is the array.'
a = array.array('b', s)

print('As byte string:', s)
print('As array      :', a)
print('As hex        :', binascii.hexlify(a))
```

In this example, the array is configured to hold a sequence of bytes and is initialized with a simple byte string.

```
$ python3 array_string.py
As byte string: b'This is the array.'
As array      : array('b', [84, 104, 105, 115, 32, 105, 115, 32, 116, 104, 101, 32, 97, 114, 114, 97, 121, 46])
As hex        : b'54686973206973207468652061727261792e'
```

### 2.3.2 Manipulating Arrays

An array can be extended and otherwise manipulated in the same ways as other Python sequences.

```
# array_sequence.py
import array
import pprint

a = array.array('i', range(3))
print('Initial :', a)

a.extend(range(3))
print('Extended:', a)

print('Slice   :', a[2:5])

print('Iterator:')
print(list(enumerate(a)))
```

The supported operations include slicing, iterating, and adding elements to the end.

```
$ python3 array_sequence.py
Initial : array('i', [0, 1, 2])
Extended: array('i', [0, 1, 2, 0, 1, 2])
Slice   : array('i', [2, 0, 1])
Iterator:
[(0, 0), (1, 1), (2, 2), (3, 0), (4, 1), (5, 2)]
```