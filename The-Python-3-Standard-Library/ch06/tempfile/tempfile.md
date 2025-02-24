# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.6 tempfile — Temporary File System Objects](https://pymotw.com/3/tempfile/index.html)

Purpose:	Create temporary file system objects.

Creating temporary files with unique names securely, so they cannot be guessed by someone wanting to break the application or steal the data, is challenging. The tempfile module provides several functions for creating temporary file system resources securely. TemporaryFile() opens and returns an unnamed file, NamedTemporaryFile() opens and returns a named file, SpooledTemporaryFile holds its content in memory before writing to disk, and TemporaryDirectory is a context manager that removes the directory when the context is closed.

### 6.6.1 Temporary Files

Applications that need temporary files to store data, without needing to share that file with other programs, should use the TemporaryFile() function to create the files. The function creates a file, and on platforms where it is possible, unlinks it immediately. This makes it impossible for another program to find or open the file, since there is no reference to it in the file system table. The file created by TemporaryFile() is removed automatically when it is closed, whether by calling close() or by using the context manager API and with statement.

```
# tempfile_TemporaryFile.py
import os
import tempfile

print("Building a filename with PID:")
filename = "/tmp/guess_my_name.{}.txt".format(os.getpid())
with open(filename, "w+b") as temp:
    print("temp:")
    print("  {!r}".format(temp))
    print("temp.name:")
    print("  {!r}".format(temp.name))

# Clean up the temporary file yourself.
os.remove(filename)

print()
print("TemporaryFile:")
with tempfile.TemporaryFile() as temp:
    print("temp:")
    print("  {!r}".format(temp))
    print("temp.name:")
    print("  {!r}".format(temp.name))

# Automatically cleans up the file.
```

This example illustrates the difference in creating a temporary file using a common pattern for making up a name, versus using the TemporaryFile() function. The file returned by TemporaryFile() has no name.

```
$ python3 tempfile_TemporaryFile.py
Building a filename with PID:
temp:
  <_io.BufferedRandom name='/tmp/guess_my_name.12048.txt'>
temp.name:
  '/tmp/guess_my_name.12048.txt'

TemporaryFile:
temp:
  <_io.BufferedRandom name=3>
temp.name:
  3
```

By default, the file handle is created with mode 'w+b' so it behaves consistently on all platforms and the caller can write to it and read from it.

```
# tempfile_TemporaryFile_binary.py
import os
import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b"Some data")

    temp.seek(0)
    print(temp.read())
```

After writing, the file handle must be “rewound” using seek() in order to read the data back from it.

```
$ python3 tempfile_TemporaryFile_binary.py
b'Some data'
```

To open the file in text mode, set mode to 'w+t' when the file is created.

```
# tempfile_TemporaryFile_text.py
import tempfile

with tempfile.TemporaryFile(mode="w+t") as f:
    f.writelines(["first\n", "second\n"])

    f.seek(0)
    for line in f:
        print(line.rstrip())
```

The file handle treats the data as text.

```
$ python3 tempfile_TemporaryFile_text.py
first
second
```

### 6.6.2 Named Files

There are situations where having a named temporary file is important. For applications spanning multiple processes, or even hosts, naming the file is the simplest way to pass it between parts of the application. The NamedTemporaryFile() function creates a file without unlinking it, so it retains its name (accessed with the name attribute).

```
# tempfile_NamedTemporaryFile.py
import os
import pathlib
import tempfile

with tempfile.NamedTemporaryFile() as temp:
    print("temp:")
    print("  {!r}".format(temp))
    print("temp.name:")
    print("  {!r}".format(temp.name))

    f = pathlib.Path(temp.name)

print("Exists after close:", f.exists())
```

The file is removed after the handle is closed.

```
$ python3 tempfile_NamedTemporaryFile.py
temp:
  <tempfile._TemporaryFileWrapper object at 0x7f76c878ff10>
temp.name:
  '/tmp/tmpt848ui0e'
Exists after close: False
```