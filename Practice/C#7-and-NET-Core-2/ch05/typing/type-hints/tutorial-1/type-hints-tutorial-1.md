# [Get started with type hints in Python](https://dev.to/decorator_factory/type-hints-in-python-tutorial-3pel)

## What's this "type hint" thing?

Type hints help you make your Python code more explicit about the types of the things you're working with. They've been a huge productivity booster for me. If you're familiar with basic Python — control flow, functions, classes — this will bring you up to speed in no time.

## Dynamic typing

Python is dynamically typed. It means that at the time of writing a program, you generally don't know what type a variable (or other expression) will be:

```
def double(x):
    return x + x
```

Here you don't know what type x will take.

Dynamic typing doesn't rid you of types. It just moves the responsibility of matching them onto the programmer.

Keeping track of types yourself isn't always bad. It lets you express flexible relations, perhaps something you can't do in C++ or Java. Dynamic typing has its own patterns, such as [duck typing](https://realpython.com/lessons/duck-typing/).

However, most of your functions have simple contracts. If you keep them implicit or informal (say, in a comment), you can't analyse them with tooling. A compiler that guides and corrects you is a big selling point for languages with rich type systems, like Haskell and Rust.

Last but not least, having a standard way of expressing contracts makes code easier to understand.

## What's a type hint?

Python allows you to document types with type hints. They look like this:

```
def double(x: int) -> int:
    return x + x
```

The x: int part means that the function expects an int object to be passed to the function; and the -> int means that the function will return an int object.

A tool like mypy or pyright can now check that you're not doing something shady, like here:

```
def double(x: int) -> int:
    return x + "FizzBuzz"  # error!
```

The types aren't checked at runtime, though — when you run the Python script, the interpreter **doesn't care about type hints**.

The interpreter doesn't do any optimizations based on annotations. Again, only programmers and type-checking tools give them meaning.

Python embraces what's called "gradual typing". You can typehint only part of your code and leave some parts untyped (as before), for example if they're impossible or very hard to annotate.

## Tooling

### PyCharm

PyCharm already has its own custom type checker.

### Installing Mypy

You can install mypy — one of the tools that does type checking — by following the instructions [here](https://mypy.readthedocs.io/en/stable/getting_started.html);

### Installing Pyright

Pyright (which is the tool I personally prefer) can be installed [here](https://github.com/Microsoft/pyright#installation).

### Using Pylance

If you're using Visual Studio Code, you can [install the Pylance extension](https://github.com/Microsoft/pyright#using-pyright-with-vs-code-python-extension) which uses Pyright for typechecking.

## The very basics

### Where do you put them?

First, you can put them on an individual variable:

`answer: int = 42`

Most of the times it's redundant. Type checkers know that 42 is an int.

Type hints are useful on functions, to explain what the function takes as input and what it returns:

```
from typing import Any

def double(x: int) -> int:
    return x + x

def myprint(*args: Any, end: str = " ") -> None:
    for arg in args:
        print(arg, end=" ")
    print()

myprint("The", "rain", "in", "Spain", "falls", "mainly", "in", "the", "plain")
```

...and on class attributes, to explain the types of objects stored in those attributes.

```
class Point:
    x: int
    y: int
```

### Inference

When you're assigning something to a variable, the type checker (remember — just a tool, separate from Python) will infer the type of the variable.

```
numbers: list[int]

numbers = [1, 2, 3, 4]
```

Inference is not "guessing" as the name may suggest. A more correct synonym would be deduction — figuring the type precisely by following an algorithm.

### Basic Types

All the types you're familiar with — int, str, float, range, list etc. — are valid type hints.

#### None

None is special — you annotate it simply as None.

```
my_salary: None
my_salary = None
```

### The `typing` module

The typing module provides some more sophisticated type hints.

#### Any

Sometimes you don't want to specify a type:

You can't express it in the Python's type hint system;
It would be verbose and confusing, requiring lots of extra code;
You really don't care what the type is — consider the print function.
Any denotes the "wildcard type". It can be treated as any type, and any value can be treated as Any.

```
from typing import Any

def print_twice(something: Any) -> None:
    print(something, something, "!")

print_twice(1.234)
```

(note: you may not have to write the -> None here — Pyright [and mypy if you set the appropriate option] will infer it for you)

Don't overuse Any, though — there are often better ways.

#### Union

Sometimes you accept several types, not just one!

In that case, you can use typing.Union.
