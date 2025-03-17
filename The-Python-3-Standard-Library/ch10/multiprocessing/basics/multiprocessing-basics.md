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

### 10.4.3 Determining the Current Process

Passing arguments to identify or name the process is cumbersome, and unnecessary. Each Process instance has a name with a default value that can be changed as the process is created. Naming processes is useful for keeping track of them, especially in applications with multiple types of processes running simultaneously.

```
# multiprocessing_names.py
import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    print(name, "Starting")
    time.sleep(2)
    print(name, "Exiting")


def my_service():
    name = multiprocessing.current_process().name
    print(name, "Starting")
    time.sleep(3)
    print(name, "Exiting")


if __name__ == "__main__":
    service = multiprocessing.Process(
        name="my_service",
        target=my_service,
    )
    worker_1 = multiprocessing.Process(
        name="worker 1",
        target=worker,
    )
    worker_2 = multiprocessing.Process(  # default name
        target=worker,
    )

    worker_1.start()
    worker_2.start()
    service.start()
```

The debug output includes the name of the current process on each line. The lines with Process-3 in the name column correspond to the unnamed process worker_2.

```
$ python3 multiprocessing_names.py
worker 1 Starting
Process-3 Starting
my_service Starting
worker 1 Exiting
Process-3 Exiting
my_service Exiting
```

### 10.4.4 Daemon Processes

By default, the main program will not exit until all of the children have exited. There are times when starting a background process that runs without blocking the main program from exiting is useful, such as in services where there may not be an easy way to interrupt the worker, or where letting it die in the middle of its work does not lose or corrupt data (for example, a task that generates “heart beats” for a service monitoring tool).

To mark a process as a daemon, set its daemon attribute to True. The default is for processes to not be daemons.

```
# multiprocessing_daemon.py
import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print("Starting:", p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print("Exiting :", p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print("Starting:", p.name, p.pid)
    sys.stdout.flush()
    print("Exiting :", p.name, p.pid)
    sys.stdout.flush()


if __name__ == "__main__":
    d = multiprocessing.Process(
        name="daemon",
        target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
        name="non-daemon",
        target=non_daemon,
    )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
```

The output does not include the “Exiting” message from the daemon process, since all of the non-daemon processes (including the main program) exit before the daemon process wakes up from its two second sleep.

```
$ python3 multiprocessing_daemon.py
Starting: daemon 22111
Starting: non-daemon 22123
Exiting : non-daemon 22123
```

The daemon process is terminated automatically before the main program exits, which avoids leaving orphaned processes running. This can be verified by looking for the process id value printed when the program runs, and then checking for that process with a command like ps.