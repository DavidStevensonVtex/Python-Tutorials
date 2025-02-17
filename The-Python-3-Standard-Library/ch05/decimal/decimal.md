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