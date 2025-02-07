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