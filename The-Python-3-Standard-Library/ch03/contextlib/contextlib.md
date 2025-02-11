# [Chapter 3 Algorithms](https://pymotw.com/3/algorithm_tools.html)

## [3.4 contextlib — Context Manager Utilities](https://pymotw.com/3/contextlib/index.html)

Purpose:	Utilities for creating and working with context managers.

The contextlib module contains utilities for working with context managers and the with statement.

### 3.4.1 Context Manager API

A context manager is responsible for a resource within a code block, possibly creating it when the block is entered and then cleaning it up after the block is exited. For example, files support the context manager API to make it easy to ensure they are closed after all reading or writing is done.

```
# contextlib_file.py
with open('/tmp/pymotw.txt', 'wt') as f:
    f.write('contents go here')
# file is automatically closed
```

A context manager is enabled by the with statement, and the API involves two methods. The `__enter__()` method is run when execution flow enters the code block inside the with. It returns an object to be used within the context. When execution flow leaves the with block, the `__exit__()` method of the context manager is called to clean up any resources being used.

```
# contextlib_api.py
class Context:

    def __init__(self):
        print("__init__()")

    def __enter__(self):
        print("__enter__()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__()")


with Context():
    print("Doing work in the context")
```

Combining a context manager and the with statement is a more compact way of writing a try:finally block, since the context manager’s `__exit__()` method is always called, even if an exception is raised.

```
$ python3 contextlib_api.py
__init__()
__enter__()
Doing work in the context
__exit__()
```

The `__enter__()` method can return any object to be associated with a name specified in the as clause of the with statement. In this example, the Context returns an object that uses the open context.

```
# contextlib_api_other_object.py
class WithinContext:

    def __init__(self, context):
        print("WithinContext.__init__({})".format(context))

    def do_something(self):
        print("WithinContext.do_something()")

    def __del__(self):
        print("WithinContext.__del__")


class Context:

    def __init__(self):
        print("Context.__init__()")

    def __enter__(self):
        print("Context.__enter__()")
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Context.__exit__()")


with Context() as c:
    c.do_something()
```

The value associated with the variable c is the object returned by `__enter__()`, which is not necessarily the Context instance created in the with statement.

```
$ python3 contextlib_api_other_object.py
Context.__init__()
Context.__enter__()
WithinContext.__init__(<__main__.Context object at 0x7f5955071040>)
WithinContext.do_something()
Context.__exit__()
WithinContext.__del__
```

The `__exit__()` method receives arguments containing details of any exception raised in the with block.

```
# contextlib_api_error.py
class Context:

    def __init__(self, handle_error):
        print("__init__({})".format(handle_error))
        self.handle_error = handle_error

    def __enter__(self):
        print("__enter__()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__()")
        print("  exc_type =", exc_type)
        print("  exc_val  =", exc_val)
        print("  exc_tb   =", exc_tb)
        return self.handle_error


with Context(True):
    raise RuntimeError("error message handled")

print()

with Context(False):
    raise RuntimeError("error message propagated")
```

If the context manager can handle the exception, `__exit__()` should return a true value to indicate that the exception does not need to be propagated. Returning false causes the exception to be re-raised after `__exit__() `returns.

```
$ python3 contextlib_api_error.py
__init__(True)
__enter__()
__exit__()
  exc_type = <class 'RuntimeError'>
  exc_val  = error message handled
  exc_tb   = <traceback object at 0x7fe9b4d98880>

__init__(False)
__enter__()
__exit__()
  exc_type = <class 'RuntimeError'>
  exc_val  = error message propagated
  exc_tb   = <traceback object at 0x7fe9b4d98880>
Traceback (most recent call last):
  File "contextlib_api_error.py", line 26, in <module>
    raise RuntimeError("error message propagated")
RuntimeError: error message propagated
```

### 3.4.2 Context Managers as Function Decorators

