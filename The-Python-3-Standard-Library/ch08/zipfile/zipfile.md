# [Chapter 8: Data Compression and Archiving](https://pymotw.com/3/compression.html)

## [8.5 zipfile — ZIP Archive Access](https://pymotw.com/3/zipfile/index.html)

**Purpose:**	Read and write ZIP archive files.

The zipfile module can be used to manipulate ZIP archive files, the format popularized by the PC program PKZIP.

### 8.5.1 Testing ZIP Files

The is_zipfile() function returns a boolean indicating whether or not the filename passed as an argument refers to a valid ZIP archive.

`$ zip -r example.zip .`

```
# zipfile_is_zipfile.py
import zipfile

for filename in ["README.txt", "example.zip", "bad_example.zip", "notthere.zip"]:
    print("{:>15}  {}".format(filename, zipfile.is_zipfile(filename)))
```

If the file does not exist at all, is_zipfile() returns False.

```
$ python3 zipfile_is_zipfile.py
     README.txt  False
    example.zip  True
bad_example.zip  False
   notthere.zip  False
```

### 8.5.2 Reading Metadata from an Archive

Use the ZipFile class to work directly with a ZIP archive. It supports methods for reading data about existing archives as well as modifying the archives by adding additional files.

```
# zipfile_namelist.py
import zipfile

with zipfile.ZipFile("example.zip", "r") as zf:
    print(zf.namelist())
```

The namelist() method returns the names of the files in an existing archive.

```
$ python3 zipfile_namelist.py
['zipfile.md', 'bad_example.zip', 'README.txt', 'zipfile_is_zipfile.py']
```

The list of names is only part of the information available from the archive, though. To access all of the metadata about the ZIP contents, use the infolist() or getinfo() methods.

```
# zipfile_infolist.py
import datetime
import zipfile


def print_info(archive_name):
    with zipfile.ZipFile(archive_name) as zf:
        for info in zf.infolist():
            print(info.filename)
            print("  Comment     :", info.comment)
            mod_date = datetime.datetime(*info.date_time)
            print("  Modified    :", mod_date)
            if info.create_system == 0:
                system = "Windows"
            elif info.create_system == 3:
                system = "Unix"
            else:
                system = "UNKNOWN"
            print("  System      :", system)
            print("  ZIP version :", info.create_version)
            print("  Compressed  :", info.compress_size, "bytes")
            print("  Uncompressed:", info.file_size, "bytes")
            print()


if __name__ == "__main__":
    print_info("example.zip")
```

There are additional fields other than those printed here, but deciphering the values into anything useful requires careful reading of the PKZIP Application Note with the ZIP file specification.

```
$ python3 zipfile_infolist.py
zipfile.md
  Comment     : b''
  Modified    : 2025-03-11 10:47:38
  System      : Unix
  ZIP version : 30
  Compressed  : 410 bytes
  Uncompressed: 695 bytes

bad_example.zip
  Comment     : b''
  Modified    : 2025-03-11 10:48:36
  System      : Unix
  ZIP version : 30
  Compressed  : 45 bytes
  Uncompressed: 45 bytes

README.txt
  Comment     : b''
  Modified    : 2025-03-11 10:47:56
  System      : Unix
  ZIP version : 30
  Compressed  : 12 bytes
  Uncompressed: 12 bytes

zipfile_is_zipfile.py
  Comment     : b''
  Modified    : 2025-03-11 10:47:28
  System      : Unix
  ZIP version : 30
  Compressed  : 131 bytes
  Uncompressed: 193 bytes
```

If the name of the archive member is known in advance, its ZipInfo object can be retrieved directly with getinfo().

```
# zipfile_getinfo.py
import zipfile

with zipfile.ZipFile("example.zip") as zf:
    for filename in ["README.txt", "notthere.txt"]:
        try:
            info = zf.getinfo(filename)
        except KeyError:
            print("ERROR: Did not find {} in zip file".format(filename))
        else:
            print("{} is {} bytes".format(info.filename, info.file_size))
```

If the archive member is not present, getinfo() raises a KeyError.

```
$ python3 zipfile_getinfo.py
README.txt is 12 bytes
ERROR: Did not find notthere.txt in zip file
```

### 8.5.3 Extracting Archived Files From an Archive

To access the data from an archive member, use the read() method, passing the member’s name.

```
# zipfile_read.py
import zipfile

with zipfile.ZipFile("example.zip") as zf:
    for filename in ["README.txt", "notthere.txt"]:
        try:
            data = zf.read(filename)
        except KeyError:
            print("ERROR: Did not find {} in zip file".format(filename))
        else:
            print(filename, ":")
            print(data)
        print()
```

The data is automatically decompressed, if necessary.

```
$ python3 zipfile_read.py
README.txt :
b'Hello world\n'

ERROR: Did not find notthere.txt in zip file
```

### 8.5.4 Creating New Archives

To create a new archive, instantiate the ZipFile with a mode of 'w'. Any existing file is truncated and a new archive is started. To add files, use the write() method.

```
# zipfile_write.py
from zipfile_infolist import print_info
import zipfile

print("creating archive")
with zipfile.ZipFile("write.zip", mode="w") as zf:
    print("adding README.txt")
    zf.write("README.txt")

print()
print_info("write.zip")
```

```
$ python3 zipfile_write.py
creating archive
adding README.txt

README.txt
  Comment     : b''
  Modified    : 2025-03-11 10:47:54
  System      : Unix
  ZIP version : 20
  Compressed  : 12 bytes
  Uncompressed: 12 bytes
```

To add compression, the zlib module is required. If zlib is available, the compression mode for individual files or for the archive as a whole can be set using zipfile.ZIP_DEFLATED. The default compression mode is zipfile.ZIP_STORED, which adds the input data to the archive without compressing it.

```
# zipfile_write_compression.py
from zipfile_infolist import print_info
import zipfile

try:
    import zlib

    compression = zipfile.ZIP_DEFLATED
except (ImportError, AttributeError):
    compression = zipfile.ZIP_STORED

modes = {
    zipfile.ZIP_DEFLATED: "deflated",
    zipfile.ZIP_STORED: "stored",
}

print("creating archive")
with zipfile.ZipFile("write_compression.zip", mode="w") as zf:
    mode_name = modes[compression]
    print("adding README.txt with compression mode", mode_name)
    zf.write("README.txt", compress_type=compression)

print()
print_info("write_compression.zip")
```

This time, the archive member is compressed.

```
$ python3 zipfile_write_compression.py
creating archive
adding README.txt with compression mode deflated

README.txt
  Comment     : b''
  Modified    : 2025-03-11 11:27:44
  System      : Unix
  ZIP version : 20
  Compressed  : 399 bytes
  Uncompressed: 736 bytes
```