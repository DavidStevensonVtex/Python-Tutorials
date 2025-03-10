# [Chapter 8: Data Compression and Archiving](https://pymotw.com/3/compression.html)

## [8.4 tarfile — Tar Archive Access](https://pymotw.com/3/tarfile/index.html)

**Purpose:**	Tar archive access.

The tarfile module provides read and write access to Unix tar archives, including compressed files. In addition to the POSIX standards, several GNU tar extensions are supported. Unix special file types such as hard and soft links, and device nodes are also handled.

Note

Although tarfile implements a Unix format, it can be used to create and read tar archives under Microsoft Windows, too.

### 8.4.1 Testing Tar Files

The is_tarfile() function returns a boolean indicating whether or not the filename passed as an argument refers to a valid tar archive.

```
# tarfile_is_tarfile.py
import tarfile

for filename in ["README.txt", "example.tar", "bad_example.tar", "notthere.tar"]:
    try:
        print("{:>15}  {}".format(filename, tarfile.is_tarfile(filename)))
    except IOError as err:
        print("{:>15}  {}".format(filename, err))
```

If the file does not exist, is_tarfile() raises an IOError.

```
$ python3 tarfile_is_tarfile.py
     README.txt  False
    example.tar  True
bad_example.tar  False
   notthere.tar  [Errno 2] No such file or directory: 'notthere.tar'
```

### 8.4.2 Reading Metadata from an Archive

Use the TarFile class to work directly with a tar archive. It supports methods for reading data about existing archives as well as modifying the archives by adding additional files.

To read the names of the files in an existing archive, use getnames().

```
# tarfile_getnames.py
import tarfile

with tarfile.open("example.tar", "r") as t:
    print(t.getnames())
```

The return value is a list of strings with the names of the archive contents.

```
$ python3 tarfile_getnames.py
['.', './tarfile_getnames.py', './tarfile.md', './tarfile_is_tarfile.py']
```

In addition to names, metadata about the archive members is available as instances of TarInfo objects.

```
# tarfile_getmembers.py
import tarfile
import time

with tarfile.open("example.tar", "r") as t:
    for member_info in t.getmembers():
        print(member_info.name)
        print("  Modified:", time.ctime(member_info.mtime))
        print("  Mode    :", oct(member_info.mode))
        print("  Type    :", member_info.type)
        print("  Size    :", member_info.size, "bytes")
        print()
```

Load the metadata via getmembers() and getmember().

```
$ python3 tarfile_getmembers.py
.
  Modified: Mon Mar 10 16:36:04 2025
  Mode    : 0o775
  Type    : b'5'
  Size    : 0 bytes

./tarfile_getnames.py
  Modified: Mon Mar 10 16:35:56 2025
  Mode    : 0o664
  Type    : b'0'
  Size    : 105 bytes

./tarfile.md
  Modified: Mon Mar 10 16:35:34 2025
  Mode    : 0o664
  Type    : b'0'
  Size    : 1600 bytes

./tarfile_is_tarfile.py
  Modified: Mon Mar 10 16:31:12 2025
  Mode    : 0o664
  Type    : b'0'
  Size    : 283 bytes
```

If the name of the archive member is known in advance, its TarInfo object can be retrieved with getmember().

```
# tarfile_getmember.py
import tarfile
import time

with tarfile.open('example.tar', 'r') as t:
    for filename in ['./tarfile.md', 'notthere.txt']:
        try:
            info = t.getmember(filename)
        except KeyError:
            print('ERROR: Did not find {} in tar archive'.format(
                filename))
        else:
            print('{} is {:d} bytes'.format(
                info.name, info.size))
```

If the archive member is not present, getmember() raises a KeyError.

```
$ python3 tarfile_getmember.py 
./tarfile.md is 1600 bytes
ERROR: Did not find notthere.txt in tar archive
```

### 8.4.3 Extracting Files from an Archive

To access the data from an archive member within a program, use the extractfile() method, passing the member’s name.

```
# tarfile_extractfile.py
import tarfile

with tarfile.open("example.tar", "r") as t:
    for filename in ["README.txt", "notthere.txt"]:
        try:
            f = t.extractfile(filename)
        except KeyError:
            print("ERROR: Did not find {} in tar archive".format(filename))
        else:
            print(filename, ":")
            print(f.read().decode("utf-8"))
```

The return value is a file-like object from which the contents of the archive member can be read.

```
$ python3 tarfile_extractfile.py

README.txt :
The examples for the tarfile module use this file and
example.tar as data.

ERROR: Did not find notthere.txt in tar archive
```

To unpack the archive and write the files to the file system, use extract() or extractall() instead.

```
# tarfile_extract.py
import tarfile
import os

os.mkdir("outdir")
with tarfile.open("example.tar", "r") as t:
    t.extract("./tarfile_is_tarfile.py", "outdir")
print(os.listdir("outdir"))
```

The member or members are read from the archive and written to the file system, starting in the directory named in the arguments.

```
$ python3 tarfile_extract.py
['tarfile_is_tarfile.py']
```

The standard library documentation includes a note stating that extractall() is safer than extract(), especially for working with streaming data where rewinding to read an earlier part of the input is not possible, and it should be used in most cases.

```
# tarfile_extractall.py
import tarfile
import os

os.mkdir("outdir")
with tarfile.open("example.tar", "r") as t:
    t.extractall("outdir")
print(os.listdir("outdir"))
```

With extractall(), the first argument is the name of the directory where the files should be written.

```
$ python3 tarfile_extractall.py
['tarfile_extract.py', 'tarfile_getnames.py', 'tarfile_getmembers.py', 'tarfile.md', 'tarfile_extractall.py', 'tarfile_is_tarfile.py', 'tarfile_getmember.py', 'tarfile_extractfile.py']
```

To extract specific files from the archive, pass their names or TarInfo metadata containers to extractall().

```
# tarfile_extractall_members.py
import tarfile
import os

os.mkdir("outdir")
with tarfile.open("example.tar", "r") as t:
    t.extractall(
        "outdir",
        members=[t.getmember("README.txt")],
    )
print(os.listdir("outdir"))
```

When a members list is provided, only the named files are extracted.

```
$ python3 tarfile_extractall_members.py

['README.txt']
```

