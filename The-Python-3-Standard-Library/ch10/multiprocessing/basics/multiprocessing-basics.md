# [Chapter 10: Concurrency with Processes, Threads, and Coroutines](https://pymotw.com/3/concurrency.html)

## [10.4 multiprocessing — Manage Processes Like Threads](https://pymotw.com/3/multiprocessing/index.html)

### 10.4.1 multiprocessing Basics

The simplest way to spawn a second process is to instantiate a Process object with a target function and call start() to let it begin working.

```
# multiprocessing_simple.py
import multiprocessing


def worker():
    """worker function"""
    print("Worker")


if __name__ == "__main__":
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
```

The output includes the word “Worker” printed five times, although it may not come out entirely clean, depending on the order of execution, because each process is competing for access to the output stream.

```
$ python3 multiprocessing_simple.py
Worker
Worker
Worker
Worker
Worker
```

It usually more useful to be able to spawn a process with arguments to tell it what work to do. Unlike with threading, in order to pass arguments to a multiprocessing Process the arguments must be able to be serialized using pickle. This example passes each worker a number to be printed.

```
# multiprocessing_simpleargs.py
import multiprocessing


def worker(num):
    """thread worker function"""
    print("Worker:", num)


if __name__ == "__main__":
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
```

The integer argument is now included in the message printed by each worker.

```
$ python3 multiprocessing_simpleargs.py
Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
```

### 10.4.2 Importable Target Functions

One difference between the threading and multiprocessing examples is the extra protection for `__main__` used in the multiprocessing examples. Due to the way the new processes are started, the child process needs to be able to import the script containing the target function. Wrapping the main part of the application in a check for `__main__` ensures that it is not run recursively in each child as the module is imported. Another approach is to import the target function from a separate script. For example, multiprocessing_import_main.py uses a worker function defined in a second module.

```
# multiprocessing_import_main.py
import multiprocessing
import multiprocessing_import_worker

if __name__ == "__main__":
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(
            target=multiprocessing_import_worker.worker,
        )
        jobs.append(p)
        p.start()
```

The worker function is defined in multiprocessing_import_worker.py.

```
# multiprocessing_import_worker.py
def worker():
    """worker function"""
    print('Worker')
    return
```

Calling the main program produces output similar to the first example.

```
$ python3 multiprocessing_import_main.py
Worker
Worker
Worker
Worker
Worker
```