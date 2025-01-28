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

#### 2.2.1.3 Updating Values

A ChainMap does not cache the values in the child mappings. Thus, if their contents are modified, the results are reflected when the ChainMap is accessed.

```
# collections_chainmap_update_behind.py
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After : {}'.format(m['c']))
```

Changing the values associated with existing keys and adding new elements works the same way.

```
$ python3 collections_chainmap_update_behind.py
Before: C
After : E
```

It is also possible to set values through the ChainMap directly, although only the first mapping in the chain is actually modified.

```
# collections_chainmap_update_directly.py
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before:', m)
m['c'] = 'E'
print('After :', m)
print('a:', a)
```

When the new value is stored using m, the a mapping is updated.

```
$ python3 collections_chainmap_update_directly.py
Before: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
After : ChainMap({'a': 'A', 'c': 'E'}, {'b': 'B', 'c': 'D'})
a: {'a': 'A', 'c': 'E'}
```

ChainMap provides a convenience method for creating a new instance with one extra mapping at the front of the maps list to make it easy to avoid modifying the existing underlying data structures.

```
# collections_chainmap_new_child.py
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child()

print('m1 before:', m1)
print('m2 before:', m2)

m2['c'] = 'E'

print('m1 after:', m1)
print('m2 after:', m2)
```

This stacking behavior is what makes it convenient to use ChainMap instances as template or application contexts. Specifically, it is easy to add or update values in one iteration, then discard the changes for the next iteration.

```
$ python3 collections_chainmap_new_child.py
m1 before: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
m2 before: ChainMap({}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
m1 after: ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
m2 after: ChainMap({'c': 'E'}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
```

For situations where the new context is known or built in advance, it is also possible to pass a mapping to new_child().

```
# collections_chainmap_new_child_explicit.py
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child(c)

print('m1["c"] = {}'.format(m1['c']))
print('m2["c"] = {}'.format(m2['c']))
```

This is the equivalent of

```
m2 = collections.ChainMap(c, *m1.maps)
```

and produces

```
$ python3 collections_chainmap_new_child_explicit.py
m1["c"] = C
m2["c"] = E
```


### 2.2.2 Counter — Count Hashable Objects

A Counter is a container that keeps track of how many times equivalent values are added. It can be used to implement the same algorithms for which other languages commonly use bag or multiset data structures.

#### 2.2.2.1 Initializing

Counter supports three forms of initialization. Its constructor can be called with a sequence of items, a dictionary containing keys and counts, or using keyword arguments that map string names to counts.

```
# collections_counter_init.py
import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))
```

The results of all three forms of initialization are the same.

```
$ python3 collections_counter_init.py
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
```

An empty Counter can be constructed with no arguments and populated via the update() method.

```
# collections_counter_update.py
import collections

c = collections.Counter()
print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': 5})
print('Dict    :', c)
```

The count values are increased based on the new data, rather than replaced. In the preceding example, the count for a goes from 3 to 4.

```
$ python3 collections_counter_update.py
Initial : Counter()
Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})
```

#### 2.2.2.2 Accessing Counts

Once a Counter is populated, its values can be retrieved using the dictionary API.

```
# collections_counter_get_values.py
import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))
```

Counter does not raise KeyError for unknown items. If a value has not been seen in the input (as with e in this example), its count is 0.

```
$ python3 collections_counter_get_values.py
a : 3
b : 2
c : 1
d : 1
e : 0
```

The elements() method returns an iterator that produces all of the items known to the Counter.

```
# collections_counter_elements.py
import collections

c = collections.Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))
```

The order of elements is not guaranteed, and items with counts less than or equal to zero are not included.

```
$ python3 collections_counter_elements.py
Counter({'e': 3, 'x': 1, 't': 1, 'r': 1, 'm': 1, 'l': 1, 'y': 1, 'z': 0})
['e', 'e', 'e', 'x', 't', 'r', 'm', 'l', 'y']
```

Use most_common() to produce a sequence of the n most frequently encountered input values and their respective counts.

```
# collections_counter_most_common.py
import collections

c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print('Most common:')
for letter, count in c.most_common(3):
    print('{}: {:>7}'.format(letter, count))
```

This example counts the letters appearing in all of the words in the system dictionary to produce a frequency distribution, then prints the three most common letters. Leaving out the argument to most_common() produces a list of all the items, in order of frequency.

