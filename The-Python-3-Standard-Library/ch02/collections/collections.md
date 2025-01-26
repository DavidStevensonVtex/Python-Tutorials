# Chapter 2: Data Structures

## 2.2 collections — Container Data Types

The collections module includes container data types beyond the built-in types list, dict, and tuple.

* [ChainMap — Search Multiple Dictionaries](https://pymotw.com/3/collections/chainmap.html)
* [Counter — Count Hashable Objects](https://pymotw.com/3/collections/counter.html)
* [defaultdict — Missing Keys Return a Default Value](https://pymotw.com/3/collections/defaultdict.html)
* [deque — Double-Ended Queue](https://pymotw.com/3/collections/deque.html)
* [namedtuple — Tuple Subclass with Named Fields](https://pymotw.com/3/collections/namedtuple.html)
* [OrderedDict — Remember the Order Keys are Added to a Dictionary](https://pymotw.com/3/collections/ordereddict.html)
* [collections.abc — Abstract Base Classes for Containers](https://pymotw.com/3/collections/abc.html)

## See also

* [Standard library documentation for collections](https://docs.python.org/3/library/collections.html)
* [Python 2 to 3 porting notes for collections](https://pymotw.com/3/porting_notes.html#porting-collections)
* [PEP 342](https://peps.python.org/pep-0342/) – Coroutines via Enhanced Generators
* [PEP 492](https://peps.python.org/pep-0492/) – Coroutines with async and await syntax
* 
### 2.2.1 ChainMap — Search Multiple Dictionaries

The ChainMap class manages a sequence of dictionaries, and searches through them in the order they are given to find values associated with keys. A ChainMap makes a good “context” container, since it can be treated as a stack for which changes happen as the stack grows, with these changes being discarded again as the stack shrinks.

#### 2.2.1.1 Accessing Values

The ChainMap supports the same API as a regular dictionary for accessing existing values.

```
# collections_chainmap_read.py
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print()

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print()

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))
print()

print('"d" in m: {}'.format(('d' in m)))
```

The child mappings are searched in the order they are passed to the constructor, so the value reported for the key 'c' comes from the a dictionary.

```
$ python3 collections_chainmap_read.py 
Individual Values
a = A
b = B
c = C

Keys = ['b', 'c', 'a']
Values = ['B', 'C', 'A']

Items:
b = B
c = C
a = A

"d" in m: False
```

#### 2.2.1.2 Reordering

The ChainMap stores the list of mappings over which it searches in a list in its maps attribute. This list is mutable, so it is possible to add new mappings directly or to change the order of the elements to control lookup and update behavior.

```
# collections_chainmap_reorder.py
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print(m.maps)
print('c = {}\n'.format(m['c']))

# reverse the list
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}'.format(m['c']))
```

When the list of mappings is reversed, the value associated with 'c' changes.

```
$ python3 collections_chainmap_reorder.py
[{'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}]
c = C

[{'b': 'B', 'c': 'D'}, {'a': 'A', 'c': 'C'}]
c = D
```