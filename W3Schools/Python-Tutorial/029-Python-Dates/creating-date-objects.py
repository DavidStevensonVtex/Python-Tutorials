# Creating Date Objects

# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.

# Example

# Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The datetime() class also takes parameters for time and timezone 
# (hour, minute, second, microsecond, tzone), but they are optional, 
# and has a default value of 0, (None for timezone).


# $ python3 creating-date-objects.py 
# 2020-05-17 00:00:00