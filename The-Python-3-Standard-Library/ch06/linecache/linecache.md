# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.5 linecache — Read Text Files Efficiently](https://pymotw.com/3/linecache/index.html)

Purpose:	Retrieve lines of text from files or imported Python modules, holding a cache of the results to make reading many lines from the same file more efficient.

The linecache module is used within other parts of the Python standard library when dealing with Python source files. The implementation of the cache holds the contents of files, parsed into separate lines, in memory. The API returns the requested line(s) by indexing into a list, and saves time over repeatedly reading the file and parsing lines to find the one desired. This is especially useful when looking for multiple lines from the same file, such as when producing a traceback for an error report.