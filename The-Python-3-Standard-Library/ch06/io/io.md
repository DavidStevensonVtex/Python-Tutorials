# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.11 io — Text, Binary, and Raw Stream I/O Tools](https://pymotw.com/3/io/index.html)

Purpose:	Implements file I/O and provides classes for working with buffers using file-like API.

The io module implements the classes behind the interpreter’s built-in open() for file-based input and output operations. The classes are decomposed in such a way that they can be recombined for alternate purposes, for example to enable writing Unicode data to a network socket.