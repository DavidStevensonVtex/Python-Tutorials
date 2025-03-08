# [Chapter 8: Data Compression and Archiving](https://pymotw.com/3/compression.html)

## [8.3 bz2 — bzip2 Compression](https://pymotw.com/3/bz2/index.html)

**Purpose:**	bzip2 compression

The bz2 module is an interface for the bzip2 library, used to compress data for storage or transmission. There are three APIs provided:

* “one shot” compression/decompression functions for operating on a blob of data
* iterative compression/decompression objects for working with streams of data
* a file-like class that supports reading and writing as with an uncompressed file

### 8.3.1 One-shot Operations in Memory

The simplest way to work with bz2 is to load all of the data to be compressed or decompressed in memory, and then use compress() and decompress() to transform it.

```
# bz2_memory.py
import bz2
import binascii

original_data = b"This is the original text."
print("Original     : {} bytes".format(len(original_data)))
print(original_data)

print()
compressed = bz2.compress(original_data)
print("Compressed   : {} bytes".format(len(compressed)))
hex_version = binascii.hexlify(compressed)
for i in range(len(hex_version) // 40 + 1):
    print(hex_version[i * 40 : (i + 1) * 40])

print()
decompressed = bz2.decompress(compressed)
print("Decompressed : {} bytes".format(len(decompressed)))
print(decompressed)
```

The compressed data contains non-ASCII characters, so it needs to be converted to its hexadecimal representation before it can be printed. In the output from these examples, the hexadecimal version is reformatted to have at most 40 characters on each line.

```
$ python3 bz2_memory.py
Original     : 26 bytes
b'This is the original text.'

Compressed   : 62 bytes
b'425a683931415926535916be35a6000002938040'
b'01040022e59c402000314c000111e93d434da223'
b'028cf9e73148cae0a0d6ed7f17724538509016be'
b'35a6'

Decompressed : 26 bytes
b'This is the original text.'
```

For short text, the compressed version can be significantly longer than the original. While the actual results depend on the input data, it is interesting to observe the compression overhead.

```
# bz2_lengths.py
import bz2

original_data = b"This is the original text."

fmt = "{:>15}  {:>15}"
print(fmt.format("len(data)", "len(compressed)"))
print(fmt.format("-" * 15, "-" * 15))

for i in range(5):
    data = original_data * i
    compressed = bz2.compress(data)
    print(fmt.format(len(data), len(compressed)), end="")
    print("*" if len(data) < len(compressed) else "")
```

The output lines ending with * show the points where the compressed data is longer than the raw input.

```
$ python3 bz2_lengths.py
      len(data)  len(compressed)
---------------  ---------------
              0               14*
             26               62*
             52               68*
             78               70
            104               72
```