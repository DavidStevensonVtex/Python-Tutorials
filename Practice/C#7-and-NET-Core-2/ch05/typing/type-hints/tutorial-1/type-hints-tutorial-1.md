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

```
from typing import Union

def print_thing(thing: Union[str, int]) -> None:
    if isinstance(thing, str):
        print("string", thing)
    else:
        print("number", thing)

print_thing("abc")
print_thing(123)
```

It means that you can do this:

```
from typing import Union


def print_thing(thing: Union[str, int]) -> None:
    if isinstance(thing, str):
        print("string", thing)
    else:
        print("number", thing)


print_thing("abc")
print_thing(123)
```

and the type checker will understand that in the first if clause thing has type str, and in the second clause it has type int.

Here we've seen that some types can be parametrized — you can pass arguments to a type to configure it. It's not special syntax — it's just using subscription, like you do on lists and dictionaries.

#### Optional

Optional[YourType] is just a shorthand for Union[YourType, None]. Union with None is very commonly used to indicate a potentially missing result. For example, when you call .get(some_key) on a dictionary, you get either an item or None.

Let's typehint this function that implements translation from Russian to English, but caches the results. It will encode an unknown word as None.

```
from typing import Optional

_cache: dict[str, str] = {"питон": "python"}

def fetch_translation(word: str, target_lang: str, default_lang: str) -> Optional[str]:
    return None

def translate(word: str) -> Optional[str]:
    from_cache: Optional[str] = _cache.get(word)
    if from_cache is not None:
        return from_cache
    fetched: Optional[str] = fetch_translation(word, "ru", "en")
    if fetched is None:
        return None
    _cache[word] = fetched
    return fetched

print(translate("питон"))
```

As you can see, it's not always straight-forward; but hopefully it matches your issues of what kind of value each variable holds at what point.

#### List, Dict, Set, ...

What if you want to add two lists of numbers elementwise? You might do this:

```
def zip_add(list1: list, list2: list) -> list:
    if len(list1) != len(list2):
        raise ValueError("Expected lists of the same length")

    return [a + b for a, b in zip(list1, list2)]


zip_add([1, 2, 3], ["abc", "def", "ghi"])
```

This is better than nothing — the type checker will complain if you'll try to zip_add an integer and a string. But it will happily allow you to zip_add a list of integers and a list of strings. There must be a better way!

#### List

This is where typing.List comes in — it allows you to say what elements the list must contain.

```
from typing import List


def zip_add(list1: List[int], list2: List[int]) -> List[int]:
    if len(list1) != len(list2):
        raise ValueError("Expected lists of the same length")

    return [a + b for a, b in zip(list1, list2)]


print(zip_add([1, 2, 3], [4, 5, 6]))


print(zip_add([1, 2, 3], [4, 5, "ghi"]))

# $ pyright list-2.py
# d:\drs\Python\GitHub\Python-Tutorials\Practice\C#7-and-NET-Core-2\ch05\typing\type-hints\tutorial-1\list-2.py
#   d:\drs\Python\GitHub\Python-Tutorials\Practice\C#7-and-NET-Core-2\ch05\typing\type-hints\tutorial-1\list-2.py:14:33 - error: Argument of type "list[int | str]" cannot be assigned to parameter "list2" of type "List[int]" in function "zip_add"
#     "Literal['ghi']" is not assignable to "int" (reportArgumentType)
# 1 error, 0 warnings, 0 informations

# $ mypy list-2.py
# list-2.py:14: error: List item 2 has incompatible type "str"; expected "int"  [list-item]
# Found 1 error in 1 file (checked 1 source file)
```

List[int] stands for a list object, in which **all** elements are int objects. For example: [1, 2, 3], [1 + 2] and [].

Now zip_add([1, 2, 3], [4, 5, 6]) will satisfy the type checker, but zip_add(["foo", "bar"], [1, 0]) will not.

#### Dict

dict has a similar typing counterpart — Dict. It's different in that it's parametrized by two types, not one: the key type and the value type:

