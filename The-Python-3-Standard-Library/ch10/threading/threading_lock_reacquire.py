# threading_lock_reacquire.py
import threading

lock = threading.Lock()

print("First try :", lock.acquire())
print("Second try:", lock.acquire(0))
