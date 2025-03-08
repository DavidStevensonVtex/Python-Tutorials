# [Chapter 8: Data Compression and Archiving](https://pymotw.com/3/compression.html)

## [8.3 bz2 — bzip2 Compression](https://pymotw.com/3/bz2/index.html)

**Purpose:**	bzip2 compression

The bz2 module is an interface for the bzip2 library, used to compress data for storage or transmission. There are three APIs provided:

* “one shot” compression/decompression functions for operating on a blob of data
* iterative compression/decompression objects for working with streams of data
* a file-like class that supports reading and writing as with an uncompressed file