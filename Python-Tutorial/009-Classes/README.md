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
