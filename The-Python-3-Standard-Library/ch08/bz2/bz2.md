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

### 8.3.3 Mixed Content Streams

BZ2Decompressor can also be used in situations where compressed and uncompressed data is mixed together.

```
# bz2_mixed.py
import bz2

lorem = open("lorem.txt", "rt").read().encode("utf-8")
compressed = bz2.compress(lorem)
combined = compressed + lorem

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(combined)

decompressed_matches = decompressed == lorem
print("Decompressed matches lorem:", decompressed_matches)

unused_matches = decompressor.unused_data == lorem
print("Unused data matches lorem :", unused_matches)
```

After decompressing all of the data, the unused_data attribute contains any data not used.

```
$ python3 bz2_mixed.py
Decompressed matches lorem: True
Unused data matches lorem : True
```

### 8.3.4 Writing Compressed Files

BZ2File can be used to write to and read from bzip2-compressed files using the usual methods for writing and reading data.

```
# bz2_file_write.py
import bz2
import io
import os

data = "Contents of the example file go here.\n"

with bz2.BZ2File("example.bz2", "wb") as output:
    with io.TextIOWrapper(output, encoding="utf-8") as enc:
        enc.write(data)

os.system("file example.bz2")
```

To write data into a compressed file, open the file with mode 'wb'. This example wraps the BZ2File with a TextIOWrapper from the io module to encode Unicode text to bytes suitable for compression.

```
$ python3 bz2_file_write.py
example.bz2: bzip2 compressed data, block size = 900k
```

Different compression levels can be used by passing a compresslevel argument. Valid values range from 1 to 9, inclusive. Lower values are faster and result in less compression. Higher values are slower and compress more, up to a point.

```
# bz2_file_compresslevel.py
import bz2
import io
import os

data = open("lorem.txt", "r", encoding="utf-8").read() * 1024
print("Input contains {} bytes".format(len(data.encode("utf-8"))))

for i in range(1, 10):
    filename = "compress-level-{}.bz2".format(i)
    with bz2.BZ2File(filename, "wb", compresslevel=i) as output:
        with io.TextIOWrapper(output, encoding="utf-8") as enc:
            enc.write(data)
    os.system("cksum {}".format(filename))
```

The center column of numbers in the output of the script is the size in bytes of the files produced. For this input data, the higher compression values do not always pay off in decreased storage space for the same input data. Results will vary for other inputs.

```
$ python3 bz2_file_compresslevel.py
Input contains 753664 bytes
624984808 8497 compress-level-1.bz2
2810842557 4688 compress-level-2.bz2
1257664293 3726 compress-level-3.bz2
2864333220 2594 compress-level-4.bz2
2583238201 2653 compress-level-5.bz2
934209552 2512 compress-level-6.bz2
632595249 2306 compress-level-7.bz2
612410620 1127 compress-level-8.bz2
1817446238 1127 compress-level-9.bz2
```

A BZ2File instance also includes a writelines() method that can be used to write a sequence of strings.

```
# bz2_file_writelines.py
import bz2
import io
import itertools
import os

data = "The same line, over and over.\n"

with bz2.BZ2File("lines.bz2", "wb") as output:
    with io.TextIOWrapper(output, encoding="utf-8") as enc:
        enc.writelines(itertools.repeat(data, 10))

os.system("bzcat lines.bz2")
```

The lines should end in a newline character, as when writing to a regular file.

```
$ python3 bz2_file_writelines.py
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

### 8.3.5 Reading Compressed Files

To read data back from previously compressed files, open the file with read mode ('rb'). The value returned from read() will be a byte string.

```
# bz2_file_read.py
import bz2
import io

with bz2.BZ2File("example.bz2", "rb") as input:
    with io.TextIOWrapper(input, encoding="utf-8") as dec:
        print(dec.read())
```

This example reads the file written by bz2_file_write.py from the previous section. The BZ2File is wrapped with a TextIOWrapper to decode bytes read to Unicode text.

```
$ python3 bz2_file_read.py
Contents of the example file go here.

```

While reading a file, it is also possible to seek, and to read only part of the data.

```
# bz2_file_seek.py
import bz2
import contextlib

with bz2.BZ2File("example.bz2", "rb") as input:
    print("Entire file:")
    all_data = input.read()
    print(all_data)

    expected = all_data[5:15]

    # rewind to beginning
    input.seek(0)

    # move ahead 5 bytes
    input.seek(5)
    print("Starting at position 5 for 10 bytes:")
    partial = input.read(10)
    print(partial)

    print()
    print(expected == partial)
```

The seek() position is relative to the uncompressed data, so the caller does not need to be aware that the data file is compressed. This allows a BZ2File instance to be passed to a function expecting a regular uncompressed file.

```
$ python3 bz2_file_seek.py
Entire file:
b'Contents of the example file go here.\n'
Starting at position 5 for 10 bytes:
b'nts of the'

True
```

### 8.3.6 Reading and Writing Unicode Data

The previous examples used BZ2File directly and managed the encoding and decoding of Unicode text strings inline with an io.TextIOWrapper, where necessary. These extra steps can be avoided by using bz2.open(), which sets up an io.TextIOWrapper to handle the encoding or decoding automatically.

```
# bz2_unicode.py
import bz2
import os

data = "Character with an åccent."

with bz2.open("example.bz2", "wt", encoding="utf-8") as output:
    output.write(data)

with bz2.open("example.bz2", "rt", encoding="utf-8") as input:
    print("Full file: {}".format(input.read()))

# Move to the beginning of the accented character.
with bz2.open("example.bz2", "rt", encoding="utf-8") as input:
    input.seek(18)
    print("One character: {}".format(input.read(1)))

# Move to the middle of the accented character.
with bz2.open("example.bz2", "rt", encoding="utf-8") as input:
    input.seek(19)
    try:
        print(input.read(1))
    except UnicodeDecodeError:
        print("ERROR: failed to decode")
```

The file handle returned by open() supports seek(), but use care because the file pointer moves by bytes not characters and may end up in the middle of an encoded character.

```
$ python3 bz2_unicode.py
Full file: Character with an åccent.
One character: å
ERROR: failed to decode
```