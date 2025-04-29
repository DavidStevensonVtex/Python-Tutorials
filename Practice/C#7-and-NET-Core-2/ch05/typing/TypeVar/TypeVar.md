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
