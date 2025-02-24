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

### 6.7.3 Working With Directory Trees

shutil includes three functions for working with directory trees. To copy a directory from one place to another, use copytree(). It recurses through the source directory tree, copying files to the destination. The destination directory must not exist in advance.

```
# shutil_copytree.py
import glob
import pprint
import shutil

print("BEFORE:")
pprint.pprint(glob.glob("/tmp/example/*"))

shutil.copytree("../shutil", "/tmp/example")

print("\nAFTER:")
pprint.pprint(glob.glob("/tmp/example/*"))
```

The symlinks argument controls whether symbolic links are copied as links or as files. The default is to copy the contents to new files. If the option is true, new symlinks are created within the destination tree.

```
$ python3 shutil_copytree.py
BEFORE:
[]

AFTER:
['/tmp/example/shutil_copy2.py',
 '/tmp/example/shutil_copyfile.py.copy',
 '/tmp/example/shutil_copystat.py',
 '/tmp/example/shutil_copyfile.py',
 '/tmp/example/file_to_change.txt',
 '/tmp/example/shutil_copytree.py',
 '/tmp/example/shutil_copy.py',
 '/tmp/example/shutil_copyfileobj.py',
 '/tmp/example/shutil_copymode.py',
 '/tmp/example/shutil.md']
```

copytree() accepts two callable arguments to control its behavior. The ignore argument is called with the name of each directory or subdirectory being copied along with a list of the contents of the directory. It should return a list of items that should be copied. The copy_function argument is called to actually copy the file.

```
# shutil_copytree_verbose.py
import glob
import pprint
import shutil


def verbose_copy(src, dst):
    print("copying\n {!r}\n to {!r}".format(src, dst))
    return shutil.copy2(src, dst)


print("BEFORE:")
pprint.pprint(glob.glob("/tmp/example/*"))
print()

shutil.copytree(
    "../shutil",
    "/tmp/example",
    copy_function=verbose_copy,
    ignore=shutil.ignore_patterns("*.py"),
)

print("\nAFTER:")
pprint.pprint(glob.glob("/tmp/example/*"))
```

In the example, ignore_patterns() is used to create an ignore function to skip copying Python source files. verbose_copy() prints the names of files as they are copied then uses copy2(), the default copy function, to make the copies.

```
$ python3 shutil_copytree_verbose.py
BEFORE:
[]

copying
 '../shutil/shutil_copyfile.py.copy'
 to '/tmp/example/shutil_copyfile.py.copy'
copying
 '../shutil/file_to_change.txt'
 to '/tmp/example/file_to_change.txt'
copying
 '../shutil/shutil.md'
 to '/tmp/example/shutil.md'

AFTER:
['/tmp/example/shutil_copyfile.py.copy',
 '/tmp/example/file_to_change.txt',
 '/tmp/example/shutil.md']
```

To remove a directory and its contents, use rmtree().

```
# shutil_rmtree.py
import glob
import pprint
import shutil

print("BEFORE:")
pprint.pprint(glob.glob("/tmp/example/*"))

shutil.rmtree("/tmp/example")

print("\nAFTER:")
pprint.pprint(glob.glob("/tmp/example/*"))
```

Errors are raised as exceptions by default, but can be ignored if the second argument is true, and a special error handler function can be provided in the third argument.

```
$ python3 shutil_rmtree.py
BEFORE:
['/tmp/example/shutil_copyfile.py.copy',
 '/tmp/example/file_to_change.txt',
 '/tmp/example/shutil.md']

AFTER:
[]
```

To move a file or directory from one place to another, use move().

```
# shutil_move.py
import glob
import shutil

with open("example.txt", "wt") as f:
    f.write("contents")

print("BEFORE: ", glob.glob("example*"))

shutil.move("example.txt", "example.out")

print("AFTER : ", glob.glob("example*"))
```

The semantics are similar to those of the Unix command mv. If the source and destination are within the same file system, the source is renamed. Otherwise the source is copied to the destination and then the source is removed.

```
$ python3 shutil_move.py
BEFORE:  ['example.txt']
AFTER :  ['example.out']
```