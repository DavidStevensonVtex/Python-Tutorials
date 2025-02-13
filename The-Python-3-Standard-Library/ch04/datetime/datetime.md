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