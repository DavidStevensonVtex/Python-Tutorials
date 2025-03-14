# os_fork_example.py
import os

print("pid of this process: ", os.getpid())
pid = os.fork()

if pid:
    print("Child process id:", pid)
else:
    print("I am the child")
