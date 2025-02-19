# [Chapter 5: Mathematics](https://pymotw.com/3/numeric.html)

## [5.4 math — Mathematical Functions](https://pymotw.com/3/math/index.html)

Purpose:	Provides functions for specialized mathematical operations.

The math module implements many of the IEEE functions that would normally be found in the native platform C libraries for complex mathematical operations using floating point values, including logarithms and trigonometric operations.

### Quick Links

* [Special Constants](https://pymotw.com/3/math/index.html#special-constants)
* [Testing for Exceptional Values](https://pymotw.com/3/math/index.html#testing-for-exceptional-values)
* [Comparing](https://pymotw.com/3/math/index.html#comparing)
* [Converting Floating Point Values to Integers](https://pymotw.com/3/math/index.html#converting-floating-point-values-to-integers)
* [Alternate Representations of Floating Point Values](https://pymotw.com/3/math/index.html#alternate-representations-of-floating-point-values)
* [Positive and Negative Signs](https://pymotw.com/3/math/index.html#positive-and-negative-signs)
* [Commonly Used Calculations](https://pymotw.com/3/math/index.html#commonly-used-calculations)
* [Exponents and Logarithms](https://pymotw.com/3/math/index.html#exponents-and-logarithms)
* [Angles](https://pymotw.com/3/math/index.html#angles)
* [Trigonometry](https://pymotw.com/3/math/index.html#trigonometry)
* [Hyperbolic Functions](https://pymotw.com/3/math/index.html#hyperbolic-functions)
* [Special Functions](https://pymotw.com/3/math/index.html#special-functions)

### 5.4.1 Special Constants

Many math operations depend on special constants. math includes values for π (pi), e, nan (not a number), and infinity.

```
# math_constants.py
import math

print("  π: {:.30f}".format(math.pi))
print("  e: {:.30f}".format(math.e))
print("nan: {:.30f}".format(math.nan))
print("inf: {:.30f}".format(math.inf))
```

Both π and e are limited in precision only by the platform’s floating point C library.

```
$ python3 math_constants.py
  π: 3.141592653589793115997963468544
  e: 2.718281828459045090795598298428
nan: nan
inf: inf
```

### 5.4.2 Testing for Exceptional Values

Floating point calculations can result in two types of exceptional values. The first of these, inf (infinity), appears when the double used to hold a floating point value overflows from a value with a large absolute value.

```
# math_isinf.py
import math

print("{:^3} {:6} {:6} {:6}".format("e", "x", "x**2", "isinf"))
print("{:-^3} {:-^6} {:-^6} {:-^6}".format("", "", "", ""))

for e in range(0, 201, 20):
    x = 10.0**e
    y = x * x
    print(
        "{:3d} {:<6g} {:<6g} {!s:6}".format(
            e,
            x,
            y,
            math.isinf(y),
        )
    )
```

When the exponent in this example grows large enough, the square of x no longer fits inside a double, and the value is recorded as infinite.

```
$ python3 math_isinf.py
 e  x      x**2   isinf 
--- ------ ------ ------
  0 1      1      False 
 20 1e+20  1e+40  False 
 40 1e+40  1e+80  False 
 60 1e+60  1e+120 False 
 80 1e+80  1e+160 False 
100 1e+100 1e+200 False 
120 1e+120 1e+240 False 
140 1e+140 1e+280 False 
160 1e+160 inf    True  
180 1e+180 inf    True  
200 1e+200 inf    True 
```

Not all floating point overflows result in inf values, however. Calculating an exponent with floating point values, in particular, raises OverflowError instead of preserving the inf result.

```
# math_overflow.py
x = 10.0**200

print("x    =", x)
print("x*x  =", x * x)
print("x**2 =", end=" ")
try:
    print(x**2)
except OverflowError as err:
    print(err)
```

This discrepancy is caused by an implementation difference in the library used by C Python.

```
$ python3 math_overflow.py
x    = 1e+200
x*x  = inf
x**2 = (34, 'Numerical result out of range')
```

Division operations using infinite values are undefined. The result of dividing a number by infinity is nan (not a number).

```
# math_isnan.py
import math

x = (10.0**200) * (10.0**200)
y = x / x

print("x =", x)
print("isnan(x) =", math.isnan(x))
print("y = x / x =", x / x)
print("y == nan =", y == float("nan"))
print("isnan(y) =", math.isnan(y))
```

nan does not compare as equal to any value, even itself, so to check for nan use isnan().

```
$ python3 math_isnan.py
x = inf
isnan(x) = False
y = x / x = nan
y == nan = False
isnan(y) = True
```

Use isfinite() to check for regular numbers or either of the special values inf or nan.

```
# math_isfinite.py
import math

for f in [0.0, 1.0, math.pi, math.e, math.inf, math.nan]:
    print("{:5.2f} {!s}".format(f, math.isfinite(f)))
```

isfinite() returns false for either of the exceptional cases, and true otherwise.

```
$ python3 math_isfinite.py
 0.00 True
 1.00 True
 3.14 True
 2.72 True
  inf False
  nan False
```

### 5.4.3 Comparing

Comparisons for floating point values can be error prone, with each step of the computation potentially introducing errors due to the numerical representation. The isclose() function uses a stable algorithm to minimize these errors and provide a way for relative as well as absolute comparisons. The formula used is equivalent to

`abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`

By default, isclose() uses relative comparison with the tolerance set to 1e-09, meaning that the difference between the values must be less than or equal to 1e-09 times the larger absolute value between a and b. Passing a keyword argument rel_tol to isclose() changes the tolerance. In this example, the values must be within 10% of each other.

```
# math_isclose.py
import math

INPUTS = [
    (1000, 900, 0.1),
    (100, 90, 0.1),
    (10, 9, 0.1),
    (1, 0.9, 0.1),
    (0.1, 0.09, 0.1),
]

print(
    "{:^8} {:^8} {:^8} {:^8} {:^8} {:^8}".format(
        "a", "b", "rel_tol", "abs(a-b)", "tolerance", "close"
    )
)
print(
    "{:-^8} {:-^8} {:-^8} {:-^8} {:-^8} {:-^8}".format("-", "-", "-", "-", "-", "-"),
)

fmt = "{:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {!s:>8}"

for a, b, rel_tol in INPUTS:
    close = math.isclose(a, b, rel_tol=rel_tol)
    tolerance = rel_tol * max(abs(a), abs(b))
    abs_diff = abs(a - b)
    print(fmt.format(a, b, rel_tol, abs_diff, tolerance, close))
```

The comparison between 0.1 and 0.09 fails because of the error representing 0.1.

```
$ python3 math_isclose.py
   a        b     rel_tol  abs(a-b) tolerance  close  
-------- -------- -------- -------- -------- --------
 1000.00   900.00     0.10   100.00   100.00     True
  100.00    90.00     0.10    10.00    10.00     True
   10.00     9.00     0.10     1.00     1.00     True
    1.00     0.90     0.10     0.10     0.10     True
    0.10     0.09     0.10     0.01     0.01    False
```

To use a fixed or “absolute” tolerance, pass abs_tol instead of rel_tol.

```
# math_isclose_abs_tol.py
import math

INPUTS = [
    (1.0, 1.0 + 1e-07, 1e-08),
    (1.0, 1.0 + 1e-08, 1e-08),
    (1.0, 1.0 + 1e-09, 1e-08),
]

print(
    "{:^8} {:^11} {:^8} {:^10} {:^8}".format("a", "b", "abs_tol", "abs(a-b)", "close")
)
print(
    "{:-^8} {:-^11} {:-^8} {:-^10} {:-^8}".format("-", "-", "-", "-", "-"),
)

for a, b, abs_tol in INPUTS:
    close = math.isclose(a, b, abs_tol=abs_tol)
    abs_diff = abs(a - b)
    print("{:8.2f} {:11} {:8} {:0.9f} {!s:>8}".format(a, b, abs_tol, abs_diff, close))
```

For an absolute tolerance, the difference between the input values must be less than the tolerance given.

```
$ python3 math_isclose_abs_tol.py
   a          b      abs_tol   abs(a-b)   close  
-------- ----------- -------- ---------- --------
    1.00   1.0000001    1e-08 0.000000100    False
    1.00  1.00000001    1e-08 0.000000010     True
    1.00 1.000000001    1e-08 0.000000001     True
```

nan and inf are special cases.

```
# math_isclose_inf.py
import math

print("nan, nan:", math.isclose(math.nan, math.nan))
print("nan, 1.0:", math.isclose(math.nan, 1.0))
print("inf, inf:", math.isclose(math.inf, math.inf))
print("inf, 1.0:", math.isclose(math.inf, 1.0))
```

nan is never close to another value, including itself. inf is only close to itself.

```
$ python3 math_isclose_inf.py
nan, nan: False
nan, 1.0: False
inf, inf: True
inf, 1.0: False
```

### 5.4.4 Converting Floating Point Values to Integers

The math module includes three functions for converting floating point values to whole numbers. Each takes a different approach, and will be useful in different circumstances.

The simplest is trunc(), which truncates the digits following the decimal, leaving only the significant digits making up the whole number portion of the value. floor() converts its input to the largest preceding integer, and ceil() (ceiling) produces the largest integer following sequentially after the input value.

```
# math_integers.py
import math

HEADINGS = ("i", "int", "trunk", "floor", "ceil")
print("{:^5} {:^5} {:^5} {:^5} {:^5}".format(*HEADINGS))
print(
    "{:-^5} {:-^5} {:-^5} {:-^5} {:-^5}".format(
        "",
        "",
        "",
        "",
        "",
    )
)

fmt = "{:5.1f} {:5.1f} {:5.1f} {:5.1f} {:5.1f}"

TEST_VALUES = [
    -1.5,
    -0.8,
    -0.5,
    -0.2,
    0,
    0.2,
    0.5,
    0.8,
    1,
]

for i in TEST_VALUES:
    print(
        fmt.format(
            i,
            int(i),
            math.trunc(i),
            math.floor(i),
            math.ceil(i),
        )
    )
```

trunc() is equivalent to converting to int directly.

```
$ python3 math_integers.py
  i    int  trunk floor ceil 
----- ----- ----- ----- -----
 -1.5  -1.0  -1.0  -2.0  -1.0
 -0.8   0.0   0.0  -1.0   0.0
 -0.5   0.0   0.0  -1.0   0.0
 -0.2   0.0   0.0  -1.0   0.0
  0.0   0.0   0.0   0.0   0.0
  0.2   0.0   0.0   0.0   1.0
  0.5   0.0   0.0   0.0   1.0
  0.8   0.0   0.0   0.0   1.0
  1.0   1.0   1.0   1.0   1.0
```