# [Chapter 4: Dates and Times](https://pymotw.com/3/dates.html)

Python does not include native types for dates and times as it does for int, float, and str, but there are three modules for manipulating date and time values in several representations.

The [time](https://pymotw.com/3/time/index.html#module-time) module exposes the time-related functions from the underlying C library. It includes functions for retrieving the clock time and the processor run time, as well as basic parsing and string formatting tools.

The [datetime](https://pymotw.com/3/datetime/index.html#module-datetime) module provides a higher level interface for date, time, and combined values. The classes in datetime support arithmetic, comparison, and time zone configuration.

The [calendar](https://pymotw.com/3/calendar/index.html#module-calendar) module creates formatted representations of weeks, months, and years. It can also be used to compute recurring events, the day of the week for a given date, and other calendar-based values.

* [time — Clock Time](https://pymotw.com/3/time/index.html)
* [datetime — Date and Time Value Manipulation](https://pymotw.com/3/datetime/index.html)
* [calendar — Work with Dates](https://pymotw.com/3/calendar/index.html)

## [4.1 time — Clock Time](https://pymotw.com/3/time/index.html)

Purpose:	Functions for manipulating clock time.

The time module provides access to several different types of clocks, each useful for different purposes. The standard system calls like time() report the system “wall clock” time. The monotonic() clock can be used to measure elapsed time in a long-running process because it is guaranteed never to move backwards, even if the system time is changed. For performance testing, perf_counter() provides access to the clock with the highest available resolution to make short time measurements more accurate. The CPU time is available through clock(), and process_time() returns the combined processor time and system time.

Note

The implementations expose C library functions for manipulating dates and times. Since they are tied to the underlying C implementation, some details (such as the start of the epoch and maximum date value supported) are platform-specific. Refer to the library documentation for complete details.