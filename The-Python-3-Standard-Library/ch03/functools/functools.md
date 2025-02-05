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

#### 3.1.1.4 Methods and Functions

While partial() returns a callable ready to be used directly, partialmethod() returns a callable ready to be used as an unbound method of an object. In the following example, the same standalone function is added as an attribute of MyClass twice, once using partialmethod() as method1() and again using partial() as method2().

```
# functools_partialmethod.py
import functools


def standalone(self, a=1, b=2):
    "Standalone function"
    print("  called standalone with:", (self, a, b))
    if self is not None:
        print("  self.attr =", self.attr)


class MyClass:
    "Demonstration class for functools"

    def __init__(self):
        self.attr = "instance attribute"

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)


o = MyClass()

print("standalone")
standalone(None)
print()

print("method1 as partialmethod")
o.method1()
print()

print("method2 as partial")
try:
    o.method2()
except TypeError as err:
    print("ERROR: {}".format(err))

```

method1() can be called from an instance of MyClass, and the instance is passed as the first argument just as with methods defined normally. method2() is not set up as a bound method, and so the self argument must be passed explicitly, or the call will result in a TypeError.

```
$ python3 functools_partialmethod.py
standalone
  called standalone with: (None, 1, 2)

method1 as partialmethod
  called standalone with: (<__main__.MyClass object at 0x7f60d8e30f70>, 1, 2)
  self.attr = instance attribute

method2 as partial
ERROR: standalone() missing 1 required positional argument: 'self'
```

#### 3.1.1.5 Acquiring Function Properties for Decorators

Updating the properties of a wrapped callable is especially useful when used in a decorator, since the transformed function ends up with properties of the original “bare” function.

```
# functools_wraps.py
import functools


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


def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a="decorated defaults", b=1):
        print("  decorated:", (a, b))
        print("  ", end=" ")
        return f(a, b=b)

    return decorated


def myfunc(a, b=2):
    "myfunc() is not complicated"
    print("  myfunc:", (a, b))
    return


# The raw function
show_details("myfunc", myfunc)
myfunc("unwrapped, default b")
myfunc("unwrapped, passing b", 3)
print()

# Wrap explicitly
wrapped_myfunc = simple_decorator(myfunc)
show_details("wrapped_myfunc", wrapped_myfunc)
wrapped_myfunc()
wrapped_myfunc("args to wrapped", 4)
print()


# Wrap with decorator syntax
@simple_decorator
def decorated_myfunc(a, b):
    myfunc(a, b)
    return


show_details("decorated_myfunc", decorated_myfunc)
decorated_myfunc()
decorated_myfunc("args to decorated", 4)
```

functools provides a decorator, wraps(), that applies update_wrapper() to the decorated function.

```
$ python3 functools_wraps.py
myfunc:
  object: <function myfunc at 0x7f26dfdd4040>
  __name__: myfunc
  __doc__ 'myfunc() is not complicated'

  myfunc: ('unwrapped, default b', 2)
  myfunc: ('unwrapped, passing b', 3)

wrapped_myfunc:
  object: <function myfunc at 0x7f26dfdd40d0>
  __name__: myfunc
  __doc__ 'myfunc() is not complicated'

  decorated: ('decorated defaults', 1)
     myfunc: ('decorated defaults', 1)
  decorated: ('args to wrapped', 4)
     myfunc: ('args to wrapped', 4)

decorated_myfunc:
  object: <function decorated_myfunc at 0x7f26dfdd41f0>
  __name__: decorated_myfunc
  __doc__ None

  decorated: ('decorated defaults', 1)
     myfunc: ('decorated defaults', 1)
  decorated: ('args to decorated', 4)
     myfunc: ('args to decorated', 4)
```

### 3.1.2 Comparison

Under Python 2, classes could define a `__cmp__()` method that returns -1, 0, or 1 based on whether the object is less than, equal to, or greater than the item being compared. Python 2.1 introduced the rich comparison methods API (`__lt__()`, `__le__()`, `__eq__()`, `__ne__()`, `__gt__()`, and `__ge__()`), which perform a single comparison operation and return a boolean value. Python 3 deprecated `__cmp__()` in favor of these new methods and functools provides tools to make it easier to write classes that comply with the new comparison requirements in Python 3.

Rich Comparison

The rich comparison API is designed to allow classes with complex comparisons to implement each test in the most efficient way possible. However, for classes where comparison is relatively simple, there is no point in manually creating each of the rich comparison methods. The total_ordering() class decorator takes a class that provides some of the methods, and adds the rest of them.

```
# functools_total_ordering.py
import functools
import inspect
from pprint import pprint


@functools.total_ordering
class MyObject:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print("  testing __eq__({}, {})".format(self.val, other.val))
        return self.val == other.val

    def __gt__(self, other):
        print("  testing __gt__({}, {})".format(self.val, other.val))
        return self.val > other.val


print("Methods:\n")
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a = MyObject(1)
b = MyObject(2)

print("\nComparisons:")
for expr in ["a < b", "a <= b", "a == b", "a >= b", "a > b"]:
    print("\n{:<6}:".format(expr))
    result = eval(expr)
    print("  result of {}: {}".format(expr, result))
```

The class must provide implementation of `__eq__()` and one other rich comparison method. The decorator adds implementations of the rest of the methods that work by using the comparisons provided. If a comparison cannot be made, the method should return NotImplemented so the comparison can be tried using the reverse comparison operators on the other object, before failing entirely.

```
$ python3 functools_total_ordering.py
Methods:

[('__eq__', <function MyObject.__eq__ at 0x7f02402eee50>),
 ('__ge__', <function _ge_from_gt at 0x7f02403bd310>),
 ('__gt__', <function MyObject.__gt__ at 0x7f02402eeee0>),
 ('__init__', <function MyObject.__init__ at 0x7f02402eedc0>),
 ('__le__', <function _le_from_gt at 0x7f02403bd3a0>),
 ('__lt__', <function _lt_from_gt at 0x7f02403bd280>)]

Comparisons:

a < b :
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a < b: True

a <= b:
  testing __gt__(1, 2)
  result of a <= b: True

a == b:
  testing __eq__(1, 2)
  result of a == b: False

a >= b:
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a >= b: False

a > b :
  testing __gt__(1, 2)
  result of a > b: False
```