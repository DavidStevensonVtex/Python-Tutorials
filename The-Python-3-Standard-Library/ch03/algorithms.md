# [Chapter 3 Algorithms](https://pymotw.com/3/algorithm_tools.html)

Python includes several modules for implementing algorithms elegantly and concisely using whatever style is most appropriate for the task. It supports purely procedural, object oriented, and functional styles and all three styles are frequently mixed within different parts of the same program.

[functools](https://pymotw.com/3/functools/index.html#module-functools) includes functions for creating function decorators, enabling aspect oriented programming and code reuse beyond what a traditional object oriented approach supports. It also provides a class decorator for implementing all of the rich comparison APIs using a short-cut, and partial objects for creating references to functions with their arguments included.

The [itertools module](https://pymotw.com/3/itertools/index.html#module-itertools) includes functions for creating and working with iterators and generators used in functional programming. The [operator module](https://pymotw.com/3/operator/index.html#module-operator) eliminates the need for many trivial lambda functions when using a functional programming style by providing function-based interfaces to built-in operations such as arithmetic or item lookup.

And no matter what style is used in a program, [contextlib](https://pymotw.com/3/contextlib/index.html#module-contextlib) makes resource management easier, more reliable, and more concise. Combining context managers and the with statement reduces the number of try:finally blocks and indentation levels needed, while ensuring that files, sockets, database transactions, and other resources are closed and released at the right time.

* [functools — Tools for Manipulating Functions](https://pymotw.com/3/functools/index.html)
* [itertools — Iterator Functions](https://pymotw.com/3/itertools/index.html)
* [operator — Functional Interface to Built-in Operators](https://pymotw.com/3/operator/index.html)
* [contextlib — Context Manager Utilities](https://pymotw.com/3/contextlib/index.html)