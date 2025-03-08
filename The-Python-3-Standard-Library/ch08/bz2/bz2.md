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

### 8.3.7 Compressing Network Data

The code in the next example responds to requests consisting of filenames by writing a compressed version of the file to the socket used to communicate with the client. It has some artificial chunking in place to illustrate the buffering that occurs when the data passed to compress() or decompress() does not result in a complete block of compressed or uncompressed output.

```
# bz2_server.py
import bz2
import logging
import socketserver
import binascii

BLOCK_SIZE = 32


class Bz2RequestHandler(socketserver.BaseRequestHandler):

    logger = logging.getLogger('Server')

    def handle(self):
        compressor = bz2.BZ2Compressor()

        # Find out what file the client wants
        filename = self.request.recv(1024).decode('utf-8')
        self.logger.debug('client asked for: "%s"', filename)

        # Send chunks of the file as they are compressed
        with open(filename, 'rb') as input:
            while True:
                block = input.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('RAW %r', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug(
                        'SENDING %r',
                        binascii.hexlify(compressed))
                    self.request.send(compressed)
                else:
                    self.logger.debug('BUFFERING')

        # Send any data being buffered by the compressor
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('FLUSHING %r',
                              binascii.hexlify(to_send))
            self.request.send(to_send)
        return
```

The main program starts a server in a thread, combining SocketServer and Bz2RequestHandler.

```
if __name__ == '__main__':
    import socket
    import sys
    from io import StringIO
    import threading

    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s: %(message)s',
                        )

    # Set up a server, running in a separate thread
    address = ('localhost', 0)  # let the kernel assign a port
    server = socketserver.TCPServer(address, Bz2RequestHandler)
    ip, port = server.server_address  # what port was assigned?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    logger = logging.getLogger('Client')

    # Connect to the server
    logger.info('Contacting server on %s:%s', ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Ask for a file
    requested_file = (sys.argv[0]
                      if len(sys.argv) > 1
                      else 'lorem.txt')
    logger.debug('sending filename: "%s"', requested_file)
    len_sent = s.send(requested_file.encode('utf-8'))

    # Receive a response
    buffer = StringIO()
    decompressor = bz2.BZ2Decompressor()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('READ %r', binascii.hexlify(response))

        # Include any unconsumed data when feeding the
        # decompressor.
        decompressed = decompressor.decompress(response)
        if decompressed:
            logger.debug('DECOMPRESSED %r', decompressed)
            buffer.write(decompressed.decode('utf-8'))
        else:
            logger.debug('BUFFERING')

    full_response = buffer.getvalue()
    lorem = open(requested_file, 'rt').read()
    logger.debug('response matches file contents: %s',
                 full_response == lorem)

    # Clean up
    server.shutdown()
    server.socket.close()
    s.close()
```

It then opens a socket to communicate with the server as a client, and requests the file (defaulting to lorem.txt) which contains:

```
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Donec egestas, enim et consectetuer ullamcorper, lectus ligula rutrum leo,
a elementum elit tortor eu quam. Duis tincidunt nisi ut ante. Nulla
facilisi. Sed tristique eros eu libero. Pellentesque vel
arcu. Vivamus purus orci, iaculis ac, suscipit sit amet, pulvinar eu,
lacus. Praesent placerat tortor sed nisl. Nunc blandit diam egestas
dui. Pellentesque habitant morbi tristique senectus et netus et
malesuada fames ac turpis egestas. Aliquam viverra fringilla
leo. Nulla feugiat augue eleifend nulla. Vivamus mauris. Vivamus sed
mauris in nibh placerat egestas. Suspendisse potenti. Mauris
massa. Ut eget velit auctor tortor blandit sollicitudin. Suspendisse
imperdiet justo.
```

<div style="color: black; background-color: pink;">
Warning

This implementation has obvious security implications. Do not run it on a server on the open Internet or in any environment where security might be an issue.
</div>

