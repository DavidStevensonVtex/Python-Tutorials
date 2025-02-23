# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.5 linecache — Read Text Files Efficiently](https://pymotw.com/3/linecache/index.html)

Purpose:	Retrieve lines of text from files or imported Python modules, holding a cache of the results to make reading many lines from the same file more efficient.

The linecache module is used within other parts of the Python standard library when dealing with Python source files. The implementation of the cache holds the contents of files, parsed into separate lines, in memory. The API returns the requested line(s) by indexing into a list, and saves time over repeatedly reading the file and parsing lines to find the one desired. This is especially useful when looking for multiple lines from the same file, such as when producing a traceback for an error report.

### 6.5.1 Test Data

This text produced by a Lorem Ipsum generator is used as sample input.

```
# linecache_data.py
import os
import tempfile

lorem = """Lorem ipsum dolor sit amet, consectetuer
adipiscing elit.  Vivamus eget elit. In posuere mi non
risus. Mauris id quam posuere lectus sollicitudin
varius. Praesent at mi. Nunc eu velit. Sed augue massa,
fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur
eros pede, egestas at, ultricies ac, apellentesque eu,
tellus.

Sed sed odio sed mi luctus mollis. Integer et nulla ac augue
convallis accumsan. Ut felis. Donec lectus sapien, elementum
nec, condimentum ac, interdum non, tellus. Aenean viverra,
mauris vehicula semper porttitor, ipsum odio consectetuer
lorem, ac imperdiet eros odio a sapien. Nulla mauris tellus,
aliquam non, egestas a, nonummy et, erat. Vivamus sagittis
porttitor eros."""


def make_tempfile():
    fd, temp_file_name = tempfile.mkstemp()
    os.close(fd)
    with open(temp_file_name, "wt") as f:
        f.write(lorem)
    return temp_file_name


def cleanup(filename):
    os.unlink(filename)
```

### 6.5.2 Reading Specific Lines

The line numbers of files read by the linecache module start with 1, but normally lists start indexing the array from 0.

```
# linecache_getline.py
import linecache
from linecache_data import *

filename = make_tempfile()

# Pick out the same line from source and cache.
# (Notice that linecache counts from 1)
print("SOURCE:")
print("{!r}".format(lorem.split("\n")[4]))
print()
print("CACHE:")
print("{!r}".format(linecache.getline(filename, 5)))

cleanup(filename)
```

Each line returned includes a trailing newline.

```
$ python3 linecache_getline.py
SOURCE:
'fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur'

CACHE:
'fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur\n'
```