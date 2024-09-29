# Python-Tutorials

My self-training in Python

# [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

[Python web site](https://www.python.org/)

[The Python Language Reference](https://docs.python.org/3/reference/index.html)

[The Python Standard Library](https://docs.python.org/3/library/index.html)

## 2. Using the Python Interpreter

### 2.1. Invoking the Interpreter

```
python
Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep 6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

```
python -c command [arg]
```

```
python -m module [arg]
```

Typing an end-of-file character (`Control-D` on Unix, `Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status.

`quit()`

### 2.1.1. Argument Passing

`import sys`
`sys.argv[0]`

### 2.1.2. Interactive Mode

```
python
Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```

## 2.2. The Interpreter and Its Environment¶

### 2.2.1. Source Code Encoding

By default, Python source files are treated as encoded in UTF-8.

# 3. An Informal Introduction to Pytho

001-example.py:

```
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```

```
py .\001-example.py
```

## 3.1. Using Python as a Calculator

### 3.1.1. Numbers

```
py
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5 # division always returns a floating-point number
1.6
>>> ^Z
```

The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part
(e.g. 5.0, 1.6) have type float. We will see more about numeric types later in the tutorial.

Division (/) always returns a float. To do floor division and get an integer result you can use the // operator; to calculate the remainder you can use %:

```
py
>>> 17 / 3 # classic division returns a float
5.666666666666667
>>> 17 // 3 # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2 # floored quotient * divisor + remainder
17
>>> ^Z
```

With Python, it is possible to use the \*\* operator to calculate powers

```
>>> 5 ** 2 # 5 squared
25
>>> 2 ** 7 # 2 to the power of 7
128
```

The equal sign (=) is used to assign a value to a variable.
Afterwards, no result is displayed before the next interactive prompt:

```
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:

```
>>> 4 * 3.75 - 1
14.0
```

In interactive mode, the last printed expression is assigned to the variable \_. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:

```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

This variable should be treated as read-only by the user. Don’t explicitly assign a value to it — you would create an independent local variable with the same name masking the built-in variable with its magic behavior.

In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction. Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).

### 3.1.2. Text

```
>>> 'spam eggs' # single quotes
'spam eggs'
>>> "Paris rabbit got your back :)! Yay!" # double quotes
'Paris rabbit got your back :)! Yay!'
>>> '1975'  # digits and numerals enclosed in quotes are also strings
'1975'
```

```
>>> "doesn't"  # ... or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```

The print() function produces a more readable output, by omitting the
enclosing quotes and by printing escaped and special characters:

```
>>> s = 'First line.\nSecond line.'  # \n means newLine
>>> s  # without print(), special characters are included in the string
'First line.\nSecond line.'
>>> print(s)  # with print, special characters are interpreted, so \n produces new line
First line.
Second line.
```

If you don’t want characters prefaced by \ to be interpreted as special characters,
you can use raw strings by adding an r before the first quote:

```
>>> print('C:\some\name')  # here \n means newline!
<stdin>:1: SyntaxWarning: invalid escape sequence '\s'
C:\some
ame
>>> print(r'C:\some\name') # note the r before the quote
C:\some\name
>>> print(r'C:\some\name\') # odd number of \ characters
  File "<stdin>", line 1
    print(r'C:\some\name\') # odd number of \ characters
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

There is one subtle aspect to raw strings: a raw string may not end in an
odd number of \ characters; see
[the FAQ entry](https://docs.python.org/3/faq/programming.html#faq-programming-raw-string-backslash)
for more information and workarounds.

String literals can span multiple lines. One way is using triple-quotes:
"""...""" or '''...'''. End of lines are automatically included in the
string, but it’s possible to prevent this by adding a \ at the end of the line.
The following example:

```
>>> print("""\
... Usage: thingy [OPTIONS]
...      -h                        Display this usage message
...      -H hostname               Hostname to connect to
... """)
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

>>>
```

Strings can be concatenated (glued together) with the + operator, and repeated with \*:

```
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

Two or more string literals (i.e. the ones enclosed between quotes)
next to each other are automatically concatenated.

```
>>> 'Py' 'thon'
'Python'
```

This feature is particularly useful when you want to break long strings:

```
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

This only works with two literals though, not with variables or expressions:

```
>>> prefix = 'Py'
>>> prefix 'thon' # can't concatenate a variable and a string literal.
  File "<stdin>", line 1
    prefix 'thon' # can't concatenate a variable and a string literal.
           ^^^^^^
SyntaxError: invalid syntax
>>> ('un' *3) 'ium'
  File "<stdin>", line 1
    ('un' *3) 'ium'
              ^^^^^
SyntaxError: invalid syntax
```

If you want to concatenate variables or a variable and a literal, use +:

```
>>> prefix + 'thon'
'Python'
```

Strings can be indexed (subscripted), with the first character having index 0.
There is no separate character type; a character is simply a string of size one:

```
>>> word = 'Python'
>>> word[0] # character in position 0
'P'
>>> word[5] # character in position 5
'n'
```

Indices may also be negative numbers, to start counting from the right:

```
>>> word[-1] # Last character
'n'
>>> word[-2] # second last character
'o'
>>> word[-6]
'P'
```

Note that since -0 is the same as 0, negative indices start from -1.

In addition to indexing, slicing is also supported. While indexing is
used to obtain individual characters, slicing allows you to obtain a
substring:

```
>>> word[0:2] # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5] # characters from positon 2 (included) to 5 (excluded)
'tho'
```

Slice indices have useful defaults; an omitted first index defaults to zero,
an omitted second index defaults to the size of the string being sliced.

```
>>> word[:2] # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:] # characters from position 4 (included) to the end
'on'
>>> word[-2:] # characters from the second-last (included) to the end
'on'
```

Note how the start is always included, and the end always excluded.
This makes sure that s[:i] + s[i:] is always equal to s:

```
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

One way to remember how slices work is to think of the indices as pointing
between characters, with the left edge of the first character numbered 0.
Then the right edge of the last character of a string of n characters has
index n, for example:

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

Attempting to use an index that is too large will result in an error:

However, out of range slice indexes are handled gracefully when used for slicing:

```
>>> word[42]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> word[4:42]
'on'
>>> word[42:]
''
```

Python strings cannot be changed — they are immutable.
Therefore, assigning to an indexed position in the string results in an error:

```
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

If you need a different string, you should create a new one:

```
>>> 'J' + word[1:]
'Jython'
```

The built-in function len() returns the length of a string:

```
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```