The class ContextDecorator adds support to regular context manager classes to let them be used as function decorators as well as context managers.

```
# contextlib_decorator.py
import contextlib


class Context(contextlib.ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        print("__init__({})".format(how_used))

    def __enter__(self):
        print("__enter__({})".format(self.how_used))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__({})".format(self.how_used))


@Context("as decorator")
def func(message):
    print(message)


print()
with Context("as context manager"):
    print("Doing work in the context")

print()
func("Doing work in the wrapped function")
```

One difference with using the context manager as a decorator is that the value returned by `__enter__()` is not available inside the function being decorated, unlike when using with and as. Arguments passed to the decorated function are available in the usual way.

```
$ python3 contextlib_decorator.py
__init__(as decorator)

__init__(as context manager)
__enter__(as context manager)
Doing work in the context
__exit__(as context manager)

__enter__(as decorator)
Doing work in the wrapped function
__exit__(as decorator)
```

### 3.4.3 From Generator to Context Manager

Creating context managers the traditional way, by writing a class with __enter__() and __exit__() methods, is not difficult. But sometimes writing everything out fully is extra overhead for a trivial bit of context. In those sorts of situations, use the contextmanager() decorator to convert a generator function into a context manager.

```
# contextlib_contextmanager.py
import contextlib


@contextlib.contextmanager
def make_context():
    print("  entering")
    try:
        yield {}
    except RuntimeError as err:
        print("  ERROR:", err)
    finally:
        print("  exiting")


print("Normal:")
with make_context() as value:
    print("  inside with statement:", value)

print("\nHandled error:")
with make_context() as value:
    raise RuntimeError("showing example of handling an error")

print("\nUnhandled error:")
with make_context() as value:
    raise ValueError("this exception is not handled")
```

The generator should initialize the context, yield exactly one time, then clean up the context. The value yielded, if any, is bound to the variable in the as clause of the with statement. Exceptions from within the with block are re-raised inside the generator, so they can be handled there.

```
$ python3 contextlib_contextmanager.py
Normal:
  entering
  inside with statement: {}
  exiting

Handled error:
  entering
  ERROR: showing example of handling an error
  exiting

Unhandled error:
  entering
  exiting
Traceback (most recent call last):
  File "contextlib_contextmanager.py", line 26, in <module>
    raise ValueError("this exception is not handled")
ValueError: this exception is not handled
```

The context manager returned by contextmanager() is derived from ContextDecorator, so it also works as a function decorator.

```
# contextlib_contextmanager_decorator.py
import contextlib


@contextlib.contextmanager
def make_context():
    print("  entering")
    try:
        # Yield control, but not a value, because any value
        # yielded is not available when the context manager
        # is used as a decorator.
        yield
    except RuntimeError as err:
        print("  ERROR:", err)
    finally:
        print("  exiting")


@make_context()
def normal():
    print("  inside with statement")


@make_context()
def throw_error(err):
    raise err


print("Normal:")
normal()

print("\nHandled error:")
throw_error(RuntimeError("showing example of handling an error"))

print("\nUnhandled error:")
throw_error(ValueError("this exception is not handled"))
```

As in the ContextDecorator example above, when the context manager is used as a decorator the value yielded by the generator is not available inside the function being decorated. Arguments passed to the decorated function are still available, as demonstrated by throw_error() in this example.

```
$ python3 contextlib_contextmanager_decorator.py
Normal:
  entering
  inside with statement
  exiting

Handled error:
  entering
  ERROR: showing example of handling an error
  exiting

Unhandled error:
  entering
  exiting
Traceback (most recent call last):
  File "contextlib_contextmanager_decorator.py", line 36, in <module>
    throw_error(ValueError("this exception is not handled"))
  File "/usr/lib/python3.8/contextlib.py", line 75, in inner
    return func(*args, **kwds)
  File "contextlib_contextmanager_decorator.py", line 26, in throw_error
    raise err
ValueError: this exception is not handled
```