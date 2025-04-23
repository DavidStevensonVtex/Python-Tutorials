# [mypy -- Getting Started](https://mypy.readthedocs.io/en/stable/getting_started.html)

This chapter introduces some core concepts of mypy, including function annotations, the [typing module](https://docs.python.org/3/library/typing.html#module-typing), stub files, and more.

If you’re looking for a quick intro, see the [mypy cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#cheat-sheet-py3).

If you’re unfamiliar with the concepts of static and dynamic type checking, be sure to read this chapter carefully, as the rest of the documentation may not make much sense otherwise.

## Installing and running mypy

Mypy requires Python 3.9 or later to run. You can install mypy using pip:

`$ python3 -m pip install mypy`

Once mypy is installed, run it by using the mypy tool:

`$ mypy program.py`

This command makes mypy type check your program.py file and print out any errors it finds. Mypy will type check your code statically: this means that it will check for errors without ever running your code, just like a linter.

This also means that you are always free to ignore the errors mypy reports, if you so wish. You can always use the Python interpreter to run your code, even if mypy reports errors.

However, if you try directly running mypy on your existing Python code, it will most likely report little to no errors. This is a feature! It makes it easy to adopt mypy incrementally.

In order to get useful diagnostics from mypy, you must add type annotations to your code. See the section below for details.

## Dynamic vs static typing

A function without type annotations is considered to be dynamically typed by mypy:

```
def greeting(name):
    return 'Hello ' + name
```

By default, mypy will **not** type check dynamically typed functions. This means that with a few exceptions, mypy will not report any errors with regular unannotated Python.

This is the case even if you misuse the function!

```
def greeting(name):
return 'Hello ' + name

# These calls will fail when the program runs, but mypy does not report an error

# because "greeting" does not have type annotations.

greeting(123)
greeting(b"Alice")
```

We can get mypy to detect these kinds of bugs by adding type annotations (also known as type hints). For example, you can tell mypy that greeting both accepts and returns a string like so:

```
# The "name: str" annotation says that the "name" argument should be a string

# The "-> str" annotation says that "greeting" will return a string

def greeting(name: str) -> str:
    return 'Hello ' + name
```

This function is now statically typed: mypy will use the provided type hints to detect incorrect use of the greeting function and incorrect use of variables within the greeting function. For example:

def greeting(name: str) -> str:
return 'Hello ' + name

greeting(3) # Argument 1 to "greeting" has incompatible type "int"; expected "str"
greeting(b'Alice') # Argument 1 to "greeting" has incompatible type "bytes"; expected "str"
greeting("World!") # No error

def bad*greeting(name: str) -> str:
return 'Hello ' * name # Unsupported operand types for \_ ("str" and "str")
Being able to pick whether you want a function to be dynamically or statically typed can be very helpful. For example, if you are migrating an existing Python codebase to use static types, it’s usually easier to migrate by incrementally adding type hints to your code rather than adding them all at once. Similarly, when you are prototyping a new feature, it may be convenient to initially implement the code using dynamic typing and only add type hints later once the code is more stable.

Once you are finished migrating or prototyping your code, you can make mypy warn you if you add a dynamic function by mistake by using the --disallow-untyped-defs flag. You can also get mypy to provide some limited checking of dynamically typed functions by using t
