# Chapter 2: [Data Structures](https://pymotw.com/3/data_structures.html)

## [2.7 struct — Binary Data Structures](https://pymotw.com/3/struct/index.html)

Purpose:	Convert between strings and binary data.

The [struct module](https://docs.python.org/3/library/struct.html) includes functions for converting between strings of bytes and native Python data types such as numbers and strings.

### 2.7.1 Functions versus Struct Class

A set of module-level functions is available for working with structured values, as well as the Struct class. Format specifiers are converted from their string format to a compiled representation, similar to the way regular expressions are handled. The conversion takes some resources, so it is typically more efficient to do it once when creating a Struct instance and call methods on the instance instead of using the module-level functions. All of the following examples use the Struct class.

### 2.7.2 Packing and Unpacking

Structs support _packing_ data into strings, and _unpacking_ data from strings using format specifiers made up of characters representing the type of the data and optional count and endianness indicators. Refer to the standard library documentation for a complete list of the supported format specifiers.

In this example, the specifier calls for an integer or long integer value, a two-byte string, and a floating-point number. The spaces in the format specifier are included to separate the type indicators, and are ignored when the format is compiled.

```
# struct_pack.py
import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print('Original values:', values)
print('Format string  :', s.format)
print('Uses           :', s.size, 'bytes')
print('Packed Value   :', binascii.hexlify(packed_data))
```

The example converts the packed value to a sequence of hex bytes for printing with binascii.hexlify(), since some of the characters are nulls.

```
$ python3 struct_pack.py
Original values: (1, b'ab', 2.7)
Format string  : I 2s f
Uses           : 12 bytes
Packed Value   : b'0100000061620000cdcc2c40'
```

Use unpack() to extract data from its packed representation.

```
# struct_unpack.py
import struct
import binascii

packed_data = binascii.unhexlify(b'0100000061620000cdcc2c40')

s = struct.Struct('I 2s f')
unpacked_data = s.unpack(packed_data)
print('Unpacked Values:', unpacked_data)
```

Passing the packed value to unpack(), gives basically the same values back (note the discrepancy in the floating point value).

```
$ python3 struct_unpack.py
Unpacked Values: (1, b'ab', 2.700000047683716)
```