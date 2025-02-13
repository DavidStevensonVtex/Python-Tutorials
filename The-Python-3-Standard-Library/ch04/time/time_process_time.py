# time_process_time.py
import hashlib
import time

# Data to use to calculate md5 checksums
print(__file__)
data = open(__file__, "rb").read()

for i in range(5):
    h = hashlib.sha1()
    print(time.ctime(), ": {:0.3f} {:0.3f}".format(time.time(), time.process_time()))
    for i in range(300000):
        h.update(data)
    cksum = h.digest()
