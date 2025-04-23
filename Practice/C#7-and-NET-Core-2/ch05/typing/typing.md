# [Python typing](https://docs.python.org/3/library/typing.html) -- Support for type hints

**Note** The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.

This module provides runtime support for type hints.

Consider the function below:

```
def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."
```

While type hints can be simple classes like float or str, they can also be more complex. The typing module provides a vocabulary of more advanced type hints.

New features are frequently added to the typing module. The [typing_extensions package](https://pypi.org/project/typing-extensions/) provides backports of these new features to older versions of Python.

See also
[“Typing cheat sheet”](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
A quick overview of type hints (hosted at the mypy docs)

“Type System Reference” section of [the mypy docs](https://mypy.readthedocs.io/en/stable/index.html)
The Python typing system is standardised via PEPs, so this reference should broadly apply to most Python type checkers. (Some parts may still be specific to mypy.)

“Static Typing with Python”
Type-checker-agnostic documentation written by the community detailing type system features, useful typing related tools and typing best practices.
