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