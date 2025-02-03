# Chapter 2: [Data Structures](https://pymotw.com/3/data_structures.html)

## [2.8 weakref: Impermanent References to Objects](https://pymotw.com/3/weakref/index.html)


Purpose:	Refer to an “expensive” object, but allow its memory to be reclaimed by the garbage collector if there are no other non-weak references.

The weakref module supports weak references to objects. A normal reference increments the reference count on the object and prevents it from being garbage collected. This outcome is not always desirable, especially when a circular reference might be present or when a cache of objects should be deleted when memory is needed. A weak reference is a handle to an object that does not keep it from being cleaned up automatically.

### 2.8.1 References

Weak references to objects are managed through the ref class. To retrieve the original object, call the reference object.

```
# weakref_ref.py
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())
```

In this case, since obj is deleted before the second call to the reference, the ref returns None.

```
$ python3 weakref_ref.py
obj: <__main__.ExpensiveObject object at 0x7f87bcc43040>
ref: <weakref at 0x7f87bcb0f770; to 'ExpensiveObject' at 0x7f87bcc43040>
r(): <__main__.ExpensiveObject object at 0x7f87bcc43040>
deleting obj
(Deleting <__main__.ExpensiveObject object at 0x7f87bcc43040>)
r(): None
```

### 2.8.2 Reference Callbacks

The ref constructor accepts an optional callback function that is invoked when the referenced object is deleted.

```
# weakref_ref_callback.py
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())
```

The callback receives the reference object as an argument after the reference is “dead” and no longer refers to the original object. One use for this feature is to remove the weak reference object from a cache.

```
$ python3 weakref_ref_callback.py
obj: <__main__.ExpensiveObject object at 0x7f97f7be8040>
ref: <weakref at 0x7f97f7ab4860; to 'ExpensiveObject' at 0x7f97f7be8040>
r(): <__main__.ExpensiveObject object at 0x7f97f7be8040>
deleting obj
(Deleting <__main__.ExpensiveObject object at 0x7f97f7be8040>)
callback(<weakref at 0x7f97f7ab4860; dead>)
r(): None
```

### 2.8.3 Finalizing Objects

For more robust management of resources when weak references are cleaned up, use finalize to associate callbacks with objects. A finalize instance is retained until the attached object is deleted, even if the application does not retain a reference to the finalizer.

```
# weakref_finalize.py
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


obj = ExpensiveObject()
weakref.finalize(obj, on_finalize, 'extra argument')

del obj
```

The arguments to finalize are the object to track, a callable to invoke when the object is garbage collected, and any positional or named arguments to pass to the callable.

```
$ python3 weakref_finalize.py
(Deleting <__main__.ExpensiveObject object at 0x7f79f699b040>)
on_finalize(('extra argument',))
```