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

### 8.3.2 Incremental Compression and Decompression

The in-memory approach has obvious drawbacks that make it impractical for real-world use cases. The alternative is to use BZ2Compressor and BZ2Decompressor objects to manipulate data incrementally so that the entire data set does not have to fit into memory.

```
# bz2_incremental.py
import bz2
import binascii
import io

compressor = bz2.BZ2Compressor()

with open("lorem.txt", "rb") as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print("Compressed: {}".format(binascii.hexlify(compressed)))
        else:
            print("buffering...")
    remaining = compressor.flush()
    print("Flushed: {}".format(binascii.hexlify(remaining)))

```

This example reads small blocks of data from a plain-text file and passes it to compress(). The compressor maintains an internal buffer of compressed data. Since the compression algorithm depends on checksums and minimum block sizes, the compressor may not be ready to return data each time it receives more input. If it does not have an entire compressed block ready, it returns an empty string. When all of the data is fed in, the flush() method forces the compressor to close the final block and return the rest of the compressed data.

```
$ python3 bz2_incremental.py
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
buffering...
Flushed: b'425a6839314159265359cb07c9da000042d7800010400524074b003ff7ff004001d2e34183423129ed53d353ca34068341aa78d26446a34d0068c818d311846980000129910453d3265234f53689ea0cddf6e3ccaee7a400028dce03aac30d417615abf883428245302e5e197e9047c4c836ad3262ab674a0a16613eee561f2db16ad21a50bad29ca48a9a258422e72793045c04ae97373c3041eec9137bacc2b5cff449ccf7ed21a69a973c514573633d4854be0bdcc60dd19c0cca77ab4d82bdb3a5e123daf22d99e7304eec48f26d5dffa66ea8d7bb362ff02f59db1ce87ec35b9ca9b9639a8dfa78457bc1c355d9d33ced467ed7e164938b33be5119e31a157ab875d16e8b629208b83364cdf5f51b6dc6988d96a6ef53182475eee579cf5886d433e46615539331874a1d9c28b2a892eed426892ad4d0523bf5db9fae8a8dd7c69f76a8d3ad4785c1984849525b706ea197f0c929bf1cc6c5152dc4ceb7d6e8a2edc0a869eaa59fa3118b0c4ac497a18225f6b3a295a5bf53848a8a986642b44702d2a3429c8855e81e68a0c8df715b7990081a7aead4fc2231c62ed5829b19746315a6c3786c1203ee9fc5dc914e142432c1f27680'
```