# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.3 dbm — Unix Key-Value Databases](https://pymotw.com/3/dbm/index.html)

Purpose:	dbm provides a generic dictionary-like interface to DBM-style, string-keyed databases

dbm is a front-end for DBM-style databases that use simple string values as keys to access records containing strings. It uses whichdb() to identify databases, then opens them with the appropriate module. It is used as a back-end for [shelve](https://pymotw.com/3/shelve/index.html), which stores objects in a DBM database using [pickle](https://pymotw.com/3/pickle/index.html).

### 7.3.1 Database Types

Python comes with several modules for accessing DBM-style databases. The default implementation selected depends on the libraries available on the current system and the options used when Python was compiled. Separate interfaces to the specific implementations allow Python programs to exchange data with programs in other languages that do not automatically switch between available formats, or to write portable data files that will work on multiple platforms.