```
Most common:
s:   94661
e:   91292
i:   68740
```

#### 2.2.2.3 Arithmetic

Counter instances support arithmetic and set operations for aggregating results. This example shows the standard operators for creating new Counter instances, but the in-place operators +=, -=, &=, and |= are also supported.

```
# collections_counter_arithmetic.py
import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('C1:', c1)
print('C2:', c2)

print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction:')
print(c1 - c2)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)
```

Each time a new Counter is produced through an operation, any items with zero or negative counts are discarded. The count for a is the same in c1 and c2, so subtraction leaves it at zero.

```
$ python3 collections_counter_arithmetic.py
C1: Counter({'b': 3, 'a': 2, 'c': 1})
C2: Counter({'a': 2, 'l': 1, 'p': 1, 'h': 1, 'b': 1, 'e': 1, 't': 1})

Combined counts:
Counter({'a': 4, 'b': 4, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})

Subtraction:
Counter({'b': 2, 'c': 1})

Intersection (taking positive minimums):
Counter({'a': 2, 'b': 1})

Union (taking maximums):
Counter({'b': 3, 'a': 2, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})
```

### 2.2.3 defaultdict — Missing Keys Return a Default Value

The standard dictionary includes the method setdefault() for retrieving a value and establishing a default if the value does not exist. By contrast, defaultdict lets the caller specify the default up front when the container is initialized.

```
# collections_defaultdict.py
import collections


def default_factory():
    return 'default value'


d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])
```

This method works well as long as it is appropriate for all keys to have the same default. It can be especially useful if the default is a type used for aggregating or accumulating values, such as a list, set, or even int. The standard library documentation includes several examples in which defaultdict is used in this way.

```
$ python3 collections_defaultdict.py
d: defaultdict(<function default_factory at 0x7f722ceb4c10>, {'foo': 'bar'})
foo => bar
bar => default value
```

### 2.2.4 deque — Double-Ended Queue

A double-ended queue, or deque, supports adding and removing elements from either end of the queue. The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.

```
# collections_deque.py
import collections

d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])

d.remove('c')
print('remove(c):', d)
```

Since deques are a type of sequence container, they support some of the same operations as list, such as examining the contents with `__getitem__()`, determining length, and removing elements from the middle of the queue by matching identity.

```
$ python3 collections_deque.py
Deque: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
Length: 7
Left end: a
Right end: g
remove(c): deque(['a', 'b', 'd', 'e', 'f', 'g'])
```

#### 2.2.4.1 Populating

A deque can be populated from either end, termed “left” and “right” in the Python implementation.

```
# collections_deque_populating.py
import collections

# Add to the right
d1 = collections.deque()
d1.extend('abcdefg')
print('extend    :', d1)
d1.append('h')
print('append    :', d1)

# Add to the left
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)
```

The extendleft() function iterates over its input and performs the equivalent of an appendleft() for each item. The end result is that the deque contains the input sequence in reverse order.

```
$ python3 collections_deque_populating.py 
extend    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
append    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
extendleft: deque([5, 4, 3, 2, 1, 0])
appendleft: deque([6, 5, 4, 3, 2, 1, 0])
```

#### 2.2.4.2 Consuming

Similarly, the elements of the deque can be consumed from both ends or either end, depending on the algorithm being applied.

```
# collections_deque_consuming.py
import collections

print('From the right:')
d = collections.deque('abcdefg')
while True:
    try:
        print(d.pop(), end='')
    except IndexError:
        break
print()

print('\nFrom the left:')
d = collections.deque(range(6))
while True:
    try:
        print(d.popleft(), end='')
    except IndexError:
        break
print()
```

Use pop() to remove an item from the “right” end of the deque and popleft() to take an item from the “left” end.

```
$ python3 collections_deque_consuming.py 
From the right:
gfedcba

From the left:
012345
```

Since deques are thread-safe, the contents can even be consumed from both ends at the same time from separate threads.

```
# collections_deque_both_ends.py
import collections
import threading
import time

candle = collections.deque(range(5))


def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return


left = threading.Thread(target=burn,
                        args=('Left', candle.popleft))
right = threading.Thread(target=burn,
                         args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()
```

The threads in this example alternate between each end, removing items until the deque is empty.

```
$ python3 collections_deque_both_ends.py 
    Left: 0
   Right: 4
    Left: 1
   Right: 3
    Left: 2
   Right done
    Left done
```

