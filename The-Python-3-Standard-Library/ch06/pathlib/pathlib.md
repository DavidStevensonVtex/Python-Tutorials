# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## 6.2 pathlib — Filesystem Paths as Objects

Purpose:	Parse, build, test, and otherwise work on filenames and paths using an object-oriented API instead of low-level string operations.

### 6.2.1 Path Representations

pathlib includes classes for managing filesystem paths formatted using either the POSIX standard or Microsoft Windows syntax. It includes so called “pure” classes, which operate on strings but do not interact with an actual filesystem, and “concrete” classes, which extend the API to include operations that reflect or modify data on the local filesystem.

The pure classes PurePosixPath and PureWindowsPath can be instantiated and used on any operating system, since they only work on names. To instantiate the correct class for working with a real filesystem, use Path to get either a PosixPath or WindowsPath, depending on the platform.