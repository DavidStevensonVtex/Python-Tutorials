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