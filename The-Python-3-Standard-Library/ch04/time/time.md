# [Chapter 4: Dates and Times](https://pymotw.com/3/dates.html)

## [4.1 time — Clock Time](https://pymotw.com/3/time/index.html)

Purpose:	Functions for manipulating clock time.

The time module provides access to several different types of clocks, each useful for different purposes. The standard system calls like time() report the system “wall clock” time. The monotonic() clock can be used to measure elapsed time in a long-running process because it is guaranteed never to move backwards, even if the system time is changed. For performance testing, perf_counter() provides access to the clock with the highest available resolution to make short time measurements more accurate. The CPU time is available through clock(), and process_time() returns the combined processor time and system time.

Note

The implementations expose C library functions for manipulating dates and times. Since they are tied to the underlying C implementation, some details (such as the start of the epoch and maximum date value supported) are platform-specific. Refer to the library documentation for complete details.

### 4.1.1 Comparing Clocks

Implementation details for the clocks varies by platform. Use get_clock_info() to access basic information about the current implementation, including the clock’s resolution.

```
# time_get_clock_info.py
import textwrap
import time

available_clocks = [
    ("monotonic", time.monotonic),
    ("perf_counter", time.perf_counter),
    ("process_time", time.process_time),
    ("time", time.time),
]

for clock_name, func in available_clocks:
    print(
        textwrap.dedent(
            """\
    {name}:
        adjustable    : {info.adjustable}
        implementation: {info.implementation}
        monotonic     : {info.monotonic}
        resolution    : {info.resolution}
        current       : {current}
    """
        ).format(name=clock_name, info=time.get_clock_info(clock_name), current=func())
    )
```

This output for Ubuntu 20.04 shows that the monotonic and perf_counter clocks are implemented using the same underlying system call.

```
$ python3 time_get_clock_info.py
monotonic:
    adjustable    : False
    implementation: clock_gettime(CLOCK_MONOTONIC)
    monotonic     : True
    resolution    : 1e-09
    current       : 26489.642705662

perf_counter:
    adjustable    : False
    implementation: clock_gettime(CLOCK_MONOTONIC)
    monotonic     : True
    resolution    : 1e-09
    current       : 26489.642786844

process_time:
    adjustable    : False
    implementation: clock_gettime(CLOCK_PROCESS_CPUTIME_ID)
    monotonic     : True
    resolution    : 1e-09
    current       : 0.039325777

time:
    adjustable    : True
    implementation: clock_gettime(CLOCK_REALTIME)
    monotonic     : False
    resolution    : 1e-09
    current       : 1739390998.1144085
```

### 4.1.2 Wall Clock Time

One of the core functions of the time module is time(), which returns the number of seconds since the start of the “epoch” as a floating point value.

```
# time_time.py
import time

print("The time is:", time.time())
```

The epoch is the start of measurement for time, which for Unix systems is 0:00 on January 1, 1970. Although the value is always a float, actual precision is platform-dependent.

```
$ python3 time_time.py
The time is: 1739391320.1193054
```

The float representation is useful when storing or comparing dates, but not as useful for producing human readable representations. For logging or printing time ctime() can be more useful.

```
# time_ctime.py
import time

print("The time is      :", time.ctime())
later = time.time() + 15
print("15 secs from now :", time.ctime(later))
```

The second print() call in this example shows how to use ctime() to format a time value other than the current time.

```
$ python3 time_ctime.py
The time is      : Wed Feb 12 15:17:37 2025
15 secs from now : Wed Feb 12 15:17:52 2025
```

### 4.1.3 Monotonic Clocks

Because time() looks at the system clock, and the system clock can be changed by the user or system services for synchronizing clocks across multiple computers, calling time() repeatedly may produce values that go forwards and backwards. This can result in unexpected behavior when trying to measure durations or otherwise use those times for computation. Avoid those situations by using monotonic(), which always returns values that go forward.

```
# time_monotonic.py
import time

start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print("start : {:>9.2f}".format(start))
print("end   : {:>9.2f}".format(end))
print("span  : {:>9.2f}".format(end - start))
```

The start point for the monotonic clock is not defined, so return values are only useful for doing calculations with other clock values. In this example the duration of the sleep is measured using monotonic().

```
$ python3 time_monotonic.py
start :  27249.98
end   :  27250.08
span  :      0.10
```

### 4.1.4 Processor Clock Time

While time() returns a wall clock time, process_time() returns processor clock time. The values returned from process_time() reflect the actual time used by the program as it runs.

```
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
```

In this example, the formatted ctime() is printed along with the floating point values from time(), and clock() for each iteration through the loop.

Note

If you want to run the example on your system, you may have to add more cycles to the inner loop or work with a larger amount of data to actually see a difference in the times.

```
$ python3 time_process_time.py
time_process_time.py
Thu Feb 13 14:00:00 2025 : 1739473200.238 0.032
Thu Feb 13 14:00:00 2025 : 1739473200.501 0.295
Thu Feb 13 14:00:00 2025 : 1739473200.702 0.496
Thu Feb 13 14:00:00 2025 : 1739473200.894 0.688
Thu Feb 13 14:00:01 2025 : 1739473201.087 0.882
```

Typically, the processor clock does not tick if a program is not doing anything.

```
# time_clock_sleep.py
import time

template = "{} - {:0.2f} - {:0.2f}"

print(template.format(time.ctime(), time.time(), time.process_time()))

for i in range(3, 0, -1):
    print("Sleeping", i)
    time.sleep(i)
    print(template.format(time.ctime(), time.time(), time.process_time()))
```

In this example, the loop does very little work by going to sleep after each iteration. The time() value increases even while the application is asleep, but the process_time() value does not.

```
$ python3 -u time_clock_sleep.py
Thu Feb 13 14:03:27 2025 - 1739473407.07 - 0.03
Sleeping 3
Thu Feb 13 14:03:30 2025 - 1739473410.07 - 0.03
Sleeping 2
Thu Feb 13 14:03:32 2025 - 1739473412.07 - 0.03
Sleeping 1
Thu Feb 13 14:03:33 2025 - 1739473413.07 - 0.03
```

Calling sleep() yields control from the current thread and asks it to wait for the system to wake it back up. If a program has only one thread, this effectively blocks the app and it does no work.

### 4.1.5 Performance Counter

It is important to have a high-resolution monotonic clock for measuring performance. Determining the best clock data source requires platform-specific knowledge, which Python provides in perf_counter().

```
# time_perf_counter.py
import hashlib
import time

# Data to use to calculate md5 checksums
data = open(__file__, "rb").read()

loop_start = time.perf_counter()

for i in range(5):
    iter_start = time.perf_counter()
    h = hashlib.sha1()
    for i in range(300000):
        h.update(data)
    cksum = h.digest()
    now = time.perf_counter()
    loop_elapsed = now - loop_start
    iter_elapsed = now - iter_start
    print(time.ctime(), ": {:0.3f} {:0.3f}".format(iter_elapsed, loop_elapsed))
```

As with monotonic(), the epoch for perf_counter() is undefined, and the values are meant to be used for comparing and computing values, not as absolute times.

```
$ python3 time_perf_counter.py
Thu Feb 13 14:07:33 2025 : 0.257 0.257
Thu Feb 13 14:07:33 2025 : 0.256 0.513
Thu Feb 13 14:07:33 2025 : 0.264 0.777
Thu Feb 13 14:07:33 2025 : 0.260 1.037
Thu Feb 13 14:07:34 2025 : 0.291 1.329
```