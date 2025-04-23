# [Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

This document is a quick cheat sheet showing how to use type annotations for various common types in Python.

## Variables

Technically many of the type annotations shown below are redundant, since mypy can usually infer the type of a variable from its value. See [Type inference and type annotations](https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html#type-inference-and-annotations) for more details.

```
# This is how you declare the type of a variable
age: int = 1

# You don't need to initialize a variable to annotate it
a: int  # Ok (no value at runtime until assigned)

# Doing so can be useful in conditional branches
child: bool
if age < 18:
    child = True
else:
    child = False
```
