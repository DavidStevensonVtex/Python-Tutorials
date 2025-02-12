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