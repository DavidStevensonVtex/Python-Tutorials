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

### 3.1.3. Lists

```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

Like strings (and all other built-in sequence types), lists can be indexed and sliced:

```
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```

Lists also support operations like concatenation:

```
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

```
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3 # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64
>>> cubes
[1, 8, 27, 64, 125]
```

You can also add new items at the end of the list, by using the list.append() method (we will see more about methods later):

```
>>> cubes.append(216) # add the cube of 6
>>> cubes.append(7 ** 3)        # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

Simple assignment in Python never copies data. When you assign a list to a variable,
the variable refers to the existing list. Any changes you make to the list through
one variable will be seen through all other variables that refer to it.:

```
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba) # they reference the same object
True
>>> rgba.append("Alph")
>>> rgb
['Red', 'Green', 'Blue', 'Alph']
```

All slice operations return a new list containing the requested elements.
This means that the following slice returns a shallow copy of the list:

```
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
['Red', 'Green', 'Blue', 'Alpha']
>>> rgba
['Red', 'Green', 'Blue', 'Alph']
```

Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

```
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = [ 'C', 'D', 'E' ]
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

The built-in function len() also applies to lists:

```
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

It is possible to nest lists (create lists containing other lists), for example:

```
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

### 3.2. First Steps Towards Programming

Of course, we can use Python for more complicated tasks than adding
two and two together. For instance, we can write an initial sub-sequence
of the Fibonacci series as follows:

```
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
```

```
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
```

The keyword argument end can be used to avoid the newline after the
output, or end the output with a different string:

```
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=', ')
...     a, b = b, a + b
...
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
```

# 4. More Control Flow Tools

## 4.1. if Statements

```
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```

## 4.2. for Statements

Python’s for statement iterates over the items of any sequence (a list or a string),
in the order that they appear in the sequence. For example (no pun intended):

```
>>> # Measure some strings:
>>> words = [ 'cat', 'window', 'defenestrate' ]
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

Code that modifies a collection while iterating over that same collection
can be tricky to get right. Instead, it is usually more straight-forward
to loop over a copy of the collection or to create a new collection:

```
>>> # Create a sample collection
>>> users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
>>>
>>> # Strategy: Iterate over a copy
>>> for user, status in users.copy().items():
...     if status == 'inactive':
...             del users[user]
...
>>> # Strategy: Create a new collection
>>> active_users = {}
>>> for user, status in users.items():
...     if status == 'active':
...             active_users[user] = status
...
>>> users
{'Hans': 'active', '景太郎': 'active'}
>>> active_users
{'Hans': 'active', '景太郎': 'active'}
```

## 4.3. The range() Function

If you do need to iterate over a sequence of numbers, the built-in
function range() comes in handy. It generates arithmetic progressions:

```
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):

```
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(-10, -100, -30))
[-10, -40, -70]
```

To iterate over the indices of a sequence, you can combine range() and len() as follows:

```
>>> a = [ ' Mary', 'had', 'a', 'little', 'lamb' ]
>>> for i in range(len(a)):
...     print(i, a[i])
...
0  Mary
1 had
2 a
3 little
4 lamb
```

In most such cases, however, it is convenient to use the
[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)
function, see Looping Techniques.

```
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

A strange thing happens if you just print a range:

```
>>> range(10)
range(0, 10)
```

In many ways the object returned by [range()](https://docs.python.org/3/library/stdtypes.html#range) behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.

We say such an object is [iterable](https://docs.python.org/3/glossary.html#term-iterable), that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. We have seen that the for statement is such a construct, while an example of a function that takes an iterable is sum():

```
>>> sum(range(4))  # 0 + 1 + 2 + 3
6
```

Later we will see more functions that return iterables and take iterables as arguments.
In chapter [Data Structures](https://docs.python.org/3/tutorial/datastructures.html#tut-structures),
we will discuss in more detail about [list()](https://docs.python.org/3/library/stdtypes.html#list).

## 4.4. break and continue Statements

The break statement breaks out of the innermost enclosing for or while loop:

```
>>> for n in range(2,10):
...     for x in range(2,n):
...             if n % x == 0:
...                     print(f"{n} equals {x} * {n//x}")
...                     break
...
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
```

The continue statement continues with the next iteration of the loop:

```
>>> for num in range(2,10):
...     if num % 2 == 0:
...             print(f"Found an even number {num}")
...             continue
...     print(f"Found an odd number {num}")
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