Running bz2_server.py produces:

```
$ python3 bz2_server.py 
Client: Contacting server on 127.0.0.1:57479
Client: sending filename: "lorem.txt"
Server: client asked for: "lorem.txt"
Server: RAW b'Lorem ipsum dolor sit amet, cons'
Server: BUFFERING
Server: RAW b'ectetuer adipiscing elit.\nDonec '
Server: BUFFERING
Server: RAW b'egestas, enim et consectetuer ul'
Server: BUFFERING
Server: RAW b'lamcorper, lectus ligula rutrum '
Server: BUFFERING
Server: RAW b'leo,\na elementum elit tortor eu '
Server: BUFFERING
Server: RAW b'quam. Duis tincidunt nisi ut ant'
Server: BUFFERING
Server: RAW b'e. Nulla\nfacilisi. Sed tristique'
Server: BUFFERING
Server: RAW b' eros eu libero. Pellentesque ve'
Server: BUFFERING
Server: RAW b'l\narcu. Vivamus purus orci, iacu'
Server: BUFFERING
Server: RAW b'lis ac, suscipit sit amet, pulvi'
Server: BUFFERING
Server: RAW b'nar eu,\nlacus. Praesent placerat'
Server: BUFFERING
Server: RAW b' tortor sed nisl. Nunc blandit d'
Server: BUFFERING
Server: RAW b'iam egestas\ndui. Pellentesque ha'
Server: BUFFERING
Server: RAW b'bitant morbi tristique senectus '
Server: BUFFERING
Server: RAW b'et netus et\nmalesuada fames ac t'
Server: BUFFERING
Server: RAW b'urpis egestas. Aliquam viverra f'
Server: BUFFERING
Server: RAW b'ringilla\nleo. Nulla feugiat augu'
Server: BUFFERING
Server: RAW b'e eleifend nulla. Vivamus mauris'
Server: BUFFERING
Server: RAW b'. Vivamus sed\nmauris in nibh pla'
Server: BUFFERING
Server: RAW b'cerat egestas. Suspendisse poten'
Server: BUFFERING
Server: RAW b'ti. Mauris\nmassa. Ut eget velit '
Server: BUFFERING
Server: RAW b'auctor tortor blandit sollicitud'
Server: BUFFERING
Server: RAW b'in. Suspendisse\nimperdiet justo.'
Server: BUFFERING
Server: FLUSHING b'425a6839314159265359cb07c9da000042d7800010400524074b003ff7ff0040'
Server: FLUSHING b'01d2e34183423129ed53d353ca34068341aa78d26446a34d0068c818d3118469'
Client: READ b'425a6839314159265359cb07c9da000042d7800010400524074b003ff7ff0040'
Server: FLUSHING b'80000129910453d3265234f53689ea0cddf6e3ccaee7a400028dce03aac30d41'
Client: BUFFERING
Server: FLUSHING b'7615abf883428245302e5e197e9047c4c836ad3262ab674a0a16613eee561f2d'
Client: READ b'01d2e34183423129ed53d353ca34068341aa78d26446a34d0068c818d3118469'
Server: FLUSHING b'b16ad21a50bad29ca48a9a258422e72793045c04ae97373c3041eec9137bacc2'
Client: BUFFERING
Server: FLUSHING b'b5cff449ccf7ed21a69a973c514573633d4854be0bdcc60dd19c0cca77ab4d82'
Client: READ b'80000129910453d3265234f53689ea0cddf6e3ccaee7a400028dce03aac30d41'
Server: FLUSHING b'bdb3a5e123daf22d99e7304eec48f26d5dffa66ea8d7bb362ff02f59db1ce87e'
Client: BUFFERING
Server: FLUSHING b'c35b9ca9b9639a8dfa78457bc1c355d9d33ced467ed7e164938b33be5119e31a'
Client: READ b'7615abf883428245302e5e197e9047c4c836ad3262ab674a0a16613eee561f2d'
Server: FLUSHING b'157ab875d16e8b629208b83364cdf5f51b6dc6988d96a6ef53182475eee579cf'
Client: BUFFERING
Server: FLUSHING b'5886d433e46615539331874a1d9c28b2a892eed426892ad4d0523bf5db9fae8a'
Client: READ b'b16ad21a50bad29ca48a9a258422e72793045c04ae97373c3041eec9137bacc2'
Server: FLUSHING b'8dd7c69f76a8d3ad4785c1984849525b706ea197f0c929bf1cc6c5152dc4ceb7'
Client: BUFFERING
Server: FLUSHING b'd6e8a2edc0a869eaa59fa3118b0c4ac497a18225f6b3a295a5bf53848a8a9866'
Client: READ b'b5cff449ccf7ed21a69a973c514573633d4854be0bdcc60dd19c0cca77ab4d82'
Server: FLUSHING b'42b44702d2a3429c8855e81e68a0c8df715b7990081a7aead4fc2231c62ed582'
Client: BUFFERING
Server: FLUSHING b'9b19746315a6c3786c1203ee9fc5dc914e142432c1f27680'
Client: READ b'bdb3a5e123daf22d99e7304eec48f26d5dffa66ea8d7bb362ff02f59db1ce87e'
Client: BUFFERING
Client: READ b'c35b9ca9b9639a8dfa78457bc1c355d9d33ced467ed7e164938b33be5119e31a'
Client: BUFFERING
Client: READ b'157ab875d16e8b629208b83364cdf5f51b6dc6988d96a6ef53182475eee579cf'
Client: BUFFERING
Client: READ b'5886d433e46615539331874a1d9c28b2a892eed426892ad4d0523bf5db9fae8a'
Client: BUFFERING
Client: READ b'8dd7c69f76a8d3ad4785c1984849525b706ea197f0c929bf1cc6c5152dc4ceb7'
Client: BUFFERING
Client: READ b'd6e8a2edc0a869eaa59fa3118b0c4ac497a18225f6b3a295a5bf53848a8a9866'
Client: BUFFERING
Client: READ b'42b44702d2a3429c8855e81e68a0c8df715b7990081a7aead4fc2231c62ed582'
Client: BUFFERING
Client: READ b'9b19746315a6c3786c1203ee9fc5dc914e142432c1f27680'
Client: DECOMPRESSED b'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\nDonec egestas, enim et consectetuer ullamcorper, lectus ligula rutrum leo,\na elementum elit tortor eu quam. Duis tincidunt nisi ut ante. Nulla\nfacilisi. Sed tristique eros eu libero. Pellentesque vel\narcu. Vivamus purus orci, iaculis ac, suscipit sit amet, pulvinar eu,\nlacus. Praesent placerat tortor sed nisl. Nunc blandit diam egestas\ndui. Pellentesque habitant morbi tristique senectus et netus et\nmalesuada fames ac turpis egestas. Aliquam viverra fringilla\nleo. Nulla feugiat augue eleifend nulla. Vivamus mauris. Vivamus sed\nmauris in nibh placerat egestas. Suspendisse potenti. Mauris\nmassa. Ut eget velit auctor tortor blandit sollicitudin. Suspendisse\nimperdiet justo.'
Client: response matches file contents: True
```

### See also

* [Standard library documentation for bz2](https://docs.python.org/3/library/bz2.html)
* [bzip2.org](http://www.bzip.org/) – The home page for bzip2.
* [zlib](https://pymotw.com/3/zlib/index.html) – The zlib module for GNU zip compression.
* [gzip](https://pymotw.com/3/gzip/index.html) – A file-like interface to GNU zip compressed files.
* [io](https://pymotw.com/3/io/index.html) – Building-blocks for creating input and output pipelines.
* [Python 2 to 3 porting notes for bz2](https://pymotw.com/3/porting_notes.html#porting-bz2)