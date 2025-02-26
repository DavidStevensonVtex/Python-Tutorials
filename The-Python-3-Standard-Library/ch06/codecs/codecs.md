# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.10 codecs — String Encoding and Decoding](https://pymotw.com/3/codecs/index.html)

Purpose:	Encoders and decoders for converting text between different representations.

The codecs module provides stream and file interfaces for transcoding data. It is most commonly used to work with Unicode text, but other encodings are also available for other purposes.

### 6.10.1 Unicode Primer

CPython 3.x differentiates between text and byte strings. bytes instances use a sequence of 8-bit byte values. In contrast, str strings are managed internally as a sequence of Unicode code points. The code point values are saved as a sequence of 2 or 4 bytes each, depending on the options given when Python was compiled.

When str values are output, they are encoded using one of several standard schemes so that the sequence of bytes can be reconstructed as the same string of text later. The bytes of the encoded value are not necessarily the same as the code point values, and the encoding defines a way to translate between the two sets of values. Reading Unicode data also requires knowing the encoding so that the incoming bytes can be converted to the internal representation used by the unicode class.

The most common encodings for Western languages are UTF-8 and UTF-16, which use sequences of one and two byte values respectively to represent each code point. Other encodings can be more efficient for storing languages where most of the characters are represented by code points that do not fit into two bytes.

#### See also

For more introductory information about Unicode, refer to the list of references at the end of this section. [The Python Unicode HOWTO](https://docs.python.org/3/howto/unicode.html) is especially helpful.