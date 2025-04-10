# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

Python’s standard library includes a large range of tools for working with files on the file system, building and parsing filenames, and examining file contents.

The first step in working with files is to determine the name of the file to work on. Python represents filenames as simple strings, but provides tools for building them from standard, platform-independent, components in [os.path](https://pymotw.com/3/os.path/index.html#module-os.path).

The [pathlib](https://pymotw.com/3/pathlib/index.html#module-pathlib) module provides an object-oriented API for working with file system paths. Using it instead of [os.path](https://pymotw.com/3/os.path/index.html#module-os.path) provides some conveniences because it operates at a higher level of abstraction.

List the contents of a directory with listdir() from [os](https://pymotw.com/3/os/index.html#module-os), or use [glob](https://pymotw.com/3/glob/index.html#module-glob) to build a list of filenames from a pattern.

The file name pattern matching used by [glob](https://pymotw.com/3/glob/index.html#module-glob) is also exposed directly through [fnmatch](https://pymotw.com/3/fnmatch/index.html#module-fnmatch) so it can be used in other contexts.

After the name of the file is identified, other characteristics, such as permissions or the file size, can be checked using o[s.stat()](https://docs.python.org/3/library/stat.html) and the constants in stat.

When an application needs random access to files, [linecache](https://pymotw.com/3/linecache/index.html#module-linecache) makes it easy to read lines by their line number. The contents of the file are maintained in a cache, so be careful of memory consumption.

[tempfile](https://pymotw.com/3/tempfile/index.html#module-tempfile) is useful for cases that need to create scratch files to hold data temporarily, or before moving it to a permanent location. It provides classes to create temporary files and directories safely and securely. Names are guaranteed to be unique, and include random components so they are not easily guessable.

Frequently, programs need to work on files as a whole, without regard to their content. The [shutil](https://pymotw.com/3/shutil/index.html#module-shutil) module includes high-level file operations such as copying files and directories, and creating or extracting archives of files.

The [filecmp](https://pymotw.com/3/filecmp/index.html#module-filecmp) module compares files and directories by looking at the bytes they contain, but without any special knowledge about their format.

The built-in file class can be used to read and write files visible on local file systems. A program’s performance can suffer when it accesses large files through the read() and write() interfaces, though, since they both involve copying the data multiple times as it is moved from the disk to memory the application can see. Using [mmap](https://pymotw.com/3/mmap/index.html#module-mmap) tells the operating system to use its virtual memory subsystem to map a file’s contents directly into memory accessible by a program, avoiding a copy step between the operating system and the internal buffer for the file object.

Text data using characters not available in ASCII is usually saved in a Unicode data format. Since the standard file handle assumes each byte of a text file represents one character, reading Unicode text with multi-byte encodings requires extra processing. The [codecs](https://pymotw.com/3/codecs/index.html#module-codecs) module handles the encoding and decoding automatically, so that in many cases a non-ASCII file can be used without any other changes to the program.

The [io](https://pymotw.com/3/io/index.html#module-io) module provides access to the classes used to implement Python’s file-based input and output. For testing code that depends on reading or writing data from files, [io](https://pymotw.com/3/io/index.html#module-io) provides an in-memory stream object that behaves like a file, but does not reside on disk.

* [os.path — Platform-independent Manipulation of Filenames](https://pymotw.com/3/os.path/index.html)
* [pathlib — Filesystem Paths as Objects](https://pymotw.com/3/pathlib/index.html)
* [glob — Filename Pattern Matching](https://pymotw.com/3/glob/index.html)
* [fnmatch — Unix-style Glob Pattern Matching](https://pymotw.com/3/fnmatch/index.html)
* [linecache — Read Text Files Efficiently](https://pymotw.com/3/linecache/index.html)
* [tempfile — Temporary File System Objects](https://pymotw.com/3/tempfile/index.html)
* [shutil — High-level File Operations](https://pymotw.com/3/shutil/index.html)
* [filecmp — Compare Files](https://pymotw.com/3/filecmp/index.html)
* [mmap — Memory-map Files](https://pymotw.com/3/mmap/index.html)
* [codecs — String Encoding and Decoding](https://pymotw.com/3/codecs/index.html)
* [io — Text, Binary, and Raw Stream I/O Tools](https://pymotw.com/3/io/index.html)