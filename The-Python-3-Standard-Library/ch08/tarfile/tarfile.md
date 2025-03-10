# [Chapter 8: Data Compression and Archiving](https://pymotw.com/3/compression.html)

## [8.4 tarfile — Tar Archive Access](https://pymotw.com/3/tarfile/index.html)

**Purpose:**	Tar archive access.

The tarfile module provides read and write access to Unix tar archives, including compressed files. In addition to the POSIX standards, several GNU tar extensions are supported. Unix special file types such as hard and soft links, and device nodes are also handled.

Note

Although tarfile implements a Unix format, it can be used to create and read tar archives under Microsoft Windows, too.