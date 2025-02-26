# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.10 codecs — String Encoding and Decoding](https://pymotw.com/3/codecs/index.html)

Purpose:	Encoders and decoders for converting text between different representations.

The codecs module provides stream and file interfaces for transcoding data. It is most commonly used to work with Unicode text, but other encodings are also available for other purposes.

### 6.10.1 Unicode Primer

CPython 3.x differentiates between text and byte strings. bytes instances use a sequence of 8-bit byte values. In contrast, str strings are managed internally as a sequence of Unicode code points. The code point values are saved as a sequence of 2 or 4 bytes each, depending on the options given when Python was compiled.

When str values are output, they are encoded using one of several standard schemes so that the sequence of bytes can be reconstructed as the same string of text later. The bytes of the encoded value are not necessarily the same as the code point values, and the encoding defines a way to translate between the two sets of values. Reading Unicode data also requires knowing the encoding so that the incoming bytes can be converted to the internal representation used by the unicode class.

The most common encodings for Western languages are UTF-8 and UTF-16, which use sequences of one and two byte values respectively to represent each code point. Other encodings can be more efficient for storing languages where most of the characters are represented by code points that do not fit into two bytes.

See also

For more introductory information about Unicode, refer to the list of references at the end of this section. [The Python Unicode HOWTO](https://docs.python.org/3/howto/unicode.html) is especially helpful.

#### 6.1.1.1 Encodings

The best way to understand encodings is to look at the different series of bytes produced by encoding the same string in different ways. The following examples use this function to format the byte string to make it easier to read.

```
# codecs_to_hex.py
import binascii


def to_hex(t, nbytes):
    """Format text t as a sequence of nbyte long values
    separated by spaces.
    """
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    return b" ".join(
        hex_version[start : start + chars_per_item]
        for start in range(0, len(hex_version), chars_per_item)
    )


if __name__ == "__main__":
    print(to_hex(b"abcdef", 1))
    print(to_hex(b"abcdef", 2))
```

The function uses binascii to get a hexadecimal representation of the input byte string, then insert a space between every nbytes bytes before returning the value.

```
$ python3 codecs_to_hex.py
b'61 62 63 64 65 66'
b'6162 6364 6566'
```

The first encoding example begins by printing the text 'français' using the raw representation of the unicode class, followed by the name of each character from the Unicode database. The next two lines encode the string as UTF-8 and UTF-16 respectively, and show the hexadecimal values resulting from the encoding.

```
# codecs_encodings.py
import unicodedata
from codecs_to_hex import to_hex

text = "français"

print("Raw   : {!r}".format(text))
for c in text:
    print("  {!r}: {}".format(c, unicodedata.name(c, c)))
print("UTF-8 : {!r}".format(to_hex(text.encode("utf-8"), 1)))
print("UTF-16: {!r}".format(to_hex(text.encode("utf-16"), 2)))
```

The result of encoding a str is a bytes object.

```
$ python3 codecs_encodings.py
Raw   : 'français'
  'f': LATIN SMALL LETTER F
  'r': LATIN SMALL LETTER R
  'a': LATIN SMALL LETTER A
  'n': LATIN SMALL LETTER N
  'ç': LATIN SMALL LETTER C WITH CEDILLA
  'a': LATIN SMALL LETTER A
  'i': LATIN SMALL LETTER I
  's': LATIN SMALL LETTER S
UTF-8 : b'66 72 61 6e c3 a7 61 69 73'
UTF-16: b'fffe 6600 7200 6100 6e00 e700 6100 6900 7300'
```

Given a sequence of encoded bytes as a bytes instance, the decode() method translates them to code points and returns the sequence as a str instance.

```
# codecs_decode.py
from codecs_to_hex import to_hex

text = "français"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")

print("Original :", repr(text))
print("Encoded  :", to_hex(encoded, 1), type(encoded))
print("Decoded  :", repr(decoded), type(decoded))
```

The choice of encoding used does not change the output type.

```
$ python3 codecs_decode.py
Original : 'français'
Encoded  : b'66 72 61 6e c3 a7 61 69 73' <class 'bytes'>
Decoded  : 'français' <class 'str'>
```

Note

The default encoding is set during the interpreter start-up process, when [site](https://pymotw.com/3/site/index.html#module-site) is loaded. Refer to the [Unicode Defaults](https://pymotw.com/3/sys/interpreter.html#sys-unicode-defaults) section from the discussion of [sys](https://pymotw.com/3/sys/index.html#module-sys) for a description of the default encoding settings.

### 6.10.2 Working with Files

Encoding and decoding strings is especially important when dealing with I/O operations. Whether writing to a file, socket, or other stream, the data must use the proper encoding. In general, all text data needs to be decoded from its byte representation as it is read, and encoded from the internal values to a specific representation as it is written. A program can explicitly encode and decode data, but depending on the encoding used it can be non-trivial to determine whether enough bytes have been read in order to fully decode the data. codecs provides classes that manage the data encoding and decoding, so applications do not have to do that work.

The simplest interface provided by codecs is an alternative to the built-in open() function. The new version works just like the built-in, but adds two new arguments to specify the encoding and desired error handling technique.

```
# codecs_open_write.py
from codecs_to_hex import to_hex

import codecs
import sys

encoding = sys.argv[1]
filename = encoding + ".txt"

print("Writing to", filename)
with codecs.open(filename, mode="w", encoding=encoding) as f:
    f.write("français")

# Determine the byte grouping to use for to_hex()
nbytes = {
    "utf-8": 1,
    "utf-16": 2,
    "utf-32": 4,
}.get(encoding, 1)

# Show the raw bytes in the file
print("File contents:")
with open(filename, mode="rb") as f:
    print(to_hex(f.read(), nbytes))
```

This example starts with a unicode string with “ç” and saves the text to a file using an encoding specified on the command line.

```
$ python3 codecs_open_write.py utf-8
Writing to utf-8.txt
File contents:
b'66 72 61 6e c3 a7 61 69 73'
$ python3 codecs_open_write.py utf-16
Writing to utf-16.txt
File contents:
b'fffe 6600 7200 6100 6e00 e700 6100 6900 7300'
$ python3 codecs_open_write.py utf-32
Writing to utf-32.txt
File contents:
b'fffe0000 66000000 72000000 61000000 6e000000 e7000000 61000000 69000000 73000000'
```

Reading the data with open() is straightforward, with one catch: the encoding must be known in advance, in order to set up the decoder correctly. Some data formats, such as XML, specify the encoding as part of the file, but usually it is up to the application to manage. codecs simply takes the encoding as an argument and assumes it is correct.

```
# codecs_open_read.py
import codecs
import sys

encoding = sys.argv[1]
filename = encoding + ".txt"

print("Reading from", filename)
with codecs.open(filename, mode="r", encoding=encoding) as f:
    print(repr(f.read()))
```

This example reads the files created by the previous program, and prints the representation of the resulting unicode object to the console.

```
$ python3 codecs_open_read.py utf-8
Reading from utf-8.txt
'français'
$ python3 codecs_open_read.py utf-16
Reading from utf-16.txt
'français'
$ python3 codecs_open_read.py utf-32
Reading from utf-32.txt
'français'
```

### 6.10.3 Byte Order

Multi-byte encodings such as UTF-16 and UTF-32 pose a problem when transferring the data between different computer systems, either by copying the file directly or with network communication. Different systems use different ordering of the high and low order bytes. This characteristic of the data, known as its endianness, depends on factors such as the hardware architecture and choices made by the operating system and application developer. There is not always a way to know in advance what byte order to use for a given set of data, so the multi-byte encodings include a byte-order marker (BOM) as the first few bytes of encoded output. For example, UTF-16 is defined in such a way that 0xFFFE and 0xFEFF are not valid characters, and can be used to indicate the byte order. codecs defines constants for the byte order markers used by UTF-16 and UTF-32.

```
# codecs_bom.py
import codecs
from codecs_to_hex import to_hex

BOM_TYPES = [
    "BOM",
    "BOM_BE",
    "BOM_LE",
    "BOM_UTF8",
    "BOM_UTF16",
    "BOM_UTF16_BE",
    "BOM_UTF16_LE",
    "BOM_UTF32",
    "BOM_UTF32_BE",
    "BOM_UTF32_LE",
]

for name in BOM_TYPES:
    print("{:12} : {}".format(name, to_hex(getattr(codecs, name), 2)))
```

BOM, BOM_UTF16, and BOM_UTF32 are automatically set to the appropriate big-endian or little-endian values depending on the current system’s native byte order.

```
$ python3 codecs_bom.py
BOM          : b'fffe'
BOM_BE       : b'feff'
BOM_LE       : b'fffe'
BOM_UTF8     : b'efbb bf'
BOM_UTF16    : b'fffe'
BOM_UTF16_BE : b'feff'
BOM_UTF16_LE : b'fffe'
BOM_UTF32    : b'fffe 0000'
BOM_UTF32_BE : b'0000 feff'
BOM_UTF32_LE : b'fffe 0000'
```

Byte ordering is detected and handled automatically by the decoders in codecs, but an explicit ordering can be specified when encoding.

```
# codecs_bom_create_file.py
import codecs
from codecs_to_hex import to_hex

# Pick the nonnative version of UTF-16 encoding
if codecs.BOM_UTF16 == codecs.BOM_UTF16_BE:
    bom = codecs.BOM_UTF16_LE
    encoding = "utf_16_le"
else:
    bom = codecs.BOM_UTF16_BE
    encoding = "utf_16_be"

print("Native order  :", to_hex(codecs.BOM_UTF16, 2))
print("Selected order:", to_hex(bom, 2))

# Encode the text.
encoded_text = "français".encode(encoding)
print("{:14}: {}".format(encoding, to_hex(encoded_text, 2)))

with open("nonnative-encoded.txt", mode="wb") as f:
    # Write the selected byte-order marker.  It is not included
    # in the encoded text because the byte order was given
    # explicitly when selecting the encoding.
    f.write(bom)
    # Write the byte string for the encoded text.
    f.write(encoded_text)
```

codecs_bom_create_file.py figures out the native byte ordering, then uses the alternate form explicitly so the next example can demonstrate auto-detection while reading.

```
$ python3 codecs_bom_create_file.py
Native order  : b'fffe'
Selected order: b'feff'
utf_16_be     : b'0066 0072 0061 006e 00e7 0061 0069 0073'
```

codecs_bom_detection.py does not specify a byte order when opening the file, so the decoder uses the BOM value in the first two bytes of the file to determine it.

```
# codecs_bom_detection.py
import codecs
from codecs_to_hex import to_hex

# Look at the raw data
with open("nonnative-encoded.txt", mode="rb") as f:
    raw_bytes = f.read()

print("Raw    :", to_hex(raw_bytes, 2))

# Re-open the file and let codecs detect the BOM
with codecs.open(
    "nonnative-encoded.txt",
    mode="r",
    encoding="utf-16",
) as f:
    decoded_text = f.read()

print("Decoded:", repr(decoded_text))
```

Since the first two bytes of the file are used for byte order detection, they are not included in the data returned by read().

```
$ python3 codecs_bom_detection.py
Raw    : b'feff 0066 0072 0061 006e 00e7 0061 0069 0073'
Decoded: 'français'
```