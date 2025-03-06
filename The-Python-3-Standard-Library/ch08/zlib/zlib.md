# [Chapter 8: Data Compression and Archiving](https://pymotw.com/3/compression.html)

## [8.1 zlib — GNU zlib Compression](https://pymotw.com/3/zlib/index.html)

**Purpose:**	Low-level access to GNU zlib compression library

The zlib module provides a lower-level interface to many of the functions in the zlib compression library from the GNU project.

### 8.1.1 Working with Data in Memory

The simplest way to work with zlib requires holding all of the data to be compressed or decompressed in memory.

```
# zlib_memory.py
import zlib
import binascii

original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)

compressed = zlib.compress(original_data)
print('Compressed   :', len(compressed),
      binascii.hexlify(compressed))

decompressed = zlib.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)
```

The compress() and decompress() functions both take a byte sequence argument and return a byte sequence.

```
$ python3 zlib_memory.py
Original     : 26 b'This is the original text.'
Compressed   : 32 b'789c0bc9c82c5600a2928c5485fca2ccf4ccbcc41c8592d48a123d007f2f097e'
Decompressed : 26 b'This is the original text.'
```

The previous example demonstrates that the compressed version of small amounts of data can be larger than the uncompressed version. While the actual results depend on the input data, it is interesting to observe the compression overhead for small data sets

```
# zlib_lengths.py
import zlib

original_data = b'This is the original text.'

template = '{:>15}  {:>15}'
print(template.format('len(data)', 'len(compressed)'))
print(template.format('-' * 15, '-' * 15))

for i in range(5):
    data = original_data * i
    compressed = zlib.compress(data)
    highlight = '*' if len(data) < len(compressed) else ''
    print(template.format(len(data), len(compressed)), highlight)
```

The \* in the output highlight the lines where the compressed data takes up more memory than the uncompressed version.

```
$ python3 zlib_lengths.py
      len(data)  len(compressed)
---------------  ---------------
              0                8 *
             26               32 *
             52               35 
             78               35 
            104               36 
```

zlib supports several different compression levels, allowing a balance between computational cost and the amount of space reduction. The default compression level, zlib.Z_DEFAULT_COMPRESSION is -1 and corresponds to a hard-coded value that compromises between performance and compression outcome. This currently corresponds to level 6.

```
# zlib_compresslevel.py
import zlib

input_data = b'Some repeated text.\n' * 1024
template = '{:>5}  {:>5}'

print(template.format('Level', 'Size'))
print(template.format('-----', '----'))

for i in range(0, 10):
    data = zlib.compress(input_data, i)
    print(template.format(i, len(data)))
```

A level of 0 means no compression at all. A level of 9 requires the most computation and produces the smallest output. As this example shows, the same size reduction may be achieved with multiple compression levels for a given input.

```
$ python3 zlib_compresslevel.py
Level   Size
-----   ----
    0  20491
    1    172
    2    172
    3    172
    4     98
    5     98
    6     98
    7     98
    8     98
    9     98
```