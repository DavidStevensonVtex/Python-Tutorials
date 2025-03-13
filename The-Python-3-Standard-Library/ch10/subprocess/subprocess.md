# [Chapter 10: Concurrency with Processes, Threads, and Coroutines](https://pymotw.com/3/concurrency.html)

## [10.1 subprocess — Spawning Additional Processes](https://pymotw.com/3/subprocess/index.html)

**Purpose:**	Start and communicate with additional processes.

The subprocess module supports three APIs for working with processes. The run() function, added in Python 3.5, is a high-level API for running a process and optionally collecting its output. The functions call(), check_call(), and check_output() are the former high-level API, carried over from Python 2. They are still supported and widely used in existing programs. The class Popen is a low-level API used to build the other APIs and useful for more complex process interactions. The constructor for Popen takes arguments to set up the new process so the parent can communicate with it via pipes. It provides all of the functionality of the other modules and functions it replaces, and more. The API is consistent for all uses, and many of the extra steps of overhead needed (such as closing extra file descriptors and ensuring the pipes are closed) are “built in” instead of being handled by the application code separately.

The subprocess module is intended to replace functions such as os.system(), os.spawnv(), the variations of popen() in the os and popen2 modules, as well as the commands() module. To make it easier to compare subprocess with those other modules, many of the examples in this section re-create the ones used for os and popen2.

Note

The API for working on Unix and Windows is roughly the same, but the underlying implementation is different because of the difference in process models in the operating systems. All of the examples shown here were tested on Mac OS X. Behavior on a non-Unix OS may vary.