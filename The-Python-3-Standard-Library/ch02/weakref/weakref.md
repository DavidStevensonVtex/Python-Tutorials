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

The finalize instance has a writable propertly atexit to control whether the callback is invoked as a program is exiting, if it hasn’t already been called.

```
# weakref_finalize_atexit.py
import sys
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


obj = ExpensiveObject()
f = weakref.finalize(obj, on_finalize, 'extra argument')
f.atexit = bool(int(sys.argv[1]))
```

The default is to invoke the callback. Setting atexit to false disables that behavior.

```
$ python3 weakref_finalize_atexit.py 1
on_finalize(('extra argument',))
(Deleting <__main__.ExpensiveObject object at 0x7f572df45040>)
$ python3 weakref_finalize_atexit.py 0
(Deleting <__main__.ExpensiveObject object at 0x7f65b270f040>)
```

Giving the finalize instance a reference to the object it tracks causes a reference to be retained, so the object is never garbage collected.

```
# weakref_finalize_reference.py
import gc
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


obj = ExpensiveObject()
obj_id = id(obj)

f = weakref.finalize(obj, on_finalize, obj)
f.atexit = False

del obj

for o in gc.get_objects():
    if id(o) == obj_id:
        print('found uncollected object in gc')
```

As this example shows, even though the explicit reference to obj is deleted, the object is retained and visible to the garbage collector through f.

```
$ python3 weakref_finalize_reference.py
found uncollected object in gc
(Deleting <__main__.ExpensiveObject object at 0x7f3dea3f0040>)
```

Using a bound method of a tracked object as the callable can also prevent an object from being finalized properly.

```
# weakref_finalize_reference_method.py
import gc
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))

    def do_finalize(self):
        print('do_finalize')


obj = ExpensiveObject()
obj_id = id(obj)

f = weakref.finalize(obj, obj.do_finalize)
f.atexit = False

del obj

for o in gc.get_objects():
    if id(o) == obj_id:
        print('found uncollected object in gc')
```

Because the callable given to finalize is a bound method of the instance obj, the finalize object holds a reference to obj, which cannot be deleted and garbage collected.

```
$ python3 weakref_finalize_reference_method.py
found uncollected object in gc
(Deleting <__main__.ExpensiveObject object at 0x7f8271b20040>)
```

### 2.8.4 Proxies

It is sometimes more convenient to use a proxy, rather than a weak reference. Proxies can be used as though they were the original object, and do not need to be called before the object is accessible. As a consequence, they can be passed to a library that does not know it is receiving a reference instead of the real object.

```
# weakref_proxy.py
import weakref


class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('(Deleting {})'.format(self))


obj = ExpensiveObject('My Object')
r = weakref.ref(obj)
p = weakref.proxy(obj)

print('via obj:', obj.name)
print('via ref:', r().name)
print('via proxy:', p.name)
del obj
print('via proxy:', p.name)
```

If the proxy is accessed after the referent object is removed, a ReferenceError exception is raised.

```
$ python3 weakref_proxy.py
via obj: My Object
via ref: My Object
via proxy: My Object
(Deleting <__main__.ExpensiveObject object at 0x7f37be820df0>)
Traceback (most recent call last):
  File "weakref_proxy.py", line 22, in <module>
    print('via proxy:', p.name)
ReferenceError: weakly-referenced object no longer exists
```

