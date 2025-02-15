# [Chapter 5: Mathematics](https://pymotw.com/3/numeric.html)

As a general purpose programming language, Python is frequently used to solve mathematical problems. It includes built-in types for managing integer and floating point numbers, which are suitable for the basic math that might appear in an average application. The standard library includes modules for more advanced needs.

Python’s built-in floating point numbers use the underlying double representation. They are sufficiently precise for most programs with mathematical requirements, but when more accurate representations of non-integer values are needed the [decimal](https://pymotw.com/3/decimal/index.html#module-decimal) and [fractions](https://pymotw.com/3/fractions/index.html#module-fractions) modules will be useful. Arithmetic with decimal and fractional values retains precision, but is not as fast as the native float.

The [random](https://pymotw.com/3/random/index.html#module-random) module includes a uniform distribution pseudorandom number generator, as well as functions for simulating many common non-uniform distributions.

The [math](https://pymotw.com/3/math/index.html#module-math) module contains fast implementations of advanced mathematical functions such as logarithms and trigonometric functions. The full complement of IEEE functions usually found in the native platform C libraries is available through the module.

* [decimal — Fixed and Floating Point Math](https://pymotw.com/3/decimal/index.html)
* [fractions — Rational Numbers](https://pymotw.com/3/fractions/index.html)
* [random — Pseudorandom Number Generators](https://pymotw.com/3/random/index.html)
* [math — Mathematical Functions](https://pymotw.com/3/math/index.html)
* [statistics — Statistical Calculations](https://pymotw.com/3/statistics/index.html)