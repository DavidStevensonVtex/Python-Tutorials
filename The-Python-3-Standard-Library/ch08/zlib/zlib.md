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

### 8.1.2 Incremental Compression and Decompression

The in-memory approach has drawbacks that make it impractical for real-world use cases, primarily that the system needs enough memory to hold both the uncompressed and compressed versions resident in memory at the same time. The alternative is to use Compress and Decompress objects to manipulate data incrementally, so that the entire data set does not have to fit into memory.

```
# zlib_incremental.py
import zlib
import binascii

compressor = zlib.compressobj(1)

with open('lorem.txt', 'rb') as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print('Compressed: {}'.format(
                binascii.hexlify(compressed)))
        else:
            print('buffering...')
    remaining = compressor.flush()
    print('Flushed: {}'.format(binascii.hexlify(remaining)))
```

This example reads small blocks of data from a plain text file and passes it to compress(). The compressor maintains an internal buffer of compressed data. Since the compression algorithm depends on checksums and minimum block sizes, the compressor may not be ready to return data each time it receives more input. If it does not have an entire compressed block ready, it returns an empty byte string. When all of the data is fed in, the flush() method forces the compressor to close the final block and return the rest of the compressed data.

```
$ python3 zlib_incremental.py
Compressed: b'7801'
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
Flushed: b'55525b8edb300cfcf7297800c37728b09f6d51a068ff1999c9b2a024af48fafc3bea669b06300c8b1687f3e0d73ea4921e9e95f66e7d906b105789954a6f2e25245206f1ae877ad17623318d6d79e94d0ac94d3cd85792a695249e9bd28c6be9e390b192012b9d4c6f694c236360a6495f1706a4546981c204a7e8030f49d25b72dde825d529b415ddb3053575a504cd16b2d1f73965b97251437da39fb2530cf5d0b71492d17d02995ef0b9d10f31c324f1f9f3145b7894dce8b79e5cc1eec881771f4557522e0948e2b29227b41fa0f6b0e7483bb5f1a4b92e86bb0ef4c1e280a7030519fc4f8a831468dba4db0a5d8cdb0eb45d19923f3c5cf604fb277eaf7cd1804aaa7d5cf43f5598f1e1261c6f08081263a96ce2c93bd315014ede143990dae7848dbe184cc1c8534f1903170702d5e91f82b85b4957c99b823ae76d1a68a25769a03f7d7e38553961f2e30c8560306ba40d5a2faf0f13ee0a914dfa012c75173a7ac02948fef6b70bcdeec0ff15936ecc6ce62666999b705f884fdbbc9b69d1c85ddb13e8a215bbb62bfaffa447dfde015cf60e9b'
```

### 8.1.3 Mixed Content Streams

The Decompress class returned by decompressobj() can also be used in situations where compressed and uncompressed data is mixed together.

```
# zlib_mixed.py
import zlib

lorem = open('lorem.txt', 'rb').read()
compressed = zlib.compress(lorem)
combined = compressed + lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)

decompressed_matches = decompressed == lorem
print('Decompressed matches lorem:', decompressed_matches)

unused_matches = decompressor.unused_data == lorem
print('Unused data matches lorem :', unused_matches)
```

After decompressing all of the data, the unused_data attribute contains any data not used.

```
$ python3 zlib_mixed.py
Decompressed matches lorem: True
Unused data matches lorem : True
```

### 8.1.4 Checksums

In addition to compression and decompression functions, zlib includes two functions for computing checksums of data, adler32() and crc32(). Neither checksum is cryptographically secure, and they are only intended for use for data integrity verification.

```
# zlib_checksums.py
import zlib

data = open('lorem.txt', 'rb').read()

cksum = zlib.adler32(data)
print('Adler32: {:12d}'.format(cksum))
print('       : {:12d}'.format(zlib.adler32(data, cksum)))

cksum = zlib.crc32(data)
print('CRC-32 : {:12d}'.format(cksum))
print('       : {:12d}'.format(zlib.crc32(data, cksum)))
```

Both functions take the same arguments, a byte string containing the data and an optional value to be used as a starting point for the checksum. They return a 32-bit signed integer value which can also be passed back on subsequent calls as a new starting point argument to produce a running checksum.

```
$ python3 zlib_checksums.py
Adler32:   1559629467
       :   3072466229
CRC-32 :   1880370372
       :   3995978981
```