## 4.5. else Clauses on Loops

In a for or while loop the break statement may be paired with an else clause.
If the loop finishes without executing the break, the else clause executes.

In a for loop, the else clause is executed after the loop finishes its final
iteration, that is, if no break occurred.

In a while loop, it’s executed after the loop’s condition becomes false.

In either kind of loop, the else clause is not executed if the loop was
terminated by a break.

This is exemplified in the following for loop, which searches for prime numbers:

```
>>> for n in range(2,10):
...     for x in range(2,n):
...             if n % x == 0:
...                     print(n, 'equals', x, '*', n//x)
...                     break
...     else:
...             # Loop fell through without finding a factor
...             print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

(Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement.)

When used with a loop, the else clause has more in common with the else clause of a try statement than it does with that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs. For more on the try statement and exceptions, see Handling Exceptions.

## 4.6. pass Statements

The pass statement does nothing. It can be used when a statement is required
syntactically but the program requires no action. For example:

```
>>> while True:
...     pass # Busy-wait for keyboard input
```

This is commonly used for creating minimal classes:

```
>>> class MyEmptyClass:
...     pass
...
```

Another place pass can be used is as a place-holder for a function or
conditional body when you are working on new code, allowing you to keep
thinking at a more abstract level. The pass is silently ignored:

```
>>> def initlog(*args):
...     pass # Remember to implement this!
...
```

## 4.7. match Statements

A [match](https://docs.python.org/3/reference/compound_stmts.html#match) statement takes an expression and compares its value to successive patterns given as one or more case blocks. This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), but it’s more similar to pattern matching in languages like Rust or Haskell.

```
>>> status = 418
>>> def http_error(status):
...     match status:
...         case 400:
...             return "Bad request"
...         case 404:
...             return "Not found"
...         case 418:
...             return "I'm a teapot"
...         case _:
...             return "Something's wrong with the internet"
...
>>> print(http_error(status))
I'm a teapot
```

```
>>> x = 45
>>> y = 90
>>> point = (x,y)
>>> # point is an (x, y) tuple
>>> match point:
...     case (0, 0):
...         print("Origin")
...     case (0, y):
...         print(f"Y={y}")
...     case (x, 0):
...         print(f"X={x}")
...     case (x, y):
...         print(f"X={x}, Y={y}")
...     case _:
...         raise ValueError("Not a point")
...
X=45, Y=90
```

## 4.8. Defining Functions

```
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

# Results
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

## 4.9. More on Defining Functions

It is also possible to define functions with a variable number of arguments.
There are three forms, which can be combined.

4.9.3.5. Recap

The use case will determine which parameters to use in the function definition:

```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```

As guidance:

-   Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

-   Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

-   For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

# 5. Data Structures

This chapter describes some things you’ve learned about already in more detail, and adds some new things as well.

## 5.1. More on Lists

```
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

### 5.1.1. Using Lists as Stacks

```
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### 5.1.2. Using Lists as Queues

It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

```
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
>>> deque(['Michael', 'Terry', 'Graham'])
deque(['Michael', 'Terry', 'Graham'])
```

### 5.1.3. List Comprehensions

List comprehensions provide a concise way to create lists.

```
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Alternatively (not a list comprehension)

```
>>> squares = list(map(lambda x: x**2, range(10)))
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

or, equivalently:

```
>>> squares = [x**2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

```
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

and it’s equivalent to:

