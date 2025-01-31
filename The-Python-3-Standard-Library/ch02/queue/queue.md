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

### 2.6.2 LIFO Queue

In contrast to the standard FIFO implementation of Queue, the LifoQueue uses last-in, first-out ordering (normally associated with a stack data structure).

```
# queue_lifo.py
import queue

q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
```

The item most recently put into the queue is removed by get.

```
$ python3 queue_lifo.py
4 3 2 1 0
```

### 2.6.3 Priority Queue

Sometimes the processing order of the items in a queue needs to be based on characteristics of those items, rather than just the order they are created or added to the queue. For example, print jobs from the payroll department may take precedence over a code listing that a developer wants to print. PriorityQueue uses the sort order of the contents of the queue to decide which item to retrieve.

```
# queue_priority.py
import functools
import queue
import threading


@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))

print(q)

def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()


workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]
for w in workers:
    w.setDaemon(True)
    w.start()

q.join()
```

This example has multiple threads consuming the jobs, which are processed based on the priority of items in the queue at the time get() was called. The order of processing for items added to the queue while the consumer threads are running depends on thread context switching.

```
$ python3 queue_priority.py
New job: Mid-level job
New job: Low-level job
New job: Important job
<queue.PriorityQueue object at 0x7f5677eab040>
Processing job: Important job
Processing job: Mid-level job
Processing job: Low-level job
```