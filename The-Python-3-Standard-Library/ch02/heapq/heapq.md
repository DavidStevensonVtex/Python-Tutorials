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