#### 2.2.4.3 Rotating

Another useful aspect of the deque is the ability to rotate it in either direction, so as to skip over some items.

```
# collections_deque_rotate.py
import collections

d = collections.deque(range(10))
print('Normal        :', d)

d = collections.deque(range(10))
d.rotate(2)
print('Right rotation:', d)

d = collections.deque(range(10))
d.rotate(-2)
print('Left rotation :', d)
```

Rotating the deque to the right (using a positive rotation) takes items from the right end and moves them to the left end. Rotating to the left (with a negative value) takes items from the left end and moves them to the right end. It may help to visualize the items in the deque as being engraved along the edge of a dial.

```
$ python3 collections_deque_rotate.py
Normal        : deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
Right rotation: deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
Left rotation : deque([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
```

#### 2.2.4.4 Constraining the Queue Size

A deque instance can be configured with a maximum length so that it never grows beyond that size. When the queue reaches the specified length, existing items are discarded as new items are added. This behavior is useful for finding the last n items in a stream of undetermined length.

```
# collections_deque_maxlen.py
import collections
import random

# Set the random seed so we see the same output each time
# the script is run.
random.seed(1)

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)

for i in range(5):
    n = random.randint(0, 100)
    print('n =', n)
    d1.append(n)
    d2.appendleft(n)
    print('D1:', d1)
    print('D2:', d2)
```

The deque length is maintained regardless of which end the items are added to.

```
$ python3 collections_deque_maxlen.py
n = 17
D1: deque([17], maxlen=3)
D2: deque([17], maxlen=3)
n = 72
D1: deque([17, 72], maxlen=3)
D2: deque([72, 17], maxlen=3)
n = 97
D1: deque([17, 72, 97], maxlen=3)
D2: deque([97, 72, 17], maxlen=3)
n = 8
D1: deque([72, 97, 8], maxlen=3)
D2: deque([8, 97, 72], maxlen=3)
n = 32
D1: deque([97, 8, 32], maxlen=3)
D2: deque([32, 8, 97], maxlen=3)
```

#### See also