```
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

```
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> [-8, -4, 0, 4, 8]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> ['banana', 'loganberry', 'passion fruit']
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

List comprehensions can contain complex expressions and nested functions:

```
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### 5.1.4. Nested List Comprehensions

Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:

```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> matrix
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```

Transposing rows and columns means switching the data in a table
so that rows become columns and columns become rows.

The following list comprehension will transpose rows and columns:

```
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

Equivalent transposing example:

```
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

which, in turn, is the same as:

```
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

In the real world, you should prefer built-in functions to complex flow
statements. The zip() function would do a great job for this use case:

```
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

See
[Unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments)
for details on the asterisk in this line.

## 5.2. The del statement

There is a way to remove an item from a list given its
index instead of its value: the del statement.

```
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> a[:]
[-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

del can also be used to delete entire variables:

```
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

## 5.3. Tuples and Sequences

We saw that lists and strings have many common properties, such as indexing and slicing operations.
They are two examples of sequence data types
(see [Sequence Types](https://docs.python.org/3/library/stdtypes.html#typesseq) —
list, tuple, range).
Since Python is an evolving language, other sequence data types may be added.
There is also another standard sequence data type: the tuple.

A tuple consists of a number of values separated by commas, for instance:

```
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> (12345, 54321, 'hello!')
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

A special problem is the construction of tuples containing 0 or 1 items:
the syntax has some extra quirks to accommodate these. Empty tuples are
constructed by an empty pair of parentheses; a tuple with one item is
constructed by following a value with a comma (it is not sufficient to
enclose a single value in parentheses). Ugly, but effective.

```
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

This is called, appropriately enough, _sequence unpacking_ and works
for any sequence on the right-hand side. Sequence unpacking requires
that there are as many variables on the left side of the equals sign
as there are elements in the sequence. Note that multiple assignment
is really just a combination of tuple packing and sequence unpacking.

```
>>> t
(12345, 54321, 'hello!')
>>> x, y, z = t
>>> print(x, y, z)
12345 54321 hello!
```

## 5.4. Sets

Python also includes a data type for _sets_. A set is an unordered collection
with no duplicate elements. Basic uses include membership testing and
eliminating duplicate entries. Set objects also support mathematical
operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create
an empty set you have to use set(), not {}; the latter creates an empty dictionary,
a data structure that we discuss in the next section.

```
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'pear', 'apple', 'banana', 'orange'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False
>>>
>>> # Demonstrate set operations on unique letters from two words
>>>
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'d', 'r', 'b', 'c', 'a'}
>>> a - b                              # letters in a but not in b
{'d', 'r', 'b'}
>>> a | b                              # letters in a or b or both
{'d', 'r', 'b', 'z', 'l', 'c', 'm', 'a'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'m', 'd', 'r', 'b', 'z', 'l'}
```

Similarly to list comprehensions, set comprehensions are also supported:

```
>>> b = {x for x in 'abracadabra' }
>>> b
{'d', 'r', 'b', 'c', 'a'}
>>>
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'d', 'r'}
```

## 5.5. Dictionaries

Another useful data type built into Python is the dictionary
(see [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#typesmapping)).
Dictionaries are sometimes found in other languages as “associative memories” or
“associative arrays”. Unlike sequences, which are indexed by a range of numbers,
dictionaries are indexed by keys, which can be any immutable type; strings and
numbers can always be keys. Tuples can be used as keys if they contain only strings,
numbers, or tuples; if a tuple contains any mutable object either directly or
indirectly, it cannot be used as a key. You can’t use lists as keys, since lists
can be modified in place using index assignments, slice assignments, or methods
like append() and extend().

It is best to think of a dictionary as a set of key: value pairs, with the requirement
that the keys are unique (within one dictionary). A pair of braces creates an empty
dictionary: {}.
Placing a comma-separated list of key:value pairs within the braces adds initial
key:value pairs to the dictionary; this is also the way dictionaries are written
on output.

```
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
```

The [dict()](https://docs.python.org/3/library/stdtypes.html#dict)
constructor builds dictionaries directly from sequences of key-value pairs:

```
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

