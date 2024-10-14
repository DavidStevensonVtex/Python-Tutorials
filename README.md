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

## 6.2. Standard Modules

Python comes with a library of standard modules, described in a separate document,
the Python Library Reference (“Library Reference” hereafter).

One particular module deserves some attention: sys, which is built into every Python
interpreter. The variables sys.ps1 and sys.ps2 define the strings used as primary
and secondary prompts:

```
>>>
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>>
>>> sys.ps1 = 'C> '
C> print('Yuck')
Yuck
```

These two variables are only defined if the interpreter is in interactive mode.

```
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
>>> sys.path
['', 'C:\\Program Files\\Python312\\python312.zip', 'C:\\Program Files\\Python312\\DLLs', 'C:\\Program Files\\Python312\\Lib', 'C:\\Program Files\\Python312', 'C:\\Program Files\\Python312\\Lib\\site-packages', '/ufs/guido/lib/python']
```

## 6.3. The [dir()](https://docs.python.org/3/library/functions.html#dir) Function

The built-in function dir() is used to find out which names a module defines.
It returns a sorted list of strings:

```
>>> import fibo, sys
>>> dir(fibo)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']
```

Without arguments, dir() lists the names you have defined currently:

```
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'fib', 'fibo']
```

dir() does not list the names of built-in functions and variables.
If you want a list of those, they are defined in the standard module
[builtins](https://docs.python.org/3/library/builtins.html#module-builtins):

```
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

## 6.4. Packages

Packages are a way of structuring Python’s module namespace by using “dotted module names”.
For example, the module name A.B designates a submodule named B in a package named A.
Just like the use of modules saves the authors of different modules from having to worry
about each other’s global variable names, the use of dotted module names saves the authors
of multi-module packages like NumPy or Pillow from having to worry about each other’s
module names.

The \_\_init\_\_.py files are required to make Python treat directories containing the
file as packages (unless using a namespace package, a relatively advanced feature).

In the simplest case, \_\_init\_\_.py can just be an empty file, but it can also execute
initialization code for the package or set the \_\_all\_\d\_ variable, described later.

```
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

An alternative way of importing the submodule is:

```
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)
```

```
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)
```

Note that when using from package import item, the item can be either a submodule
(or subpackage) of the package, or some other name defined in the package, like
a function, class or variable.

Contrarily, when using syntax like import item.subitem.subsubitem, each item except
for the last must be a package; the last item can be a module or a package but can’t
be a class or function or variable defined in the previous item.

### 6.4.1. Importing \* From a Package

Now what happens when the user writes from sound.effects import \*? Ideally, one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all. This could take a long time and importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the package. The import statement uses the following convention: if a package’s \_\_init\_\_.py code defines a list named \_\_all\_\_, it is taken to be the list of module names that should be imported when from package import \* is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released.

```
__all__ = ["echo", "surround", "reverse"]
```

This would mean that from sound.effects import \* would import the three
named submodules of the sound.effects package.

Be aware that submodules might become shadowed by locally defined names.

```
__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'
```

If \_\_all\_\_ is not defined, the statement from sound.effects import \* does not import all submodules

Although certain modules are designed to export only names that follow certain
patterns when you use import \*, it is still considered bad practice in
production code.

Remember, there is nothing wrong with using from package import
specific_submodule! In fact, this is the recommended notation unless the importing
module needs to use submodules with the same name from different packages.

### 6.4.2. Intra-package References

When packages are structured into subpackages (as with the sound package in the example),
you can use absolute imports to refer to submodules of siblings packages.

For example, if the module sound.filters.vocoder needs to use the echo module in the
sound.effects package, it can use from sound.effects import echo.

You can also write relative imports, with the from module import name form of import statement.
These imports use leading dots to indicate the current and parent packages involved in the
relative import. From the surround module for example, you might use:

```
from . import echo
from .. import formats
from ..filters import equalizer
```

Note that relative imports are based on the name of the current module.
Since the name of the main module is always "**main**", modules intended for use
as the main module of a Python application must always use absolute imports.

### 6.4.3. Packages in Multiple Directories

Packages support one more special attribute,
[\_\_path\_\_](https://docs.python.org/3/reference/datamodel.html#module.__path__).
This is initialized to be a sequence of strings containing the name of the directory
holding the package’s \_\_init\_\_.py before the code in that file is executed.
This variable can be modified; doing so affects future searches for modules and
subpackages contained in the package.

While this feature is not often needed, it can be used to extend the set of modules found in a package.

# 7. Input and Output

## 7.1. Fancier Output Formatting

So far we’ve encountered two ways of writing values: expression statements and the
[print()](https://docs.python.org/3/library/functions.html#print) function.
(A third way is using the
[write()](https://docs.python.org/3/library/io.html#io.TextIOBase.write)
method of file objects; the standard output file can be referenced as
sys.stdout.
See the Library Reference for more information on this.)

-   To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.

```
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

-   The [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) method of strings requires more manual effort. You’ll still use { and } to mark where a variable will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information to be formatted.

```
>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'
```

```
>>> yes_votes = 42_572_654
>>> total_votes = 85_705_149
>>> percentage = yes_votes / total_votes
>>>
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

(see [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec) for details).

When you don’t need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the [repr()](https://docs.python.org/3/library/functions.html#repr) or
[str()](https://docs.python.org/3/library/stdtypes.html#str) functions.

```
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> s
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument tot repr() may be any Python object:
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

### 7.1.1. Formatted String Literals

[Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

```
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.

```
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():

```
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My overcraft is full of {animals!r}.')
My overcraft is full of 'eels'.
```

The = specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:

```
>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs} {count=} {area=}')
Debugging roaches count=13 area='living room'
```

### 7.1.2. The String format() Method

Basic usage of the str.format() method looks like this:

```
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.

```
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.

```
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

If you have a really long format string that you don’t want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets '[]' to access the keys.

```
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

This could also be done by passing the table dictionary as keyword arguments with the \*\* notation.

```
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

As an example, the following lines produce a tidily aligned set of columns giving integers and their squares and cubes:

```
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

For a complete overview of string formatting with str.format(), see
[Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings).

### 7.1.3. Manual String Formatting

```
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

```
>>> for x in range(1,11):
...     print(str(x).rjust(2), str(x*x).rjust(3), str(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

There is another method, str.zfill(), which pads a numeric string on the left
with zeros. It understands about plus and minus signs:

```
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

### 7.1.4. Old string formatting

The % operator (modulo) can also be used for string formatting. Given format % values (where format is a string), % conversion specifications in format are replaced with zero or more elements of values. This operation is commonly known as string interpolation. For example:

```
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

More information can be found in the
[printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting) section.

## 7.2. Reading and Writing Files

[open()](https://docs.python.org/3/library/functions.html#open)
returns a [file object](https://docs.python.org/3/glossary.html#term-file-object),
and is most commonly used with two positional arguments
and one keyword argument: open(filename, mode, encoding=None)

The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent.

Because UTF-8 is the modern de-facto standard, encoding="utf-8" is recommended unless you know that you need to use a different encoding. Appending a 'b' to the mode opens the file in binary mode. Binary mode data is read and written as bytes objects. You can not specify encoding when opening file in binary mode.

In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n.

When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files.

```
>>> with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()
...     print(read_data)
...
The rain in Spain falls mainly in the plain.
The rain in Spain falls mainly in the plain.
The rain in Spain falls mainly in the plain.
The rain in Spain falls mainly in the plain.
```

If you’re not using the
[with](https://docs.python.org/3/reference/compound_stmts.html#with)
keyword, then you should call f.close() to close the file and immediately free up any system resources used by it.

After a file object is closed, either by a with statement or by calling f.close(), attempts to use the file object will automatically fail.

### 7.2.1. Methods of File Objects

The rest of the examples in this section will assume that a file object called f has already been created.

To read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric argument.

When size is omitted or negative, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory.

f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline.

For reading lines from a file, you can loop over the file object.
This is memory efficient, fast, and leads to simple code:

```
>>> with open('workfile', encoding="utf-8") as f:
...     for line in f:
...             print(line, end='')
...
This is the first line of the file.
Second line of the file
```

f.write(string) writes the contents of string to the file, returning the number of characters written.

Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:

```
>>> with open('outputfile', 'w', encoding="utf-8") as f:
...     value = ('the answer', 42)
...     s = str(value)
...     f.write(s)
...
18
```

outputfile:

```
('the answer', 42)
```

```
>>> f = open('outputfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)    # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3,2)  # Go to the 3rd byte before the end
15
>>> f.read(1)
b'f'
```

### 7.2.2. Saving structured data with [json](https://docs.python.org/3/library/json.html#module-json)

The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

```
>>> import json
>>> x = [1, 'simple', 'list' ]
>>> json.dumps(x)
'[1, "simple", "list"]'
```

Another variant of the dumps() function, called dump(), simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:

```
json.dump(x, f)
```

To decode the object again, if f is a binary file or text file object which has been opened for reading:

```
x = json.load(f)
```

**Note:** JSON files must be encoded in UTF-8.
Use encoding="utf-8" when opening JSON file
as a text file for both of reading and writing.

This simple serialization technique can handle lists and dictionaries, but serializing arbitrary class instances in JSON requires a bit of extra effort.
The reference for the
[json](https://docs.python.org/3/library/json.html#module-json)
module contains an explanation of this.

See also pickle - the pickle module

Contrary to JSON,
[pickle](https://docs.python.org/3/library/pickle.html#module-pickle)
is a protocol which allows the serialization of arbitrarily complex Python objects. As such, it is specific to Python and cannot be used to communicate with applications written in other languages. It is also insecure by default: deserializing pickle data coming from an untrusted source can execute arbitrary code, if the data was crafted by a skilled attacker.

# 8. Errors and Exceptions

## 8.1. Syntax Errors

```
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

The parser repeats the offending line and displays little ‘arrow’s pointing at the token in the line where the error was detected.

## 8.2. Exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here:

```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam * 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) lists the built-in exceptions and their meanings.

## 8.3. Handling Exceptions

```
>>> while True:
...     try:
...             x = int(input("Please enter a number: "))
...     except ValueError:
...             print("Oops!  That was no valid number.  Try again...")
...
Please enter a number: abc
Oops!  That was no valid number.  Try again...
Please enter a number: 123
```

A try statement may have more than one except clause, to specify handlers for different exceptions.

```
... except (RuntimeError, TypeError, NameError):
...     pass
```

A class in an except clause matches exceptions which are instances of the class itself or one of its derived classes (but not the other way around — an except clause listing a derived class does not match instances of its base classes).

```
>>> class B(Exception):
...     pass
...
>>> class C(B):
...     pass
...
>>> class D(C):
...     pass
...
>>> for cls in [B, C, D]:
...     try:
...         raise cls()
...     except D:
...         print("D")
...     except C:
...         print("C")
...     except B:
...         print("B")
...
B
C
D
```

```
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception type
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

BaseException is the common base class of all exceptions.

One of its subclasses, Exception, is the base class of all the non-fatal exceptions.

Exceptions which are not subclasses of Exception are not typically handled, because they are used to indicate that the program should terminate. They include SystemExit which is raised by sys.exit() and KeyboardInterrupt which is raised when a user wishes to interrupt the program.

The most common pattern for handling Exception is to print or log the exception and then re-raise it (allowing a caller to handle the exception as well):

```
>>> import sys
>>>
>>> try:
...     f = open('myfile.txt')
...     s = f.readline()
...     i = int(s.strip())
... except OSError as err:
...     print("OS error:", err)
... except ValueError:
...     print("Could not convert data to an integer.")
... except Exception as err:
...     print(f"Unexpected {err=}, {type(err)=}")
...     raise
...
OS error: [Errno 2] No such file or directory: 'myfile.txt'
```

The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception.

Exception handlers do not handle only exceptions that occur immediately in the try clause, but also those that occur inside functions that are called (even indirectly) in the try clause. For example:

```
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## 8.4. Raising Exceptions

The raise statement allows the programmer to force a specified exception to occur. For example:

```
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from BaseException, such as Exception or one of its subclasses). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:

```
>>> raise ValueError  # shorthand for 'raise ValueError()'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError
```

If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception:

```
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

## 8.5. Exception Chaining

If an unhandled exception occurs inside an except section, it will have the exception being handled attached to it and included in the error message:

```
>>> try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: unable to handle error
```

To indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause:

```
# exc must be exception instance or None.
raise RuntimeError from exc
```

This can be useful when you are transforming exceptions. For example:

```
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

It also allows disabling automatic exception chaining using the from None idiom:

```
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

For more information about chaining mechanics, see
[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).

## 8.6. User-defined Exceptions

Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes). Exceptions should typically be derived from the Exception class, either directly or indirectly.

Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception.

Most exceptions are defined with names that end in “Error”, similar to the naming of the standard exceptions.

## 8.7. Defining Clean-up Actions

The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances. For example:

```
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception.

-   If an exception occurs during execution of the try clause, the exception may be handled by an except clause.

```
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

```
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
```

In real world applications, the finally clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

## 8.8. Predefined Clean-up Actions

```
for line in open("myfile.txt"):
    print(line, end="")
```

The problem with this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing.

The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

```
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

After the statement is executed, the file f is always closed, even if a problem was encountered while processing the lines.
