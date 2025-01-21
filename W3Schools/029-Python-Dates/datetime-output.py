# Date Output

# When we execute the code from the example above the result will be:

# 2025-01-21 09:18:50.800680

# The date contains year, month, day, hour, minute, second, and microsecond.

# The datetime module has many methods to return information about the date object.

# Here are a few examples, you will learn more about them later in this chapter:

# Example

# Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# $ python3 datetime-output.py 
# 2025
# Tuesday