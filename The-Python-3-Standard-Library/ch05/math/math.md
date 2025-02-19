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