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

#### 9.3.4. Method Objects

Usually, a method is called right after it is bound:

`x.f()`

It is not necessary to call a method right away: x.f is a method object, and can be stored away and called at a later time. For example:

```
xf = x.f
while True:
    print(xf())
```

The special thing about methods is that the instance object is passed as the first argument of the function.
x.f() is exactly equivalent to MyClass.f(x). In general, calling a method with a list of _n_ arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s instance object before the first argument.

#### 9.3.5. Class and Instance Variables

Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:

### 9.4. Random Remarks

If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance:

```
class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print("w1", w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print("w2", w2.purpose, w2.region)
print("w1", w1.purpose, w1.region)

# $ python Warehouse.py
# w1 storage west
# w2 storage east
# w1 storage west
```

Data attributes may be referenced by methods as well as by ordinary users (“clients”) of an object. In other words, classes are not usable to implement pure abstract data types. In fact, nothing in Python makes it possible to enforce data hiding — it is all based upon convention. (On the other hand, the Python implementation, written in C, can completely hide implementation details and control access to an object if necessary; this can be used by extensions to Python written in C.)

Often, the first argument of a method is called self. This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a class browser program might be written that relies upon such a convention.

Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok. For example:

```
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

Now f, g and h are all attributes of class C that refer to function objects, and consequently they are all methods of instances of C — h being exactly equivalent to g. Note that this practice usually only serves to confuse the reader of a program.

Methods may call other methods by using method attributes of the self argument:

```
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

Methods may reference global names in the same way as ordinary functions. The global scope associated with a method is the module containing its definition. (A class is never used as a global scope.) While one rarely encounters a good reason for using global data in a method, there are many legitimate uses of the global scope: for one thing, functions and modules imported into the global scope can be used by methods, as well as functions and classes defined in it. Usually, the class containing the method is itself defined in this global scope, and in the next section we’ll find some good reasons why a method would want to reference its own class.

Each value is an object, and therefore has a class (also called its type). It is stored as object.\_\_class\_\_.

### 9.5. Inheritance

Of course, a language feature would not be worthy of the name “class” without supporting inheritance. The syntax for a derived class definition looks like this:

```
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

The name BaseClassName must be defined in a namespace accessible from the scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

`class DerivedClassName(modname.BaseClassName):`

Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

There’s nothing special about instantiation of derived classes: DerivedClassName() creates a new instance of the class. Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.

Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it. (For C++ programmers: all methods in Python are effectively virtual.)

An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name. There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as BaseClassName in the global scope.)

Python has two built-in functions that work with inheritance:

-   Use [isinstance()](https://docs.python.org/3/library/functions.html#isinstance) to check an instance’s type: isinstance(obj, int) will be True only if obj.\_\_class\_\_ is int or some class derived from int.

-   Use [issubclass()](https://docs.python.org/3/library/functions.html#issubclass) to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

#### 9.5.1. Multiple Inheritance

Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:

```
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.

In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to super(). This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful than the super call found in single-inheritance languages.

Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships (where at least one of the parent classes can be accessed through multiple paths from the bottommost class). For example, all classes inherit from object, so any case of multiple inheritance provides more than one path to reach object. To keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way that preserves the left-to-right ordering specified in each class, that calls each parent only once, and that is monotonic (meaning that a class can be subclassed without affecting the precedence order of its parents). Taken together, these properties make it possible to design reliable and extensible classes with multiple inheritance. For more detail, see [The Python 2.3 Method Resolution Order](https://docs.python.org/3/howto/mro.html#python-2-3-mro).

### 9.6. Private Variables

“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. \_spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called _name mangling_. Any identifier of the form \_\_spam (at least two leading underscores, at most one trailing underscore) is textually replaced with \_classname\_\_spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

See also The [private name mangling specifications](https://docs.python.org/3/reference/expressions.html#private-name-mangling) for details and special cases.

Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:

```
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

The above example would work even if MappingSubclass were to introduce a \_\_update identifier since it is replaced with \_Mapping\_\_update in the Mapping class and \_MappingSubclass\_\_update in the MappingSubclass class respectively.

Note that the mangling rules are designed mostly to avoid accidents; it still is possible to access or modify a variable that is considered private. This can even be useful in special circumstances, such as in the debugger.

Notice that code passed to exec() or eval() does not consider the classname of the invoking class to be the current class; this is similar to the effect of the global statement, the effect of which is likewise restricted to code that is byte-compiled together. The same restriction applies to getattr(), setattr() and delattr(), as well as when referencing \_\_dict\_\_ directly.
