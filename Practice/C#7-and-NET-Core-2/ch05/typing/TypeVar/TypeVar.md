# [`TypeVar`s explained](https://dev.to/decorator_factory/typevars-explained-hmo)

If you're totally unfamiliar with type annotations in Python, my [previous article](https://dev.to/decorator_factory/type-hints-in-python-tutorial-3pel) should get you started.

In this post, I'm going to show you how to use type variables, or TypeVars, for fun and profit.

## The problem

This function accepts anything as the argument and returns it as is. How do you explain to the type checker that the return type is the same as the type of arg?

```
def identity(arg):
    return arg
```

## Why not use Any?

```
def identity(arg: Any) -> Any:
    return arg
```

If you use `Any`, the type checker will not understand how this function works: as far as it's concerned, the function can return anything at all. The return type doesn't depend on the type of `arg`.

We'd really want `number` to be an `int` here, so that the type checker will catch an error on the next line:

## Why not specialize the function for different types?

```
def identity_int(arg: int) -> int:
    return arg


def identity_str(arg: str) -> str:
    return arg


def identity_list_str(arg: list[str]) -> list[str]:
    return arg
```

1.  This doesn't scale well. Are you going to replicate the same function 10 times? Will you remember to keep them in sync?

2.  What if this is a library function? You won't be able to predict all the ways people will use this function.

## The solution: type variables

Type variables allow you to link several types together. This is how you can use a type variable to annotate the identity function:

```
from typing import TypeVar

T = TypeVar("T")


def identity(arg: T) -> T:
    return arg


number = identity(42)
# Operator "+" not supported for types "int" and "Literal['!']"Pylance
print(number + "!")

# $ mypy identity-solution.py
# identity-solution.py:12: error: Unsupported operand types for + ("int" and "str")  [operator]
# Found 1 error in 1 file (checked 1 source file)

# $ pyright identity-solution.py
# d:\drs\Python\GitHub\Python-Tutorials\Practice\C#7-and-NET-Core-2\ch05\typing\TypeVar\identity-solution.py
#   d:\drs\Python\GitHub\Python-Tutorials\Practice\C#7-and-NET-Core-2\ch05\typing\TypeVar\identity-solution.py:12:7 - error: Operator "+" not supported for types "int" and "Literal['!']" (reportOperatorIssue)
# 1 error, 0 warnings, 0 informations
```

Here the return type is "linked" to the parameter type: whatever you put into the function, the same thing comes out.

## Putting constraints on a type variable

Is this a well-typed function?

```
def triple(string: Union[str, bytes]) -> Union[str, bytes]:
    return string * 3
```

Not really: if you pass in a string, you always get a string, same with bytes. This will cause you some pain, because you know when you get a str and when you get a bytes back.

```
from typing import Union


def triple(string: Union[str, bytes]) -> Union[str, bytes]:
    return string * 3


scream = triple("A")
# Operator "+" not supported for types "str | bytes" and "Literal['!']"
#   Operator "+" not supported for types "bytes" and "Literal['!']"Pylance
scream_with_exlamation = triple("A") + "!"
```

"If you pass in str, you get str. If you pass in bytes, you get bytes" -- sounds like a job for a type variable.

```
from typing import TypeVar

AnyString = TypeVar("AnyString")


def triple(string: AnyString) -> AnyString:
    # Operator "*" not supported for types "AnyString@triple" and "Literal[3]"Pylance
    return string * 3
```

That's fair enough -- not all types support multiplication. We can put a restriction that our type variable should only accept `str` or `bytes` (and their subclasses, of course).

```
from typing import TypeVar

AnyString = TypeVar("AnyString", str, bytes)


def triple(string: AnyString) -> AnyString:
    return string * 3


unicode_scream = triple("A") + "!"
bytes_scream = triple(b"A") + b"!"

# $ mypy triple-3.py
# Success: no issues found in 1 source file

# $ pyright triple-3.py
# 0 errors, 0 warnings, 0 informations
```

## Using type variables as parameters

You can also use type variables as parameters to generic types, like list or Iterable.

```
from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def remove_falsey_from_list(items: list[T]) -> list[T]:
    return [item for item in items if item]


def remove_falsey(items: Iterable[T]) -> Iterator[T]:
    for item in items:
        if item:
            yield item


# $ mypy remove-falsey.py
# Success: no issues found in 1 source file

# $ pyright remove-falsey.py
# 0 errors, 0 warnings, 0 informations
```
