# [Chapter 10: Concurrency with Processes, Threads, and Coroutines](https://pymotw.com/3/concurrency.html)

Python includes sophisticated tools for managing concurrent operations using processes and threads. Even many relatively simple programs can be made to run faster by applying techniques for running parts of the job concurrently using these modules.

[subprocess](https://pymotw.com/3/subprocess/index.html) provides an API for creating and communicating with secondary processes. It is especially good for running programs that produce or consume text, since the API supports passing data back and forth through the standard input and output channels of the new process.

The [signal](https://pymotw.com/3/signal/index.html) module exposes the Unix signal mechanism for sending events to other processes. The signals are processed asynchronously, usually by interrupting what the program is doing at the time the signal arrives. Signalling is useful as a coarse messaging system, but other inter-process communication techniques are more reliable and can deliver more complicated messages.

[threading](https://pymotw.com/3/threading/index.html) includes a high-level, object oriented, API for working with concurrency from Python. Thread objects run concurrently within the same process and share memory. Using threads is an easy way to scale for tasks that are more I/O bound than CPU bound.

The [multiprocessing](https://pymotw.com/3/multiprocessing/index.html) module mirrors [threading](https://pymotw.com/3/threading/index.html), except that instead of a Thread class it provides a Process. Each Process is a true system process without shared memory, but [multiprocessing](https://pymotw.com/3/multiprocessing/index.html) provides features for sharing data and passing messages between them so that in many cases converting from threads to processes is as simple as changing a few import statements.

[asyncio](https://pymotw.com/3/asyncio/index.html) provides a framework for concurrency and asynchronous I/O management using either a class-based protocol system or coroutines. asyncio replaces the old asyncore and asynchat modules, which are still available but deprecated.

[concurrent.futures](https://pymotw.com/3/concurrent.futures/index.html) provides implementation of thread and process-based executors for managing resources pools for running concurrent tasks.

* [subprocess — Spawning Additional Processes](https://pymotw.com/3/subprocess/index.html)
* [signal — Asynchronous System Events](https://pymotw.com/3/signal/index.html)
* [threading — Manage Concurrent Operations Within a Process](https://pymotw.com/3/threading/index.html)
* [multiprocessing — Manage Processes Like Threads](https://pymotw.com/3/multiprocessing/index.html)
* [asyncio — Asynchronous I/O, event loop, and concurrency tools](https://pymotw.com/3/asyncio/index.html)
* [concurrent.futures — Manage Pools of Concurrent Tasks](https://pymotw.com/3/concurrent.futures/index.html)