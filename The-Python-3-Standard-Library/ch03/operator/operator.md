# [Chapter 3 Algorithms](https://pymotw.com/3/algorithm_tools.html)

## [3.3 operator — Functional Interface to Built-in Operators](https://pymotw.com/3/operator/index.html)

Purpose:	Functional interface to built-in operators.

Programming using iterators occasionally requires creating small functions for simple expressions. Sometimes, these can be implemented as lambda functions, but for some operations new functions are not needed at all. The operator module defines functions that correspond to built-in operations for arithmetic, comparison, and other operations corresponding to standard object APIs.

### 3.3.1 Logical Operations

There are functions for determining the boolean equivalent for a value, negating it to create the opposite boolean value, and comparing objects to see if they are identical.

```
# operator_boolean.py
from operator import *

a = -1
b = 5

print("a =", a)
print("b =", b)
print()

print("not_(a)     :", not_(a))
print("truth(a)    :", truth(a))
print("is_(a, b)   :", is_(a, b))
print("is_not(a, b):", is_not(a, b))
```

not\_() includes the trailing underscore because not is a Python keyword. truth() applies the same logic used when testing an expression in an if statement or converting an expression to a bool. is\_() implements the same check used by the is keyword, and is\_not() does the same test and returns the opposite answer.

```
$ python3 operator_boolean.py
a = -1
b = 5

not_(a)     : False
truth(a)    : True
is_(a, b)   : False
is_not(a, b): True
```

### 3.3.2 Comparison Operators

All of the rich comparison operators are supported.

```
# operator_comparisons.py
from operator import *

a = 1
b = 5.0

print("a =", a)
print("b =", b)
for func in (lt, le, eq, ne, ge, gt):
    print("{}(a, b): {}".format(func.__name__, func(a, b)))
```

The functions are equivalent to the expression syntax using <, <=, ==, >=, and >.

```
$ python3 operator_comparisons.py
a = 1
b = 5.0
lt(a, b): True
le(a, b): True
eq(a, b): False
ne(a, b): True
ge(a, b): False
gt(a, b): False
```

### 3.3.3 Arithmetic Operators

The arithmetic operators for manipulating numerical values are also supported.

```
# operator_math.py
from operator import *

a = -1
b = 5.0
c = 2
d = 6

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

print("\nPositive/Negative:")
print("abs(a):", abs(a))
print("neg(a):", neg(a))
print("neg(b):", neg(b))
print("pos(a):", pos(a))
print("pos(b):", pos(b))

print("\nArithmetic:")
print("add(a, b)     :", add(a, b))
print("floordiv(a, b):", floordiv(a, b))
print("floordiv(d, c):", floordiv(d, c))
print("mod(a, b)     :", mod(a, b))
print("mul(a, b)     :", mul(a, b))
print("pow(c, d)     :", pow(c, d))
print("sub(b, a)     :", sub(b, a))
print("truediv(a, b) :", truediv(a, b))
print("truediv(d, c) :", truediv(d, c))

print("\nBitwise:")
print("and_(c, d)  :", and_(c, d))
print("invert(c)   :", invert(c))
print("lshift(c, d):", lshift(c, d))
print("or_(c, d)   :", or_(c, d))
print("rshift(d, c):", rshift(d, c))
print("xor(c, d)   :", xor(c, d))
```

There are two separate division operators: floordiv() (integer division as implemented in Python before version 3.0) and truediv() (floating point division).

```
$ python3 operator_math.py
a = -1
b = 5.0
c = 2
d = 6

Positive/Negative:
abs(a): 1
neg(a): 1
neg(b): -5.0
pos(a): -1
pos(b): 5.0

Arithmetic:
add(a, b)     : 4.0
floordiv(a, b): -1.0
floordiv(d, c): 3
mod(a, b)     : 4.0
mul(a, b)     : -5.0
pow(c, d)     : 64
sub(b, a)     : 6.0
truediv(a, b) : -0.2
truediv(d, c) : 3.0

Bitwise:
and_(c, d)  : 2
invert(c)   : -3
lshift(c, d): 128
or_(c, d)   : 6
rshift(d, c): 1
xor(c, d)   : 4
```

### 3.3.4 Sequence Operators

The operators for working with sequences can be divided into four groups: building up sequences, searching for items, accessing contents, and removing items from sequences.

```
# operator_sequences.py
from operator import *

a = [1, 2, 3]
b = ["a", "b", "c"]

print("a =", a)
print("b =", b)

print("\nConstructive:")
print("  concat(a, b):", concat(a, b))

print("\nSearching:")
print("  contains(a, 1)  :", contains(a, 1))
print('  contains(b, "d"):', contains(b, "d"))
print("  countOf(a, 1)   :", countOf(a, 1))
print('  countOf(b, "d") :', countOf(b, "d"))
print("  indexOf(a, 3)   :", indexOf(a, 3))

print("\nAccess Items:")
print("  getitem(b, 1)                  :", getitem(b, 1))
print("  getitem(b, slice(1, 3))        :", getitem(b, slice(1, 3)))
print('  setitem(b, 1, "d")             :', end=" ")
setitem(b, 1, "d")
print(b)
print("  setitem(a, slice(1, 3), [4, 5]):", end=" ")
setitem(a, slice(1, 3), [4, 5])
print(a)

print("\nDestructive:")
print("  delitem(b, 1)          :", end=" ")
delitem(b, 1)
print(b)
print("  delitem(a, slice(1, 3)):", end=" ")
delitem(a, slice(1, 3))
print(a)
```

Some of these operations, such as setitem() and delitem(), modify the sequence in place and do not return a value.

```
$ python3 operator_sequences.py
a = [1, 2, 3]
b = ['a', 'b', 'c']

Constructive:
  concat(a, b): [1, 2, 3, 'a', 'b', 'c']

Searching:
  contains(a, 1)  : True
  contains(b, "d"): False
  countOf(a, 1)   : 1
  countOf(b, "d") : 0
  indexOf(a, 3)   : 2

Access Items:
  getitem(b, 1)                  : b
  getitem(b, slice(1, 3))        : ['b', 'c']
  setitem(b, 1, "d")             : ['a', 'd', 'c']
  setitem(a, slice(1, 3), [4, 5]): [1, 4, 5]

Destructive:
  delitem(b, 1)          : ['a', 'c']
  delitem(a, slice(1, 3)): [1]
```