```
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

```
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## 5.6. Looping Techniques

hen looping through dictionaries, the key and corresponding value can be
retrieved at the same time using the
[items](https://docs.python.org/3/library/stdtypes.html#dict.items) method.

```
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

When looping through a **sequence**, the position index and corresponding value
can be retrieved at the same time using the
[enumerate()](https://docs.python.org/3/library/functions.html#enumerate) function.

```
for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

To loop over two or more sequences at the same time, the entries can be paired with the
[zip()](https://docs.python.org/3/library/functions.html#zip) function.

```
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

To loop over a sequence in reverse, first specify the sequence in
a forward direction and then call the reversed() function.

```
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

To loop over a sequence in sorted order, use the
[sorted()](https://docs.python.org/3/library/functions.html#sorted)
function which returns a new sorted list while leaving the source unaltered.

```
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```

Using
[set()](https://docs.python.org/3/library/stdtypes.html#set)
on a sequence eliminates duplicate elements. The use of
[sorted()](https://docs.python.org/3/library/functions.html#sorted)
in combination with
[set()](https://docs.python.org/3/library/stdtypes.html#set)
over a sequence is an idiomatic way to loop over unique elements of
the sequence in sorted order.

```
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

```
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

## 5.7. More on Conditions

```
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

## 5.8. Comparing Sequences and Other Types

Sequence objects typically may be compared to other objects with the same sequence type.

```
>>> (1, 2, 3)              < (1, 2, 4)
True
>>> [1, 2, 3]              < [1, 2, 4]
True
>>> 'ABC' < 'C' < 'Pascal' < 'Python'
True
>>> (1, 2, 3, 4)           < (1, 2, 4)
True
>>> (1, 2)                 < (1, 2, -1)
True
>>> (1, 2, 3)             == (1.0, 2.0, 3.0)
True
>>> (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
True
```

# 6. Modules

fibo.py

```
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

\_\_name\_\_ is the module name.

```
>>> import fibo
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.__name__
'fibo'
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 6.1. More on Modules

A module can contain executable statements as well as function definitions.
These statements are intended to initialize the module. They are executed
only the first time the module name is encountered in an import statement.
(They are also run if the file is executed as a script.)

Each module has its own private namespace, which is used as the global
namespace by all functions defined in the module.

```
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
>>> fib2(500)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
```

Note that in general the practice of importing \* from a module or package is
rowned upon, since it often causes poorly readable code. However, it is okay
to use it to save typing in interactive sessions.

```
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

```
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 6.1.1. Executing modules as scripts

Add this code to fibo.py:

```
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
```

When you run a Python module with

python fibo.py <arguments>

```
python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

If the module is imported, the code is not run:

```
>>> import fibo
>>>
```

### 6.1.2. The Module Search Path

When a module named spam is imported, the interpreter first searches for a
built-in module with that name. These module names are listed in
[sys.builtin_module_names](https://docs.python.org/3/library/sys.html#sys.builtin_module_names).

```
>>> import sys
>>> print(sys.builtin_module_names)
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha2', '_sha3', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tokenize', '_tracemalloc',
'_typing', '_warnings', '_weakref', '_winapi', '_xxinterpchannels', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')
```

If not found, it then searches for a file named spam.py in a list of directories
given by the variable [sys.path](https://docs.python.org/3/library/sys.html#sys.path).
sys.path is initialized from these locations:

-   python -m module command line: prepend the current working directory.

-   python script.py command line: prepend the script’s directory. If it’s a symbolic link, resolve symbolic links.

-   python -c code and python (REPL) command lines: prepend an empty string, which means the current working directory.

After initialization, Python programs can modify sys.path.

### 6.1.3. “Compiled” Python files

To speed up loading modules, Python caches the compiled version of each module
in the \_\_pycache\_\_ directory under the name module.version.pyc
