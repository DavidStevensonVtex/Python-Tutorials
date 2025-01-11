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