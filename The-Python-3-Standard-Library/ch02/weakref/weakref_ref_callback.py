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