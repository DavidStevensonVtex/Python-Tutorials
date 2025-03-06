# [Chapter 8: Data Compression and Archiving](https://pymotw.com/3/compression.html)

Although modern computer systems have an ever increasing storage capacity, the growth of data being produced is unrelenting. Lossless compression algorithms make up for some of the shortfall in capacity by trading time spent compressing or decompressing data for the space needed to store it. Python includes interfaces to the most popular compression libraries so it can read and write files interchangeably.

[zlib](https://pymotw.com/3/zlib/index.html) and [gzip](https://pymotw.com/3/gzip/index.html) expose the GNU zip library, and [bz2](https://pymotw.com/3/bz2/index.html) provides access to the more recent bzip2 format. Both formats work on streams of data, without regard to input format, and provide interfaces for reading and writing compressed files transparently. Use these modules for compressing a single file or data source.

The standard library also includes modules to manage archive formats, for combining several files into a single file that can be managed as a unit. [tarfile](https://pymotw.com/3/tarfile/index.html) reads and writes the Unix tape archive format, an old standard still widely used today because of its flexibility. [zipfile](https://pymotw.com/3/zipfile/index.html) works with archives based on the format popularized by the PC program PKZIP, originally used under MS-DOS and Windows, but now also used on other platforms because of the simplicity of its API and portability of the format.

* [zlib — GNU zlib Compression](https://pymotw.com/3/zlib/index.html)
* [gzip — Read and Write GNU zip Files](https://pymotw.com/3/gzip/index.html)
* [bz2 — bzip2 Compression](https://pymotw.com/3/bz2/index.html)
* [tarfile — Tar Archive Access](https://pymotw.com/3/tarfile/index.html)
* [zipfile — ZIP Archive Access](https://pymotw.com/3/zipfile/index.html)