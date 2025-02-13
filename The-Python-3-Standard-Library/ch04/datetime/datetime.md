# [Chapter 4: Dates and Times](https://pymotw.com/3/dates.html)

## [4.2 datetime — Date and Time Value Manipulation](https://pymotw.com/3/datetime/index.html)

Purpose:	The datetime module includes functions and classes for doing date and time parsing, formatting, and arithmetic.

datetime contains functions and classes for working with dates and times, separately and together.

### 4.2.1 Times

Time values are represented with the time class. A time instance has attributes for hour, minute, second, and microsecond and can also include time zone information.

```
# datetime_time.py
import datetime

t = datetime.time(1, 2, 3)
print(t)
print("hour       :", t.hour)
print("minute     :", t.minute)
print("second     :", t.second)
print("microsecond:", t.microsecond)
print("tzinfo     :", t.tzinfo)
```

The arguments to initialize a time instance are optional, but the default of 0 is unlikely to be correct.

```
$ python3 datetime_time.py
01:02:03
hour       : 1
minute     : 2
second     : 3
microsecond: 0
tzinfo     : None
```

A time instance only holds values of time, and not a date associated with the time.

```
# datetime_time_minmax.py
import datetime

print("Earliest  :", datetime.time.min)
print("Latest    :", datetime.time.max)
print("Resolution:", datetime.time.resolution)
```

The min and max class attributes reflect the valid range of times in a single day.

```
$ python3 datetime_time_minmax.py
Earliest  : 00:00:00
Latest    : 23:59:59.999999
Resolution: 0:00:00.000001
```

The resolution for time is limited to whole microseconds.

```
# datetime_time_resolution.py
import datetime

for m in [1, 0, 0.1, 0.6]:
    try:
        print("{:02.1f} :".format(m), datetime.time(0, 0, 0, microsecond=m))
    except TypeError as err:
        print("ERROR:", err)
```

Floating point values for microseconds cause a TypeError.

```
$ python3 datetime_time_resolution.py
1.0 : 00:00:00.000001
0.0 : 00:00:00
ERROR: integer argument expected, got float
ERROR: integer argument expected, got float
```

### 4.2.2 Dates

Calendar date values are represented with the date class. Instances have attributes for year, month, and day. It is easy to create a date representing the current date using the `today()` class method.

```
# datetime_date.py
import datetime

today = datetime.date.today()
print(today)
print("ctime  :", today.ctime())
tt = today.timetuple()
print(tt)
print("tuple  : tm_year  =", tt.tm_year)
print("         tm_mon   =", tt.tm_mon)
print("         tm_mday  =", tt.tm_mday)
print("         tm_hour  =", tt.tm_hour)
print("         tm_min   =", tt.tm_min)
print("         tm_sec   =", tt.tm_sec)
print("         tm_wday  =", tt.tm_wday)
print("         tm_yday  =", tt.tm_yday)
print("         tm_isdst =", tt.tm_isdst)
print("ordinal:", today.toordinal())
print("Year   :", today.year)
print("Mon    :", today.month)
print("Day    :", today.day)
```

This example prints the current date in several formats:

```
$ python3 datetime_date.py
2025-02-13
ctime  : Thu Feb 13 00:00:00 2025
time.struct_time(tm_year=2025, tm_mon=2, tm_mday=13, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=44, tm_isdst=-1)
tuple  : tm_year  = 2025
         tm_mon   = 2
         tm_mday  = 13
         tm_hour  = 0
         tm_min   = 0
         tm_sec   = 0
         tm_wday  = 3
         tm_yday  = 44
         tm_isdst = -1
ordinal: 739295
Year   : 2025
Mon    : 2
Day    : 13
```

There are also class methods for creating instances from POSIX timestamps or integers representing date values from the Gregorian calendar, where January 1 of the year 1 is 1 and each subsequent day increments the value by 1.

```
# datetime_date_fromordinal.py
import datetime
import time

o = 733114
print("o               :", o)
print("fromordinal(o)  :", datetime.date.fromordinal(o))

t = time.time()
print("t               :", t)
print("fromtimestamp(t):", datetime.date.fromtimestamp(t))
```

This example illustrates the different value types used by fromordinal() and fromtimestamp().

```
$ python3 datetime_date_fromordinal.py
o               : 733114
fromordinal(o)  : 2008-03-13
t               : 1739476601.2556498
fromtimestamp(t): 2025-02-13
```

As with time, the range of date values supported can be determined using the min and max attributes.

```
# datetime_date_minmax.py
import datetime

print("Earliest  :", datetime.date.min)
print("Latest    :", datetime.date.max)
print("Resolution:", datetime.date.resolution)
```

The resolution for dates is whole days.

