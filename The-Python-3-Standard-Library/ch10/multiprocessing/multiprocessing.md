# [Chapter 10: Concurrency with Processes, Threads, and Coroutines](https://pymotw.com/3/concurrency.html)

## [10.4 multiprocessing — Manage Processes Like Threads](https://pymotw.com/3/multiprocessing/index.html)

**Purpose:**	Provides an API for managing processes.

The multiprocessing module includes an API for dividing work up between multiple processes based on the API for threading. In some cases multiprocessing is a drop-in replacement, and can be used instead of threading to take advantage of multiple CPU cores to avoid computational bottlenecks associated with Python’s global interpreter lock.

Due to the similarity, the first few examples here are modified from the threading examples. Features provided by multiprocessing but not available in threading are covered later.

* [multiprocessing Basics](https://pymotw.com/3/multiprocessing/basics.html)
* [Importable Target Functions](https://pymotw.com/3/multiprocessing/basics.html#importable-target-functions)
* [Determining the Current Process](https://pymotw.com/3/multiprocessing/basics.html#determining-the-current-process)
* [Daemon Processes](https://pymotw.com/3/multiprocessing/basics.html#daemon-processes)
* [Waiting for Processes](https://pymotw.com/3/multiprocessing/basics.html#waiting-for-processes)
* [Terminating Processes](https://pymotw.com/3/multiprocessing/basics.html#terminating-processes)
* [Process Exit Status](https://pymotw.com/3/multiprocessing/basics.html#process-exit-status)
* [Logging](https://pymotw.com/3/multiprocessing/basics.html#logging)
* [Subclassing Process](https://pymotw.com/3/multiprocessing/basics.html#subclassing-process)
* [Passing Messages to Processes](https://pymotw.com/3/multiprocessing/communication.html)
* [Signaling between Processes](https://pymotw.com/3/multiprocessing/communication.html#signaling-between-processes)
* [Controlling Access to Resources](https://pymotw.com/3/multiprocessing/communication.html#controlling-access-to-resources)
* [Synchronizing Operations](https://pymotw.com/3/multiprocessing/communication.html#synchronizing-operations)
* [Controlling Concurrent Access to Resources](https://pymotw.com/3/multiprocessing/communication.html#controlling-concurrent-access-to-resources)
* [Managing Shared State](https://pymotw.com/3/multiprocessing/communication.html#managing-shared-state)
* [Shared Namespaces](https://pymotw.com/3/multiprocessing/communication.html#shared-namespaces)
* [Process Pools](https://pymotw.com/3/multiprocessing/communication.html#process-pools)
* [Implementing MapReduce](https://pymotw.com/3/multiprocessing/mapreduce.html)

### See also

* [Standard library documentation for multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
* [threading](https://pymotw.com/3/threading/index.html#module-threading) – High-level API for working with threads.
* [MapReduce - Wikipedia](https://en.wikipedia.org/wiki/MapReduce) – Overview of MapReduce on Wikipedia.
* [MapReduce: Simplified Data Processing on Large Clusters](https://research.google.com/archive/mapreduce.html) – Google Labs presentation and paper on MapReduce.
* [operator](https://pymotw.com/3/operator/index.html#module-operator) – Operator tools such as itemgetter.