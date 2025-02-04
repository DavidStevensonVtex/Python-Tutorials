# Chapter 2: [Data Structures](https://pymotw.com/3/data_structures.html)

## [2.9 copy — Duplicate Objects](https://pymotw.com/3/copy/index.html)

Purpose:	Provides functions for duplicating objects using shallow or deep copy semantics.

The copy module includes two functions, copy() and deepcopy(), for duplicating existing objects.

### 2.9.1 Shallow Copies

The shallow copy created by copy() is a new container populated with references to the contents of the original object. When making a shallow copy of a list object, a new list is constructed and the elements of the original object are appended to it.

```
# copy_shallow.py
import copy
import functools


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


a = MyClass('a')
my_list = [a]
dup = copy.copy(my_list)

print('             my_list:', my_list)
print('                 dup:', dup)
print('      dup is my_list:', (dup is my_list))
print('      dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))
```

For a shallow copy, the MyClass instance is not duplicated, so the reference in the dup list is to the same object that is in my_list.

```
$ python3 copy_shallow.py
             my_list: [<__main__.MyClass object at 0x7f35f71d3040>]
                 dup: [<__main__.MyClass object at 0x7f35f71d3040>]
      dup is my_list: False
      dup == my_list: True
dup[0] is my_list[0]: True
dup[0] == my_list[0]: True
```