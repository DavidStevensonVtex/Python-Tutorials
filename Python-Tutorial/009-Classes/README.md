# Python-Tutorials

My self-training in Python

# [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

## [9. Classes](https://docs.python.org/3/tutorial/classes.html)

Classes provide a means of bundling data and functionality together.

Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name.

Class members (including the data members) are public (except see below Private Variables), and all member functions are _virtual_.

Classes themselves are objects. This provides semantics for importing and renaming.

### 9.1. A Word About Names and Objects

Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object.
Aliases behave like pointers in some respects.

For example, passing an object is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as an argument, the caller will see the change.

### 9.2. Python Scopes and Namespaces

Class definitions play some neat tricks with namespaces, and you need to know how scopes and namespaces work to fully understand what’s going on.

A _namespace_ is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way.

Two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.

Strictly speaking, references to names in modules are attribute references: in the expression modname.funcname, modname is a module object and funcname is an attribute of it.

Attributes may be read-only or writable. Module attributes are writable: you can write modname.the_answer = 42. Writable attributes may also be deleted with the del statement. For example, del modname.the_answer will remove the attribute the_answer from the object named by modname.

The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called \_\_main\_\_, so they have their own global namespace.
(The built-in names actually also live in a module; this is called [builtins](https://docs.python.org/3/library/builtins.html#module-builtins).)

A _scope_ is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

Although scopes are determined statically, they are used dynamically. At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:

-   the innermost scope, which is searched first, contains the local names

-   the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain non-local, but also non-global names

-   the next-to-last scope contains the current module’s global names

-   the outermost scope (searched last) is the namespace containing built-in names

A special quirk of Python is that – if no [global](https://docs.python.org/3/reference/simple_stmts.html#global) or [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement is in effect – assignments to names always go into the innermost scope.

#### 9.2.1. Scopes and Namespaces Example
