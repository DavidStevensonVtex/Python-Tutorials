# os_kill_example.py
import os
import signal
import time


def signal_usr1(signum, frame):
    "Callback invoked when a signal is received"
    pid = os.getpid()
    print("Received USR1 in process {}".format(pid))


print("Forking...")
child_pid = os.fork()
if child_pid:
    print("PARENT: pid: ", os.getpid())
    print("PARENT: Pausing before sending signal...")
    time.sleep(1)
    print("PARENT: Signaling {}".format(child_pid))
    os.kill(child_pid, signal.SIGUSR1)
else:
    print("CHILD: pid: ", os.getpid())
    print("CHILD: Setting up signal handler")
    signal.signal(signal.SIGUSR1, signal_usr1)
    print("CHILD: Pausing to wait for signal")
    time.sleep(5)
