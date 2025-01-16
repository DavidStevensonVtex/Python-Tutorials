 # Python String Methods

Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

Method	Description
* capitalize()	Converts the first character to upper case
* casefold()	Converts string into lower case
* center()	Returns a centered string
* count()	Returns the number of times a specified value occurs in a string
* encode()	Returns an encoded version of the string
* endswith()	Returns true if the string ends with the specified value
* expandtabs()	Sets the tab size of the string
* find()	Searches the string for a specified value and returns the position of where it was found
* format()	Formats specified values in a string
* format_map()	Formats specified values in a string
* index()	Searches the string for a specified value and returns the position of where it was found
* isalnum()	Returns True if all characters in the string are alphanumeric
* isalpha()	Returns True if all characters in the string are in the alphabet
* isascii()	Returns True if all characters in the string are ascii characters
* isdecimal()	Returns True if all characters in the string are decimals
* isdigit()	Returns True if all characters in the string are digits
* isidentifier()	Returns True if the string is an identifier
* islower()	Returns True if all characters in the string are lower case
* isnumeric()	Returns True if all characters in the string are numeric
* isprintable()	Returns True if all characters in the string are printable
* isspace()	Returns True if all characters in the string are whitespaces
* istitle()	Returns True if the string follows the rules of a title
* isupper()	Returns True if all characters in the string are upper case
* join()	Converts the elements of an iterable into a string
* ljust()	Returns a left justified version of the string
* lower()	Converts a string into lower case
* lstrip()	Returns a left trim version of the string
* maketrans()	Returns a translation table to be used in translations
* partition()	Returns a tuple where the string is parted into three parts
* replace()	Returns a string where a specified value is replaced with a specified value
* rfind()	Searches the string for a specified value and returns the last position of where it was found
* rindex()	Searches the string for a specified value and returns the last position of where it was found
* rjust()	Returns a right justified version of the string
* rpartition()	Returns a tuple where the string is parted into three parts
* rsplit()	Splits the string at the specified separator, and returns a list
* rstrip()	Returns a right trim version of the string
* split()	Splits the string at the specified separator, and returns a list
* splitlines()	Splits the string at line breaks and returns a list
* startswith()	Returns true if the string starts with the specified value
* strip()	Returns a trimmed version of the string
* swapcase()	Swaps cases, lower case becomes upper case and vice versa
* title()	Converts the first character of each word to upper case
* translate()	Returns a translated string
* upper()	Converts a string into upper case
* zfill()	Fills the string with a specified number of 0 values at the beginning

Note: All string methods returns new values. They do not change the original string.

Learn more about strings in our [Python Strings Tutorial](https://www.w3schools.com/python/python_strings.asp).


# [Python math Module](https://www.w3schools.com/python/module_math.asp)

Python has a built-in module that you can use for mathematical tasks.

The math module has a set of methods and constants.

## Math Methods

Method	Description
* math.acos()	Returns the arc cosine of a number
* math.acosh()	Returns the inverse hyperbolic cosine of a number
* math.asin()	Returns the arc sine of a number
* math.asinh()	Returns the inverse hyperbolic sine of a number
* math.atan()	Returns the arc tangent of a number in radians
* math.atan2()	Returns the arc tangent of y/x in radians
* math.atanh()	Returns the inverse hyperbolic tangent of a number
* math.ceil()	Rounds a number up to the nearest integer
* math.comb()	Returns the number of ways to choose k items from n items without repetition and order
* math.copysign()	Returns a float consisting of the value of the first parameter and the sign of the second parameter
* math.cos()	Returns the cosine of a number
* math.cosh()	Returns the hyperbolic cosine of a number
* math.degrees()	Converts an angle from radians to degrees
* math.dist()	Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
* math.erf()	Returns the error function of a number
* math.erfc()	Returns the complementary error function of a number
* math.exp()	Returns E raised to the power of x
* math.expm1()	Returns Ex - 1
* math.fabs()	Returns the absolute value of a number
* math.factorial()	Returns the factorial of a number
* math.floor()	Rounds a number down to the nearest integer
* math.fmod()	Returns the remainder of x/y
* math.frexp()	Returns the mantissa and the exponent, of a specified number
* math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
* math.gamma()	Returns the gamma function at x
* math.gcd()	Returns the greatest common divisor of two integers
* math.hypot()	Returns the Euclidean norm
* math.isclose()	Checks whether two values are close to each other, or not
* math.isfinite()	Checks whether a number is finite or not
* math.isinf()	Checks whether a number is infinite or not
* math.isnan()	Checks whether a value is NaN (not a number) or not
* math.isqrt()	Rounds a square root number downwards to the nearest integer
* math.ldexp()	Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
* math.lgamma()	Returns the log gamma value of x
* math.log()	Returns the natural logarithm of a number, or the logarithm of number to base
* math.log10()	Returns the base-10 logarithm of x
* math.log1p()	Returns the natural logarithm of 1+x
* math.log2()	Returns the base-2 logarithm of x
* math.perm()	Returns the number of ways to choose k items from n items with order and without repetition
* math.pow()	Returns the value of x to the power of y
* math.prod()	Returns the product of all the elements in an iterable
* math.radians()	Converts a degree value into radians
* math.remainder()	Returns the closest value that can make numerator completely divisible by the denominator
* math.sin()	Returns the sine of a number
* math.sinh()	Returns the hyperbolic sine of a number
* math.sqrt()	Returns the square root of a number
* math.tan()	Returns the tangent of a number
* math.tanh()	Returns the hyperbolic tangent of a number
* math.trunc()	Returns the truncated integer parts of a number

Math Constants
Constant	Description
* math.e	Returns Euler's number (2.7182...)
* math.inf	Returns a floating-point positive infinity
* math.nan	Returns a floating-point NaN (Not a Number) value
* math.pi	Returns PI (3.1415...)
* math.tau	Returns tau (6.2831...)