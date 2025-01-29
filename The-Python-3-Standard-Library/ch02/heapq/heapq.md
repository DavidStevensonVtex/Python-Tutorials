# Chapter 2: [Data Structures](https://pymotw.com/3/data_structures.html)

## [2.4 heapq – Heap Sort Algorithm](https://pymotw.com/3/heapq/index.html)

Purpose:	The heapq implements a min-heap sort algorithm suitable for use with Python’s lists.

A heap is a tree-like data structure in which the child nodes have a sort-order relationship with the parents. Binary heaps can be represented using a list or array organized so that the children of element N are at positions 2 * N + 1 and 2 * N + 2 (for zero-based indexes). This layout makes it possible to rearrange heaps in place, so it is not necessary to reallocate as much memory when adding or removing items.

A max-heap ensures that the parent is larger than or equal to both of its children. A min-heap requires that the parent be less than or equal to its children. Python’s heapq module implements a min-heap.

### 2.4.1 Example Data

The examples in this section use the data in heapq_heapdata.py.

```
# heapq_heapdata.py
# This data was generated with the random module.

data = [19, 9, 4, 10, 11]
```

The heap output is printed using heapq_showtree.py.

```
# heapq_showtree.py
import math
from io import StringIO


def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()
```

### 2.4.2 Creating a Heap

There are two basic ways to create a heap: heappush() and heapify().

```
# heapq_heappush.py
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)
```

When heappush() is used, the heap sort order of the elements is maintained as new items are added from a data source.

```
$ python3 heapq_heappush.py
random : [19, 9, 4, 10, 11]

add  19:

                 19                 
------------------------------------

add   9:

                 9                  
        19        
------------------------------------

add   4:

                 4                  
        19                9         
------------------------------------

add  10:

                 4                  
        10                9         
    19   
------------------------------------

add  11:

                 4                  
        10                9         
    19       11   
------------------------------------
```

If the data is already in memory, it is more efficient to use heapify() to rearrange the items of the list in place.

```
# heapq_heapify.py
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print('random    :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)
```

The result of building a list in heap order one item at a time is the same as building an unordered list and then calling heapify().

```
$ python3 heapq_heapify.py
random    : [19, 9, 4, 10, 11]
heapified :

                 4                  
        9                 19        
    10       11   
------------------------------------
```