```
from typing import Dict


def print_salaries(employees: Dict[str, int]) -> None:
    for name, salary in employees.items():
        print(f"{name} has salary of ${salary}")


print_salaries({"alice": 420, "bob": 420})

# $ python dict-1.py
# alice has salary of $420
# bob has salary of $420

# $ pyright dict-1.py
# 0 errors, 0 warnings, 0 informations

# $ mypy dict-1.py
# Success: no issues found in 1 source file
```

The type hint says that print_salaries accepts a dictionary where all keys are strings, and all values are integers. An example would be {"alice": 420, "bob": 420}.

#### Other data structures

A similar pattern applies to Set, Frozenset, Deque, OrderedDict, DefaultDict, Counter, ChainMap:

```
from typing import Set


def extract_bits(numbers: Set[int]) -> Set[int]:
    return numbers & {0, 1}


print(extract_bits({0, 1, 2, 3, 4, 5}))

# $ python set-1.py
# {0, 1}

# $ pyright set-1.py
# 0 errors, 0 warnings, 0 informations
# $ mypy set-1.py
# Success: no issues found in 1 source file
```

### Changes in Python 3.9

Since Python 3.9, ordinary types like list, dict, tuple, type, set, frozenset, ... allow being subscripted. So our first example would look like this:

```
def zip_add(list1: list[int], list2: list[int]) -> list[int]:
    if len(list1) != len(list2):
        raise ValueError("Expected lists of the same length")

    return [a + b for a, b in zip(list1, list2)]
```

No import from typing required — just index into the list class!

### Tuples

Tuples are a bit more complicated, because they're used for different purposes:

-   a 'heterogenous record' of fixed size (like ('alice', 420) or (1, 2) [meaning a point on a 2D grid])
-   an immutable list of values having the same type (like (1, 2, 3, 4, 5))

Type hints for tuples support both cases.

#### Tuples as records

Let's start with the first usage. We'll need to import typing.Tuple (or, if you're on 3.9 or above, just use tuple), and simply pass the expected types in order (there can be as many as you want.

```
from typing import Tuple

def print_salary_entry(entry: Tuple[str, int]) -> None:
    name, salary = entry
    print(f"Salary of {name}: {salary}")

print_salary_entry(("Joe Q. Employee", 123456))

# $ python tuple-1.py
# Salary of Joe Q. Employee: 123456
# $ pyright tuple-1.py
# 0 errors, 0 warnings, 0 informations
# $ mypy tuple-1.py
# Success: no issues found in 1 source file
```

This type hint means that print_salary_entry accepts a tuple of length 2 where the first element is a string and the second element is an integer.

You can nest types as deeply as you want. For example, you might have volunteers, not just employees:

```
from typing import Tuple, Optional


def print_salary_entry(entry: Tuple[str, Optional[int]]) -> None:
    name, salary = entry
    if salary is None:
        print(f"{name} is a volunteer")
    else:
        print(f"Salary of {name}: {salary}")


print_salary_entry(("Joe Q. Employee", 123456))
print_salary_entry(("Joe Q. Employee", None))

# $ python tuple-2.py
# Salary of Joe Q. Employee: 123456
# Joe Q. Employee is a volunteer
# $ pyright tuple-2.py
# 0 errors, 0 warnings, 0 informations
# $ mypy tuple-2.py
# Success: no issues found in 1 source file
```

Here the type hint means that the print_salary_entry accepts a tuple of length 2 where the first element is a string and the second element is an integer or None.

#### Tuples as immutable lists

Sometimes a tuple is used as an immutable list. For example, you might want to store a sequence of objects and make sure it doesn't change. Another use is in arbitrary arguments (usually spelled as \*args). In this case, the tuple value is annotated as Tuple[YourType, ...]. ... is an ellipsis — a very niche object that found its use here. Example:

### Python 3.9

As I said before, in Python 3.9 and higher you can simply use tuple instead of typing.Tuple.