* [Wikipedia: Deque](https://en.wikipedia.org/wiki/Double-ended_queue) – A discussion of the deque data structure.
* [Deque Recipes](https://docs.python.org/3/library/collections.html#deque-recipes) – Examples of using deques in algorithms from the standard library documentation.

### 2.2.5 namedtuple — Tuple Subclass with Named Fields

The standard tuple uses numerical indexes to access its members.

```
# collections_tuple.py
bob = ('Bob', 30, 'male')
print('Representation:', bob)

jane = ('Jane', 29, 'female')
print('\nField by index:', jane[0])

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is a {} year old {}'.format(*p))
```

This makes tuples convenient containers for simple uses.

```
$ python3 collections_tuple.py
Representation: ('Bob', 30, 'male')

Field by index: Jane

Fields by index:
Bob is a 30 year old male
Jane is a 29 year old female
```

In contrast, remembering which index should be used for each value can lead to errors, especially if the tuple has a lot of fields and is constructed far from where it is used. A namedtuple assigns names, as well as the numerical index, to each member.

#### 2.2.5.1 Defining

namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance dictionaries. Each kind of namedtuple is represented by its own class, which is created by using the namedtuple() factory function. The arguments are the name of the new class and a string containing the names of the elements.

```
# collections_namedtuple_person.py
import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nRepresentation:', bob)

jane = Person(name='Jane', age=29)
print('\nField by name:', jane.name)

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is {} years old'.format(*p))
```

As the example illustrates, it is possible to access the fields of the namedtuple by name using dotted notation (obj.attr) as well as by using the positional indexes of standard tuples.

```
$ python3 collections_namedtuple_person.py

Representation: Person(name='Bob', age=30)

Field by name: Jane

Fields by index:
Bob is 30 years old
Jane is 29 years old
```

Just like a regular tuple, a namedtuple is immutable. This restriction allows tuple instances to have a consistent hash value, which makes it possible to use them as keys in dictionaries and to be included in sets.

```
# collections_namedtuple_immutable.py
import collections

Person = collections.namedtuple('Person', 'name age')

pat = Person(name='Pat', age=12)
print('\nRepresentation:', pat)

pat.age = 21
```

Trying to change a value through its named attribute results in an AttributeError.

```
$ python3 collections_namedtuple_immutable.py

Representation: Person(name='Pat', age=12)
Traceback (most recent call last):
  File "collections_namedtuple_immutable.py", line 9, in <module>
    pat.age = 21
AttributeError: can't set attribute
```

#### 2.2.5.2 Invalid Field Names

Field names are invalid if they are repeated or conflict with Python keywords.

```
# collections_namedtuple_bad_fields.py
import collections

try:
    collections.namedtuple('Person', 'name class age')
except ValueError as err:
    print(err)

try:
    collections.namedtuple('Person', 'name age age')
except ValueError as err:
    print(err)
```

As the field names are parsed, invalid values cause ValueError exceptions.

```
$ python3 collections_namedtuple_bad_fields.py
Type names and field names cannot be a keyword: 'class'
Encountered duplicate field name: 'age'
```

In situations where a namedtuple is created based on values outside the control of the program (such as to represent the rows returned by a database query, where the schema is not known in advance), the rename option should be set to True so the invalid fields are renamed.

```
# collections_namedtuple_rename.py
import collections

with_class = collections.namedtuple(
    'Person', 'name class age',
    rename=True)
print(with_class._fields)

two_ages = collections.namedtuple(
    'Person', 'name age age',
    rename=True)
print(two_ages._fields)
```

The new names for renamed fields depend on their index in the tuple, so the field with name class becomes _1 and the duplicate age field is changed to _2.

```
$ python3 collections_namedtuple_rename.py
('name', '_1', 'age')
('name', 'age', '_2')
```

#### 2.2.5.3 Special Attributes

namedtuple provides several useful attributes and methods for working with subclasses and instances. All of these built-in properties have names prefixed with an underscore (\_), which by convention in most Python programs indicates a private attribute. For namedtuple, however, the prefix is intended to protect the name from collision with user-provided attribute names.

The names of the fields passed to namedtuple to define the new class are saved in the `_fields` attribute.

```
# collections_namedtuple_fields.py
import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('Fields:', bob._fields)
```

Although the argument is a single space-separated string, the stored value is the sequence of individual names.

```
$ python3 collections_namedtuple_fields.py
Representation: Person(name='Bob', age=30)
Fields: ('name', 'age')
```

namedtuple instances can be converted to OrderedDict instances using _asdict().

```
# collections_namedtuple_asdict.py
import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('As Dictionary:', bob._asdict())
```

The keys of the OrderedDict are in the same order as the fields for the namedtuple.

```
$ python3 collections_namedtuple_asdict.py
Representation: Person(name='Bob', age=30)
As Dictionary: {'name': 'Bob', 'age': 30}
```

The `_replace()` method builds a new instance, replacing the values of some fields in the process.

```
# collections_namedtuple_replace.py
import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nBefore:', bob)
bob2 = bob._replace(name='Robert')
print('After:', bob2)
print('Same?:', bob is bob2)
```

Although the name implies it is modifying the existing object, because namedtuple instances are immutable the method actually returns a new object.

```
$ python3 collections_namedtuple_replace.py

Before: Person(name='Bob', age=30)
After: Person(name='Robert', age=30)
Same?: False
```

### 2.2.6 OrderedDict — Remember the Order Keys are Added to a Dictionary

An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.

```
# collections_ordereddict_iter.py
import collections

print('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k, v in d.items():
    print(k, v)

print('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k, v in d.items():
    print(k, v)
```

Before Python 3.6 a regular dict did not track the insertion order, and iterating over it produced the values in order based on how the keys are stored in the hash table, which is in turn influenced by a random value to reduce collisions. In an OrderedDict, by contrast, the order in which the items are inserted is remembered and used when creating an iterator.

```
$ python3.5 collections_ordereddict_iter.py

Regular dictionary:
c C
b B
a A

OrderedDict:
a A
b B
c C
```

```
$ python3 --version
Python 3.8.10
$ python3 collections_ordereddict_iter.py
Regular dictionary:
a A
b B
c C

OrderedDict:
a A
b B
c C
```

#### 2.2.6.1 Equality

A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order in which the items were added.

```
# collections_ordereddict_equality.py
import collections

print('dict       :', end=' ')
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

print('OrderedDict:', end=' ')

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = collections.OrderedDict()
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)
```

In this case, since the two ordered dictionaries are created from values in a different order, they are considered to be different.

```
$ python3 collections_ordereddict_equality.py
dict       : True
OrderedDict: False
```