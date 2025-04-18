# [Chapter 8: Data Compression and Archiving](https://pymotw.com/3/compression.html)

## [8.2 gzip — Read and Write GNU zip Files](https://pymotw.com/3/gzip/index.html)

**Purpose:**	Read and write gzip files.

The gzip module provides a file-like interface to GNU zip files, using zlib to compress and uncompress the data.

### 8.2.1 Writing Compressed Files

The module-level function open() creates an instance of the file-like class GzipFile. The usual methods for writing and reading bytes are provided.

```
# gzip_write.py
import gzip
import io
import os

outfilename = 'example.txt.gz'
with gzip.open(outfilename, 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write('Contents of the example file go here.\n')

print(outfilename, 'contains', os.stat(outfilename).st_size,
      'bytes')
os.system('file -b --mime {}'.format(outfilename))
```

To write data into a compressed file, open the file with mode 'wb'. This example wraps the GzipFile with a TextIOWrapper from the io module to encode Unicode text to bytes suitable for compression.

```
$ python3 gzip_write.py
example.txt.gz contains 75 bytes
application/gzip; charset=binary
```

Different amounts of compression can be used by passing a compresslevel argument. Valid values range from 0 to 9, inclusive. Lower values are faster and result in less compression. Higher values are slower and compress more, up to a point.

```
# gzip_compresslevel.py
import gzip
import io
import os
import hashlib


def get_hash(data):
    return hashlib.md5(data).hexdigest()


data = open('lorem.txt', 'r').read() * 1024
cksum = get_hash(data.encode('utf-8'))


print('Level  Size        Checksum')
print('-----  ----------  ---------------------------------')
print('data   {:>10}  {}'.format(len(data), cksum))

for i in range(0, 10):
    filename = 'compress-level-{}.gz'.format(i)
    with gzip.open(filename, 'wb', compresslevel=i) as output:
        with io.TextIOWrapper(output, encoding='utf-8') as enc:
            enc.write(data)
    size = os.stat(filename).st_size
    cksum = get_hash(open(filename, 'rb').read())
    print('{:>5d}  {:>10d}  {}'.format(i, size, cksum))
```

The center column of numbers in the output shows the size in bytes of the files produced by compressing the input. For this input data, the higher compression values do not necessarily pay off in decreased storage space. Results will vary, depending on the input data.

```
$ python3 gzip_compresslevel.py
Level  Size        Checksum
-----  ----------  ---------------------------------
data       753664  cf2b5077d6af0b580f0b90f01ecf4c0f
    0      753769  1c18cfe5fafee5ec7e9a7873d4effe04
    1       10420  80ec81d849bdcf924e737893cc05e064
    2        7921  0e82ee867551f5f2937c5c06d16c5591
    3        7688  e32092e7580f500ca744da856fb9e37d
    4        4162  503e4d271476ee7bfb531935a0f297b9
    5        4162  611384a5285a51add3649f0bb4e9f76e
    6        4162  54eb68195faaa64ef47e9746c1c0844f
    7        4162  3f4b8b15e06d97a748284d857d9ae840
    8        4162  89629f72f6ce62398cf34d00d35e08eb
    9        4162  bd796b4d63f9f00c91ece94e58ab9be9
```

A GzipFile instance also includes a writelines() method that can be used to write a sequence of strings.

```
# gzip_writelines.py
import gzip
import io
import itertools
import os

with gzip.open('example_lines.txt.gz', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.writelines(
            itertools.repeat('The same line, over and over.\n',
                             10)
        )

os.system('zcat example_lines.txt.gz')
```

As with a regular file, the input lines need to include a newline character.

```
$ python3 gzip_writelines.py
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
The same line, over and over.
```

### 8.2.2 Reading Compressed Data

To read data back from previously compressed files, open the file with binary read mode ('rb') so no text-based translation of line endings or Unicode decoding is performed.

```
# gzip_read.py
import gzip
import io

with gzip.open('example.txt.gz', 'rb') as input_file:
    with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
        print(dec.read())
```

This example reads the file written by gzip_write.py from the previous section, using a TextIOWrapper to decode the text after it is decompressed.

```
$ python3 gzip_read.py
Contents of the example file go here.

```

While reading a file, it is also possible to seek and read only part of the data.

```
# gzip_seek.py
import gzip

with gzip.open('example.txt.gz', 'rb') as input_file:
    print('Entire file:')
    all_data = input_file.read()
    print(all_data)

    expected = all_data[5:15]

    # rewind to beginning
    input_file.seek(0)

    # move ahead 5 bytes
    input_file.seek(5)
    print('Starting at position 5 for 10 bytes:')
    partial = input_file.read(10)
    print(partial)

    print()
    print(expected == partial)
```

The seek() position is relative to the uncompressed data, so the caller does not need to know that the data file is compressed.

```
$ python3 gzip_seek.py
Entire file:
b'Contents of the example file go here.\n'
Starting at position 5 for 10 bytes:
b'nts of the'

True
```

### 8.2.3 Working with Streams

The GzipFile class can be used to wrap other types of data streams so they can use compression as well. This is useful when the data is being transmitted over a socket or an existing (already open) file handle. A BytesIO buffer can also be used.

```
# gzip_BytesIO.py
import gzip
from io import BytesIO
import binascii

uncompressed_data = b"The same line, over and over.\n" * 10
print("UNCOMPRESSED:", len(uncompressed_data))
print(uncompressed_data)

buf = BytesIO()
with gzip.GzipFile(mode="wb", fileobj=buf) as f:
    f.write(uncompressed_data)

compressed_data = buf.getvalue()
print("COMPRESSED:", len(compressed_data))
print(binascii.hexlify(compressed_data))

inbuffer = BytesIO(compressed_data)
with gzip.GzipFile(mode="rb", fileobj=inbuffer) as f:
    reread_data = f.read(len(uncompressed_data))

print("\nREREAD:", len(reread_data))
print(reread_data)
```

One benefit of using GzipFile over [zlib](https://pymotw.com/3/zlib/index.html) is that it supports the file API. However, when re-reading the previously compressed data, an explicit length is passed to read(). Leaving the length off resulted in a CRC error, possibly because BytesIO returned an empty string before reporting EOF. When working with streams of compressed data, either prefix the data with an integer representing the actual amount of data to be read or use the incremental decompression API in [zlib](https://pymotw.com/3/zlib/index.html).

```
$ python3 gzip_BytesIO.py
UNCOMPRESSED: 300
b'The same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\n'
COMPRESSED: 51
b'1f8b08002e3bcb6702ff0bc94855284ecc4d55c8c9cc4bd551c82f4b2d5248cc4b0133f4b8424665916401d3e717802c010000'

REREAD: 300
b'The same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\nThe same line, over and over.\n'
```

### See also

* [Standard library documentation for gzip](https://docs.python.org/3/library/gzip.html)
* [zlib](https://pymotw.com/3/zlib/index.html) – The zlib module is a lower-level interface to gzip compression.
* [zipfile](https://pymotw.com/3/zipfile/index.html) – The zipfile module gives access to ZIP archives.
* [bz2](https://pymotw.com/3/bz2/index.html) – The bz2 module uses the bzip2 compression format.
* [tarfile](https://pymotw.com/3/tarfile/index.html) – The tarfile module includes built-in support for reading compressed tar archives.
* [io](https://pymotw.com/3/io/index.html) – Building-blocks for creating input and output pipelines.