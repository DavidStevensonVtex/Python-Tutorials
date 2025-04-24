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
