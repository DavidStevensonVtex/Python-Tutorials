# [Chapter 3 Algorithms](https://pymotw.com/3/algorithm_tools.html)

## [3.1 functools — Tools for Manipulating Functions](https://pymotw.com/3/functools/index.html)

Purpose:	Functions that operate on other functions.

The functools module provides tools for adapting or extending functions and other callable objects, without completely rewriting them.

### 3.1.1 Decorators

The primary tool supplied by the functools module is the class partial, which can be used to “wrap” a callable object with default arguments. The resulting object is itself callable and can be treated as though it is the original function. It takes all of the same arguments as the original, and can be invoked with extra positional or named arguments as well. A partial can be used instead of a lambda to provide default arguments to a function, while leaving some arguments unspecified.

#### 3.1.1.1 Partial Objects

This example shows two simple partial objects for the function myfunc(). The output of show_details() includes the func, args, and keywords attributes of the partial object.

```
# functools_partial.py
import functools


def myfunc(a, b=2):
    "Docstring for myfunc()."
    print("  called myfunc with:", (a, b))


def show_details(name, f, is_partial=False):
    "Show details of a callable object."
    print("{}:".format(name))
    print("  object:", f)
    if not is_partial:
        print("  __name__:", f.__name__)
    if is_partial:
        print("  func:", f.func)
        print("  args:", f.args)
        print("  keywords:", f.keywords)
    return


show_details("myfunc", myfunc)
myfunc("a", 3)
print()

# Set a different default value for 'b', but require
# the caller to provide 'a'.
p1 = functools.partial(myfunc, b=4)
show_details("partial with named default", p1, True)
p1("passing a")
p1("override b", b=5)
print()

# Set default values for both 'a' and 'b'.
p2 = functools.partial(myfunc, "default a", b=99)
show_details("partial with defaults", p2, True)
p2()
p2(b="override b")
print()

print("Insufficient arguments:")
p1()
```

At the end of the example, the first partial created is invoked without passing a value for a, causing an exception.

```
$ python3 functools_partial.py
myfunc:
  object: <function myfunc at 0x7fbec0168c10>
  __name__: myfunc
  called myfunc with: ('a', 3)

partial with named default:
  object: functools.partial(<function myfunc at 0x7fbec0168c10>, b=4)
  func: <function myfunc at 0x7fbec0168c10>
  args: ()
  keywords: {'b': 4}
  called myfunc with: ('passing a', 4)
  called myfunc with: ('override b', 5)

partial with defaults:
  object: functools.partial(<function myfunc at 0x7fbec0168c10>, 'default a', b=99)
  func: <function myfunc at 0x7fbec0168c10>
  args: ('default a',)
  keywords: {'b': 99}
  called myfunc with: ('default a', 99)
  called myfunc with: ('default a', 'override b')

Insufficient arguments:
Traceback (most recent call last):
  File "functools_partial.py", line 43, in <module>
    p1()
TypeError: myfunc() missing 1 required positional argument: 'a'
```

#### 3.1.1.2 Acquiring Function Properties

The partial object does not have `__name__` or `__doc_`_ attributes by default, and without those attributes, decorated functions are more difficult to debug. Using update_wrapper(), copies or adds attributes from the original function to the partial object.

```
# functools_update_wrapper.py
import functools


def myfunc(a, b=2):
    "Docstring for myfunc()."
    print("  called myfunc with:", (a, b))


def show_details(name, f):
    "Show details of a callable object."
    print("{}:".format(name))
    print("  object:", f)
    print("  __name__:", end=" ")
    try:
        print(f.__name__)
    except AttributeError:
        print("(no __name__)")
    print("  __doc__", repr(f.__doc__))
    print()


show_details("myfunc", myfunc)

p1 = functools.partial(myfunc, b=4)
show_details("raw wrapper", p1)

print("Updating wrapper:")
print("  assign:", functools.WRAPPER_ASSIGNMENTS)
print("  update:", functools.WRAPPER_UPDATES)
print()

functools.update_wrapper(p1, myfunc)
show_details("updated wrapper", p1)
```

The attributes added to the wrapper are defined in WRAPPER_ASSIGNMENTS, while WRAPPER_UPDATES lists values to be modified.

```
$ python3 functools_update_wrapper.py
myfunc:
  object: <function myfunc at 0x7fd222982ee0>
  __name__: myfunc
  __doc__ 'Docstring for myfunc().'

raw wrapper:
  object: functools.partial(<function myfunc at 0x7fd222982ee0>, b=4)
  __name__: (no __name__)
  __doc__ 'partial(func, *args, **keywords) - new function with partial application\n    of the given arguments and keywords.\n'

Updating wrapper:
  assign: ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
  update: ('__dict__',)

updated wrapper:
  object: functools.partial(<function myfunc at 0x7fd222982ee0>, b=4)
  __name__: myfunc
  __doc__ 'Docstring for myfunc().'

```

#### 3.1.1.3 Other Callables

Partials work with any callable object, not just with standalone functions.

```
# functools_callable.py
import functools


class MyClass:
    "Demonstration class for functools"

    def __call__(self, e, f=6):
        "Docstring for MyClass.__call__"
        print("  called object with:", (self, e, f))


def show_details(name, f):
    "Show details of a callable object."
    print("{}:".format(name))
    print("  object:", f)
    print("  __name__:", end=" ")
    try:
        print(f.__name__)
    except AttributeError:
        print("(no __name__)")
    print("  __doc__", repr(f.__doc__))
    return


o = MyClass()

show_details("instance", o)
o("e goes here")
print()

p = functools.partial(o, e="default for e", f=8)
functools.update_wrapper(p, o)
show_details("instance wrapper", p)
p()
```
This example creates partials from an instance of a class with a `__call__()` method.

```
$ python3 functools_callable.py
instance:
  object: <__main__.MyClass object at 0x7f43d3fa4df0>
  __name__: (no __name__)
  __doc__ 'Demonstration class for functools'
  called object with: (<__main__.MyClass object at 0x7f43d3fa4df0>, 'e goes here', 6)

instance wrapper:
  object: functools.partial(<__main__.MyClass object at 0x7f43d3fa4df0>, e='default for e', f=8)
  __name__: (no __name__)
  __doc__ 'Demonstration class for functools'
  called object with: (<__main__.MyClass object at 0x7f43d3fa4df0>, 'default for e', 8)
```