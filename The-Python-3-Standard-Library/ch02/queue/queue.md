# Chapter 2: [Data Structures](https://pymotw.com/3/data_structures.html)

## [2.6 queue — Thread-Safe FIFO Implementation](https://pymotw.com/3/queue/index.html)

Purpose:	Provides a thread-safe FIFO implementation

The queue module provides a first-in, first-out (FIFO) data structure suitable for multi-threaded programming. It can be used to pass messages or other data between producer and consumer threads safely. Locking is handled for the caller, so many threads can work with the same Queue instance safely and easily. The size of a Queue (the number of elements it contains) may be restricted to throttle memory usage or processing.

Note

This discussion assumes you already understand the general nature of a queue. If you do not, you may want to read some of the references before continuing.

### 2.6.1 Basic FIFO Queue

The Queue class implements a basic first-in, first-out container. Elements are added to one “end” of the sequence using put(), and removed from the other end using get().

```
# queue_fifo.py
import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
```

This example uses a single thread to illustrate that elements are removed from the queue in the same order in which they are inserted.

```
$ python3 queue_fifo.py
0 1 2 3 4 
```


