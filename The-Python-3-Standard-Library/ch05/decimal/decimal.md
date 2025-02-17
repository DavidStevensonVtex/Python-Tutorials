# [Chapter 5: Mathematics](https://pymotw.com/3/numeric.html)

## [5.1 decimal — Fixed and Floating Point Math](https://pymotw.com/3/decimal/index.html)

Purpose:	Decimal arithmetic using fixed and floating point numbers

The decimal module implements fixed and floating point arithmetic using the model familiar to most people, rather than the IEEE floating point version implemented by most computer hardware and familiar to programmers. A Decimal instance can represent any number exactly, round up or down, and apply a limit to the number of significant digits.

### 5.1.1 Decimal

Decimal values are represented as instances of the Decimal class. The constructor takes as argument one integer or string. Floating point numbers can be converted to a string before being used to create a Decimal, letting the caller explicitly deal with the number of digits for values that cannot be expressed exactly using hardware floating point representations. Alternately, the class method from_float() converts to the exact decimal representation.

```
# decimal_create.py
import decimal

fmt = "{0:<25} {1:<25}"

print(fmt.format("Input", "Output"))
print(fmt.format("-" * 25, "-" * 25))

# Integer
print(fmt.format(5, decimal.Decimal(5)))

# String
print(fmt.format("3.14", decimal.Decimal("3.14")))

# Float
f = 0.1
print(fmt.format(repr(f), decimal.Decimal(str(f))))
print("{:<0.23g} {:<25}".format(f, str(decimal.Decimal.from_float(f))[:25]))
```

The floating point value of 0.1 is not represented as an exact value in binary, so the representation as a float is different from the Decimal value. The full string representation is truncated to 25 characters in the last line of this output.

```
$ python3 decimal_create.py
Input                     Output                   
------------------------- -------------------------
5                         5                        
3.14                      3.14                     
0.1                       0.1                      
0.10000000000000000555112 0.10000000000000000555111
```

Decimals can also be created from tuples containing a sign flag (0 for positive, 1 for negative), a tuple of digits, and an integer exponent.

```
# decimal_tuple.py
import decimal

# Tuple
t = (1, (1, 1), -2)
print("Input  :", t)
print("Decimal:", decimal.Decimal(t))
```

The tuple-based representation is less convenient to create, but does offer a portable way of exporting decimal values without losing precision. The tuple form can be transmitted through the network or stored in a database that does not support accurate decimal values, then turned back into a Decimal instance later.

```
$ python3 decimal_tuple.py
Input  : (1, (1, 1), -2)
Decimal: -0.11
```

### 5.1.2 Formatting

Decimal responds to Python’s [string formatting protocol](https://docs.python.org/3.5/library/string.html#formatspec), using the same syntax and options as other numerical types.

```
# decimal_format.py
import decimal

d = decimal.Decimal(1.1)
print("Precision:")
print("{:.1}".format(d))
print("{:.2}".format(d))
print("{:.3}".format(d))
print("{:.18}".format(d))

print("\nWidth and precision combined:")
print("{:5.1f} {:5.1g}".format(d, d))
print("{:5.2f} {:5.2g}".format(d, d))
print("{:5.2f} {:5.2g}".format(d, d))

print("\nZero padding:")
print("{:05.1}".format(d))
print("{:05.2}".format(d))
print("{:05.3}".format(d))
```

The format strings can control the width of the output, the precision (number of significant digits), and how to pad the value to fill the width.

```
$ python3 decimal_format.py
Precision:
1
1.1
1.10
1.10000000000000009

Width and precision combined:
  1.1     1
 1.10   1.1
 1.10   1.1

Zero padding:
00001
001.1
01.10
```

### 5.1.3 Arithmetic

Decimal overloads the simple arithmetic operators so instances can be manipulated in much the same way as the built-in numeric types.

```
# decimal_operators.py
import decimal

a = decimal.Decimal("5.1")
b = decimal.Decimal("3.14")
c = 4
d = 3.14

print("a     =", repr(a))
print("b     =", repr(b))
print("c     =", repr(c))
print("d     =", repr(d))
print()

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print()

print("a + c =", a + c)
print("a - c =", a - c)
print("a * c =", a * c)
print("a / c =", a / c)
print()

print("a + d =", end=" ")
try:
    print(a + d)
except TypeError as e:
    print(e)
```

Decimal operators also accept integer arguments, but floating point values must be converted to Decimal instances.

```
$ python3 decimal_operators.py
a     = Decimal('5.1')
b     = Decimal('3.14')
c     = 4
d     = 3.14

a + b = 8.24
a - b = 1.96
a * b = 16.014
a / b = 1.624203821656050955414012739

a + c = 9.1
a - c = 1.1
a * c = 20.4
a / c = 1.275

a + d = unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
```

Beyond basic arithmetic, Decimal includes the methods to find the base 10 and natural logarithms. The return values from log10() and ln() are Decimal instances, so they can be used directly in formulas with other values.

### 5.1.4 Special Values

In addition to the expected numerical values, Decimal can represent several special values, including positive and negative values for infinity, “not a number”, and zero.

```
# decimal_special.py
import decimal

for value in ["Infinity", "NaN", "0"]:
    print(decimal.Decimal(value), decimal.Decimal("-" + value))
print()

# Math with infinity
print("Infinity + 1:", (decimal.Decimal("Infinity") + 1))
print("-Infinity + 1:", (decimal.Decimal("-Infinity") + 1))

# Print comparing NaN
print(decimal.Decimal("NaN") == decimal.Decimal("Infinity"))
print(decimal.Decimal("NaN") != decimal.Decimal(1))
```

Adding to infinite values returns another infinite value. Comparing for equality with NaN always returns false and comparing for inequality always returns true. Comparing for sort order against NaN is undefined and results in an error.

```
$ python3 decimal_special.py
Infinity -Infinity
NaN -NaN
0 -0

Infinity + 1: Infinity
-Infinity + 1: -Infinity
False
True
```