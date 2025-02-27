# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.11 io — Text, Binary, and Raw Stream I/O Tools](https://pymotw.com/3/io/index.html)

Purpose:	Implements file I/O and provides classes for working with buffers using file-like API.

The io module implements the classes behind the interpreter’s built-in open() for file-based input and output operations. The classes are decomposed in such a way that they can be recombined for alternate purposes, for example to enable writing Unicode data to a network socket.

### 6.11.1 In-memory Streams

StringIO provides a convenient means of working with text in memory using the file API (read(), write(), etc.). Using StringIO to build large strings can offer performance savings over some other string concatenation techniques in some cases. In-memory stream buffers are also useful for testing, where writing to a real file on disk may slow down the test suite.

Here are a few standard examples of using StringIO buffers:

```
# io_stringio.py
import io

# Writing to a buffer
output = io.StringIO()
output.write("This goes into the buffer. ")
print("And so does this.", file=output)

# Retrieve the value written
print(output.getvalue())

output.close()  # discard buffer memory

# Initialize a read buffer
input = io.StringIO("Initial value for read buffer")

# Read from the buffer
print(input.read())
```

This example uses read(), but the readline() and readlines() methods are also available. The StringIO class also provides a seek() method for jumping around in a buffer while reading, which can be useful for rewinding if a look-ahead parsing algorithm is being used.

```
$ python3 io_stringio.py
This goes into the buffer. And so does this.

Initial value for read buffer
```

To work with raw bytes instead of Unicode text, use BytesIO.

```
# io_bytesio.py
import io

# Writing to a buffer
output = io.BytesIO()
output.write("This goes into the buffer. ".encode("utf-8"))
output.write("ÁÇÊ".encode("utf-8"))

# Retrieve the value written
print(output.getvalue())

output.close()  # discard buffer memory

# Initialize a read buffer
input = io.BytesIO(b"Initial value for read buffer")

# Read from the buffer
print(input.read())
```

The values written to the BytesIO must be bytes rather than str.

```
$ python3 io_bytesio.py
b'This goes into the buffer. \xc3\x81\xc3\x87\xc3\x8a'
b'Initial value for read buffer'
```

