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