# [Chapter 10: Concurrency with Processes, Threads, and Coroutines](https://pymotw.com/3/concurrency.html)

## [10.4.10 Passing Messages to Processes](https://pymotw.com/3/multiprocessing/communication.html)

As with threads, a common use pattern for multiple processes is to divide a job up among several workers to run in parallel. Effective use of multiple processes usually requires some communication between them, so that work can be divided and results can be aggregated. A simple way to communicate between processes with multiprocessing is to use a Queue to pass messages back and forth. Any object that can be serialized with pickle can pass through a Queue.

```
# multiprocessing_queue.py
import multiprocessing


class MyFancyClass:

    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print("Doing something fancy in {} for {}!".format(proc_name, self.name))


def worker(q):
    obj = q.get()
    obj.do_something()


if __name__ == "__main__":
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()

    queue.put(MyFancyClass("Fancy Dan"))

    # Wait for the worker to finish
    queue.close()
    queue.join_thread()
    p.join()
```

This short example only passes a single message to a single worker, then the main process waits for the worker to finish.

```
$ python3 multiprocessing_queue.py
Doing something fancy in Process-1 for Fancy Dan!
```

A more complex example shows how to manage several workers consuming data from a JoinableQueue and passing results back to the parent process. The poison pill technique is used to stop the workers. After setting up the real tasks, the main program adds one “stop” value per worker to the job queue. When a worker encounters the special value, it breaks out of its processing loop. The main process uses the task queue’s join() method to wait for all of the tasks to finish before processing the results.

```
# multiprocessing_producer_consumer.py
import multiprocessing
import time


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                print("{}: Exiting".format(proc_name))
                self.task_queue.task_done()
                break
            print("{}: {}".format(proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)


class Task:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)  # pretend to take time to do the work
        return "{self.a} * {self.b} = {product}".format(
            self=self, product=self.a * self.b
        )

    def __str__(self):
        return "{self.a} * {self.b}".format(self=self)


if __name__ == "__main__":
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # Start consumers
    num_consumers = multiprocessing.cpu_count() * 2
    print("Creating {} consumers".format(num_consumers))
    consumers = [Consumer(tasks, results) for i in range(num_consumers)]
    for w in consumers:
        w.start()

    # Enqueue jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()

    # Start printing results
    while num_jobs:
        result = results.get()
        print("Result:", result)
        num_jobs -= 1
```

Although the jobs enter the queue in order, their execution is parallelized so there is no guarantee about the order they will be completed.

```
$ python3 -u multiprocessing_producer_consumer.py
Creating 8 consumers
Consumer-1: 0 * 0
Consumer-3: 2 * 2
Consumer-2: 3 * 3
Consumer-4: 4 * 4
Consumer-5: 5 * 5
Consumer-8: 1 * 1
Consumer-7: 6 * 6
Consumer-6: 7 * 7
Consumer-4: 8 * 8
Consumer-5: 9 * 9
Consumer-3: Exiting
Consumer-8: Exiting
Consumer-1: Exiting
Consumer-6: Exiting
Consumer-7: Exiting
Consumer-2: Exiting
Consumer-4: Exiting
Consumer-5: Exiting
Result: 4 * 4 = 16
Result: 5 * 5 = 25
Result: 2 * 2 = 4
Result: 1 * 1 = 1
Result: 0 * 0 = 0
Result: 7 * 7 = 49
Result: 6 * 6 = 36
Result: 3 * 3 = 9
Result: 8 * 8 = 64
Result: 9 * 9 = 81
```

### 10.4.11 Signaling between Processes

The Event class provides a simple way to communicate state information between processes. An event can be toggled between set and unset states. Users of the event object can wait for it to change from unset to set, using an optional timeout value.

```
# multiprocessing_event.py
import multiprocessing
import time


def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    print("wait_for_event: starting")
    e.wait()
    print("wait_for_event: e.is_set()->", e.is_set())


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    print("wait_for_event_timeout: starting")
    e.wait(t)
    print("wait_for_event_timeout: e.is_set()->", e.is_set())


if __name__ == "__main__":
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(
        name="block",
        target=wait_for_event,
        args=(e,),
    )
    w1.start()

    w2 = multiprocessing.Process(
        name="nonblock",
        target=wait_for_event_timeout,
        args=(e, 2),
    )
    w2.start()

    print("main: waiting before calling Event.set()")
    time.sleep(3)
    e.set()
    print("main: event is set")
```

When wait() times out it returns without an error. The caller is responsible for checking the state of the event using is_set().

```
$ python3 -u multiprocessing_event.py
main: waiting before calling Event.set()
wait_for_event: starting
wait_for_event_timeout: starting
wait_for_event_timeout: e.is_set()-> False
main: event is set
wait_for_event: e.is_set()-> True
```

### 10.4.12 Controlling Access to Resources

In situations when a single resource needs to be shared between multiple processes, a Lock can be used to avoid conflicting accesses.

```
# multiprocessing_lock.py
import multiprocessing
import sys


def worker_with(lock, stream):
    with lock:
        stream.write("Lock acquired via with\n")


def worker_no_with(lock, stream):
    lock.acquire()
    try:
        stream.write("Lock acquired directly\n")
    finally:
        lock.release()


lock = multiprocessing.Lock()
w = multiprocessing.Process(
    target=worker_with,
    args=(lock, sys.stdout),
)
nw = multiprocessing.Process(
    target=worker_no_with,
    args=(lock, sys.stdout),
)

w.start()
nw.start()

w.join()
nw.join()
```

In this example, the messages printed to the console may be jumbled together if the two processes do not synchronize their access of the output stream with the lock.

```
$ python3 multiprocessing_lock.py
Lock acquired via with
Lock acquired directly
```