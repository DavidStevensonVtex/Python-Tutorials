# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.7 shutil — High-level File Operations](https://pymotw.com/3/shutil/index.html)

Purpose:	High-level file operations.

The shutil module includes high-level file operations such as copying and archiving.

### 6.7.1 Copying Files

copyfile() copies the contents of the source to the destination and raises IOError if it does not have permission to write to the destination file.

```
# shutil_copyfile.py
import glob
import shutil

print("BEFORE:", glob.glob("shutil_copyfile.*"))

shutil.copyfile("shutil_copyfile.py", "shutil_copyfile.py.copy")

print("AFTER:", glob.glob("shutil_copyfile.*"))
```

Because the function opens the input file for reading, regardless of its type, special files (such as Unix device nodes) cannot be copied as new special files with copyfile().

```
$ python3 shutil_copyfile.py
BEFORE: ['shutil_copyfile.py']
AFTER: ['shutil_copyfile.py.copy', 'shutil_copyfile.py']
```

The implementation of copyfile() uses the lower-level function copyfileobj(). While the arguments to copyfile() are filenames, the arguments to copyfileobj() are open file handles. The optional third argument is a buffer length to use for reading in blocks.

```
# shutil_copyfileobj.py
import io
import os
import shutil
import sys


class VerboseStringIO(io.StringIO):

    def read(self, n=-1):
        next = io.StringIO.read(self, n)
        print("read({}) got {} bytes".format(n, len(next)))
        return next


lorem_ipsum = """Lorem ipsum dolor sit amet, consectetuer
adipiscing elit.  Vestibulum aliquam mollis dolor. Donec
vulputate nunc ut diam. Ut rutrum mi vel sem. Vestibulum
ante ipsum."""

print("Default:")
input = VerboseStringIO(lorem_ipsum)
output = io.StringIO()
shutil.copyfileobj(input, output)

print()

print("All at once:")
input = VerboseStringIO(lorem_ipsum)
output = io.StringIO()
shutil.copyfileobj(input, output, -1)

print()

print("Blocks of 256:")
input = VerboseStringIO(lorem_ipsum)
output = io.StringIO()
shutil.copyfileobj(input, output, 256)
```

The default behavior is to read using large blocks. Use -1 to read all of the input at one time or another positive integer to set a specific block size. This example uses several different block sizes to show the effect.

```
$ python3 shutil_copyfileobj.py
Default:
read(65536) got 166 bytes
read(65536) got 0 bytes

All at once:
read(-1) got 166 bytes
read(-1) got 0 bytes

Blocks of 256:
read(256) got 166 bytes
read(256) got 0 bytes
```

The copy() function interprets the output name like the Unix command line tool cp. If the named destination refers to a directory instead of a file, a new file is created in the directory using the base name of the source.

```
# shutil_copy.py
import glob
import os
import shutil

os.mkdir("example")
print("BEFORE:", glob.glob("example/*"))

shutil.copy("shutil_copy.py", "example")

print("AFTER :", glob.glob("example/*"))
```

The permissions of the file are copied along with the contents.

```
$ python3 shutil_copy.py
BEFORE: []
AFTER : ['example/shutil_copy.py']
```

copy2() works like copy(), but includes the access and modification times in the metadata copied to the new file.

```
# shutil_copy2.py
import os
import shutil
import time


def show_file_info(filename):
    stat_info = os.stat(filename)
    print("  Mode    :", oct(stat_info.st_mode))
    print("  Created :", time.ctime(stat_info.st_ctime))
    print("  Accessed:", time.ctime(stat_info.st_atime))
    print("  Modified:", time.ctime(stat_info.st_mtime))


os.mkdir("example")
print("SOURCE:")
show_file_info("shutil_copy2.py")

shutil.copy2("shutil_copy2.py", "example")

print("DEST:")
show_file_info("example/shutil_copy2.py")
```

The new file has all of the same characteristics as the old version.

```
$ python3 shutil_copy2.py
SOURCE:
  Mode    : 0o100664
  Created : Mon Feb 24 14:13:49 2025
  Accessed: Mon Feb 24 14:13:49 2025
  Modified: Mon Feb 24 14:13:49 2025
DEST:
  Mode    : 0o100664
  Created : Mon Feb 24 14:15:25 2025
  Accessed: Mon Feb 24 14:13:49 2025
  Modified: Mon Feb 24 14:13:49 2025
```

### 6.7.2 Copying File Metadata

By default when a new file is created under Unix, it receives permissions based on the umask of the current user. To copy the permissions from one file to another, use copymode().

```
# shutil_copymode.py
import os
import shutil
import subprocess

with open("file_to_change.txt", "wt") as f:
    f.write("content")
os.chmod("file_to_change.txt", 0o444)

print("BEFORE:", oct(os.stat("file_to_change.txt").st_mode))

shutil.copymode("shutil_copymode.py", "file_to_change.txt")

print("AFTER :", oct(os.stat("file_to_change.txt").st_mode))
```

This example script creates a file to be modified, then uses copymode() to duplicate the permissions of the script to the example file.

```
$ python3 shutil_copymode.py
BEFORE: 0o100444
AFTER : 0o100664
```

To copy other metadata about the file use copystat().

```
# shutil_copystat.py
import os
import shutil
import time


def show_file_info(filename):
    stat_info = os.stat(filename)
    print("  Mode    :", oct(stat_info.st_mode))
    print("  Created :", time.ctime(stat_info.st_ctime))
    print("  Accessed:", time.ctime(stat_info.st_atime))
    print("  Modified:", time.ctime(stat_info.st_mtime))


with open("file_to_change.txt", "wt") as f:
    f.write("content")
os.chmod("file_to_change.txt", 0o444)

print("BEFORE:")
show_file_info("file_to_change.txt")

shutil.copystat("shutil_copystat.py", "file_to_change.txt")

print("AFTER:")
show_file_info("file_to_change.txt")
```

Only the permissions and dates associated with the file are duplicated with copystat().

```
$ python3 shutil_copystat.py
BEFORE:
  Mode    : 0o100444
  Created : Mon Feb 24 14:21:48 2025
  Accessed: Mon Feb 24 14:21:48 2025
  Modified: Mon Feb 24 14:21:48 2025
AFTER:
  Mode    : 0o100664
  Created : Mon Feb 24 14:21:48 2025
  Accessed: Mon Feb 24 14:20:22 2025
  Modified: Mon Feb 24 14:20:22 2025
```