```
$ python3 datetime_date_minmax.py
Earliest  : 0001-01-01
Latest    : 9999-12-31
Resolution: 1 day, 0:00:00
```

Another way to create new date instances uses the replace() method of an existing date.

```
# datetime_date_replace.py
import datetime

d1 = datetime.date(2008, 3, 29)
print("d1:", d1.ctime())

d2 = d1.replace(year=2009)
print("d2:", d2.ctime())
```

This example changes the year, leaving the day and month unmodified.

```
$ python3 datetime_date_replace.py
d1: Sat Mar 29 00:00:00 2008
d2: Sun Mar 29 00:00:00 2009
```

### 4.2.3 timedeltas

Future and past dates can be calculated using basic arithmetic on two datetime objects, or by combining a datetime with a timedelta. Subtracting dates produces a timedelta, and a timedelta can be added or subtracted from a date to produce another date. The internal values for a timedelta are stored in days, seconds, and microseconds.

```
# datetime_timedelta.py
import datetime

print("microseconds:", datetime.timedelta(microseconds=1))
print("milliseconds:", datetime.timedelta(milliseconds=1))
print("seconds     :", datetime.timedelta(seconds=1))
print("minutes     :", datetime.timedelta(minutes=1))
print("hours       :", datetime.timedelta(hours=1))
print("days        :", datetime.timedelta(days=1))
print("weeks       :", datetime.timedelta(weeks=1))
```

Intermediate level values passed to the constructor are converted into days, seconds, and microseconds.

```
$ python3 datetime_timedelta.py
microseconds: 0:00:00.000001
milliseconds: 0:00:00.001000
seconds     : 0:00:01
minutes     : 0:01:00
hours       : 1:00:00
days        : 1 day, 0:00:00
weeks       : 7 days, 0:00:00
```

The full duration of a timedelta can be retrieved as a number of seconds using total_seconds().

```
# datetime_timedelta_total_seconds.py
import datetime

for delta in [
    datetime.timedelta(microseconds=1),
    datetime.timedelta(milliseconds=1),
    datetime.timedelta(seconds=1),
    datetime.timedelta(minutes=1),
    datetime.timedelta(hours=1),
    datetime.timedelta(days=1),
    datetime.timedelta(weeks=1),
]:
    print("{:15} = {:8} seconds".format(str(delta), delta.total_seconds()))
```

The return value is a floating point number, to accommodate sub-second durations.

```
$ python3 datetime_timedelta_total_seconds.py
0:00:00.000001  =    1e-06 seconds
0:00:00.001000  =    0.001 seconds
0:00:01         =      1.0 seconds
0:01:00         =     60.0 seconds
1:00:00         =   3600.0 seconds
1 day, 0:00:00  =  86400.0 seconds
7 days, 0:00:00 = 604800.0 seconds
```

### 4.2.4 Date Arithmetic

Date math uses the standard arithmetic operators.

```
# datetime_date_math.py
import datetime

today = datetime.date.today()
print("Today    :", today)

one_day = datetime.timedelta(days=1)
print("One day  :", one_day)

yesterday = today - one_day
print("Yesterday:", yesterday)

tomorrow = today + one_day
print("Tomorrow :", tomorrow)

print()
print("tomorrow - yesterday:", tomorrow - yesterday)
print("yesterday - tomorrow:", yesterday - tomorrow)
```

This example with date objects illustrates using timedelta objects to compute new dates, and subtracting date instances to produce timedeltas (including a negative delta value).

```
$ python3 datetime_date_math.py
Today    : 2025-02-13
One day  : 1 day, 0:00:00
Yesterday: 2025-02-12
Tomorrow : 2025-02-14

tomorrow - yesterday: 2 days, 0:00:00
yesterday - tomorrow: -2 days, 0:00:00
```

A timedelta object also supports arithmetic with integers, floats, and other timedelta instances.

```
# datetime_timedelta_math.py
import datetime

one_day = datetime.timedelta(days=1)
print("1 day    :", one_day)
print("5 days   :", one_day * 5)
print("1.5 days :", one_day * 1.5)
print("1/4 day  :", one_day / 4)

# assume an hour for lunch
work_day = datetime.timedelta(hours=7)
meeting_length = datetime.timedelta(hours=1)
print("meetings per day :", work_day / meeting_length)
```

In this example, several multiples of a single day are computed, with the resulting timedelta holding the appropriate number of days or hours. The final example demonstrates how to compute values by combining two timedelta objects. In this case, the result is a floating point number.

```
$ python3 datetime_timedelta_math.py
1 day    : 1 day, 0:00:00
5 days   : 5 days, 0:00:00
1.5 days : 1 day, 12:00:00
1/4 day  : 6:00:00
meetings per day : 7.0
```