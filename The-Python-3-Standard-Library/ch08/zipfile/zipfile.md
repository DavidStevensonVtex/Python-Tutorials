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

