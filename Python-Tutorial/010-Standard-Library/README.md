# [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

[The Python Standard Library](https://docs.python.org/3/library/)

## [10. Brief Tour of the Standard Library](https://docs.python.org/3/tutorial/stdlib.html)

### 10.1. Operating System Interface

The [os](https://docs.python.org/3/library/os.html#module-os) module provides dozens of functions for interacting with the operating system:

```
>>> import os
>>> os.getcwd()         # Return the current working directory
'/home/dstevenson/Python/GitHub/Python-Tutorials/Python-Tutorial'
>>> os.chdir('/home/dstevenson/Python')
>>> os.system('mkdir today')
```

Be sure to use the import os style instead of from os import *. This will keep [os.open()](https://docs.python.org/3/library/os.html#os.open) from shadowing the built-in [open()](https://docs.python.org/3/library/functions.html#open) function which operates much differently.

The built-in [dir()](https://docs.python.org/3/library/functions.html#dir) and [help()](https://docs.python.org/3/library/functions.html#help) functions are useful as interactive aids for working with large modules like os:

```
import os
dir(os)
<returns a list of all module functions>
help(os)
<returns an extensive manual page created from the module's docstrings>
```

For daily file and directory management tasks, the [shutil](https://docs.python.org/3/library/shutil.html#module-shutil) module provides a higher level interface that is easier to use:

```
import shutil
shutil.copyfile('data.db', 'archive.db')
'archive.db'
shutil.move('/build/executables', 'installdir')
'installdir'
```

### 10.2. File Wildcards

The [glob](https://docs.python.org/3/library/glob.html#module-glob) module provides a function for making file lists from directory wildcard searches:

```
import glob
glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

### 10.3. Command Line Arguments

Common utility scripts often need to process command line arguments. These arguments are stored in the sys module’s argv attribute as a list. For instance, let’s take the following demo.py file:

```
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

When run at the command line with python top.py --lines=5 alpha.txt beta.txt, the script sets args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt'].

### 10.4. Error Output Redirection and Program Termination

The [sys](https://docs.python.org/3/library/sys.html#module-sys) module also has attributes for stdin, stdout, and stderr. The latter is useful for emitting warnings and error messages to make them visible even when stdout has been redirected:

```
sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

The most direct way to terminate a script is to use sys.exit().

### 10.5. String Pattern Matching

The [re](https://docs.python.org/3/library/re.html#module-re) module provides regular expression tools for advanced string processing. For complex matching and manipulation, regular expressions offer succinct, optimized solutions:

```
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:

```
'tea for too'.replace('too', 'two')
'tea for two'
```

### 10.6. Mathematics

The [math](https://docs.python.org/3/library/math.html#module-math) module gives access to the underlying C library functions for floating-point math:

```
>>> import math
>>> math.cos(math.pi / 4)
0.7071067811865476
>>> math.log(1024, 2)
10.0
```

The [random](https://docs.python.org/3/library/random.html#module-random) module provides tools for making random selections:

>>>
import random
random.choice(['apple', 'pear', 'banana'])
'apple'
random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
random.random()    # random float from the interval [0.0, 1.0)
0.17970987693706186
random.randrange(6)    # random integer chosen from range(6)
4

```
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[7, 35, 48, 84, 22, 88, 26, 5, 41, 6]
>>> random.random()                 # random float from the interval [0.0, 1.0)
0.7971565029271278
>>> random.randrange(6)             # random integer chosen from range(6)
2
```

The [statistics](https://docs.python.org/3/library/statistics.html#module-statistics) module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:

```
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

The [SciPy project](https://scipy.org) has many other modules for numerical computations.

### 10.7. Internet Access

There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) for retrieving data from URLs and [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib) for sending mail:

```
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline

datetime: 2025-01-12T18:00:11.882054+00:00
```

```
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()
```