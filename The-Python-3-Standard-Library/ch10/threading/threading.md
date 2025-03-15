# [Chapter 10: Concurrency with Processes, Threads, and Coroutines](https://pymotw.com/3/concurrency.html)

## [10.3 threading — Manage Concurrent Operations Within a Process](https://pymotw.com/3/threading/index.html)

**Purpose:**	Manage several threads of execution.

Using threads allows a program to run multiple operations concurrently in the same process space.

### 10.3.1 Thread Objects

The simplest way to use a Thread is to instantiate it with a target function and call start() to let it begin working.

```
# threading_simple.py
import threading


def worker():
    """thread worker function"""
    print("Worker")


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
```

The output is five lines with "Worker" on each.

```
$ python3 threading_simple.py
Worker
Worker
Worker
Worker
Worker
```

It is useful to be able to spawn a thread and pass it arguments to tell it what work to do. Any type of object can be passed as argument to the thread. This example passes a number, which the thread then prints.

```
# threading_simpleargs.py
import threading


def worker(num):
    """thread worker function"""
    print("Worker: %s" % num)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
```

The integer argument is now included in the message printed by each thread.

```
$ python3 threading_simpleargs.py
Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
```