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