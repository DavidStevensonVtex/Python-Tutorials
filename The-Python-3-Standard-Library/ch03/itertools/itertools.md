# [Chapter 3 Algorithms](https://pymotw.com/3/algorithm_tools.html)

## [3.2 itertools — Iterator Functions](https://pymotw.com/3/itertools/index.html)

Purpose:	The itertools module includes a set of functions for working with sequence data sets.

The functions provided by itertools are inspired by similar features of functional programming languages such as Clojure, Haskell, APL, and SML. They are intended to be fast and use memory efficiently, and also to be hooked together to express more complicated iteration-based algorithms.

Iterator-based code offers better memory consumption characteristics than code that uses lists. Since data is not produced from the iterator until it is needed, all of the data does not need to be stored in memory at the same time. This “lazy” processing model can reduce swapping and other side-effects of large data sets, improving performance.

In addition to the functions defined in itertools, the examples in this section also rely on some of the built-in functions for iteration.

### 3.2.1 Merging and Splitting Iterators

The chain() function takes several iterators as arguments and returns a single iterator that produces the contents of all of the inputs as though they came from a single iterator.

```
# itertools_chain.py
from itertools import *

for i in chain([1, 2, 3], ["a", "b", "c"]):
    print(i, end=" ")
print()

```

chain() makes it easy to process several sequences without constructing one large list.

```
$ python3 itertools_chain.py
1 2 3 a b c
```

If the iterables to be combined are not all known in advance, or need to be evaluated lazily, chain.from_iterable() can be used to construct the chain instead.

```
# itertools_chain_from_iterable.py
from itertools import *


def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ["a", "b", "c"]


for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=" ")
print()
```

```
$ python3 itertools_chain_from_iterable.py
1 2 3 a b c
```

The built-in function zip() returns an iterator that combines the elements of several iterators into tuples.

```
# itertools_zip.py
for i in zip([1, 2, 3], ["a", "b", "c"]):
    print(i)
```

As with the other functions in this module, the return value is an iterable object that produces values one at a time.

```
$ python3 itertools_zip.py 
(1, 'a')
(2, 'b')
(3, 'c')
```

zip() stops when the first input iterator is exhausted. To process all of the inputs, even if the iterators produce different numbers of values, use zip_longest().

```
# itertools_zip_longest.py
from itertools import *

r1 = range(3)
r2 = range(2)

print("zip stops early:")
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)

print("\nzip_longest processes all of the values:")
print(list(zip_longest(r1, r2)))

for i in zip_longest(r1, r2):
    print(i)
```

By default, zip_longest() substitutes None for any missing values. Use the fillvalue argument to use a different substitute value.

```
$ python3 itertools_zip_longest.py 
zip stops early:
[(0, 0), (1, 1)]

zip_longest processes all of the values:
[(0, 0), (1, 1), (2, None)]
(0, 0)
(1, 1)
(2, None)
```

The islice() function returns an iterator which returns selected items from the input iterator, by index.

```
# itertools_islice.py
from itertools import *

print("Stop at 5:")
for i in islice(range(100), 5):
    print(i, end=" ")
print("\n")

print("Start at 5, Stop at 10:")
for i in islice(range(100), 5, 10):
    print(i, end=" ")
print("\n")

print("By tens to 100:")
for i in islice(range(100), 0, 100, 10):
    print(i, end=" ")
print("\n")
```

islice() takes the same arguments as the slice operator for lists: start, stop, and step. The start and step arguments are optional.

```
$ python3 itertools_islice.py
Stop at 5:
0 1 2 3 4 

Start at 5, Stop at 10:
5 6 7 8 9 

By tens to 100:
0 10 20 30 40 50 60 70 80 90 
```

The tee() function returns several independent iterators (defaults to 2) based on a single original input.

```
# itertools_tee.py
from itertools import *

r = islice(count(), 5)

i1, i2 = tee(r)

print("i1:", list(i1))
print("i2:", list(i2))
```

tee() has semantics similar to the Unix tee utility, which repeats the values it reads from its input and writes them to a named file and standard output. The iterators returned by tee() can be used to feed the same set of data into multiple algorithms to be processed in parallel.

```
$ python3 itertools_tee.py
i1: [0, 1, 2, 3, 4]
i2: [0, 1, 2, 3, 4]
```

The new iterators created by tee() share their input, so the original iterator should not be used after the new ones are created.

```
# itertools_tee_error.py
from itertools import *

r = islice(count(), 5)
i1, i2 = tee(r)

print("r:", end=" ")
for i in r:
    print(i, end=" ")
    if i > 1:
        break
print()

print("i1:", list(i1))
print("i2:", list(i2))
```

If values are consumed from the original input, the new iterators will not produce those values:

```
$ python3 itertools_tee_error.py
r: 0 1 2 
i1: [3, 4]
i2: [3, 4]
```
