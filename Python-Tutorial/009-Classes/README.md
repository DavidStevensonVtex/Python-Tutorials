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

### 9.3. A First Look at Classes

#### 9.3.1. Class Definition Syntax

The simplest form of class definition looks like this:

```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

Class definitions, like function definitions (def statements) must be executed before they have any effect.

In practice, the statements inside a class definition will usually be function definitions, but other statements are allowed. The function definitions inside a class normally have a peculiar form of argument list.

When a class definition is entered, a new namespace is created, and used as the local scope.

When a class definition is left normally (via the end), a _class object_ is created.
This is basically a wrapper around the contents of the namespace created by the class definition.

#### 9.3.2. Class Objects

Class objects support two kinds of operations: attribute references and instantiation.

_Attribute references_ use the standard syntax used for all attribute references in Python: obj.name.

```
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respectively.
Class attributes can also be assigned to, so you can change the value of MyClass.i by assignment.
\_\_doc\_\_ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".

Class _instantiation_ uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. For example (assuming the above class):

`x = MyClass()`

Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named \_\_init\_\_(), like this:

```
def __init__(self):
    self.data = []
```

When a class defines an \_\_init\_\_() method, class instantiation automatically invokes \_\_init\_\_() for the newly created class instance. So in this example, a new, initialized instance can be obtained by:

`x = MyClass()`

Of course, the \_\_init\_\_() method may have arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to \_\_init\_\_(). For example,

```
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

#### 9.3.3. Instance Objects

Now what can we do with instance objects? The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.

_data attributes_ correspond to “instance variables”. Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to.

For example, if x is the instance of MyClass created above, the following piece of code will print the value 16, without leaving a trace:

```
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

The other kind of instance attribute reference is a _method_. A method is a function that “belongs to” an object.

By definition, all attributes of a class that are function objects define corresponding methods of its instances.
x.f is not the same thing as MyClass.f — it is a _method object_, not a function object.
