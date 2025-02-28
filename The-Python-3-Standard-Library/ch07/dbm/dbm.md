# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.3 dbm — Unix Key-Value Databases](https://pymotw.com/3/dbm/index.html)

Purpose:	dbm provides a generic dictionary-like interface to DBM-style, string-keyed databases

dbm is a front-end for DBM-style databases that use simple string values as keys to access records containing strings. It uses whichdb() to identify databases, then opens them with the appropriate module. It is used as a back-end for [shelve](https://pymotw.com/3/shelve/index.html), which stores objects in a DBM database using [pickle](https://pymotw.com/3/pickle/index.html).

### 7.3.1 Database Types

Python comes with several modules for accessing DBM-style databases. The default implementation selected depends on the libraries available on the current system and the options used when Python was compiled. Separate interfaces to the specific implementations allow Python programs to exchange data with programs in other languages that do not automatically switch between available formats, or to write portable data files that will work on multiple platforms.

#### 7.3.1.1 dbm.gnu

dbm.gnu is an interface to the version of the dbm library from the GNU project. It works the same as the other DBM implementations described here, with a few changes to the flags supported by open().

Besides the standard 'r', 'w', 'c', and 'n' flags, dbm.gnu.open() supports:

* 'f' to open the database in _fast_ mode. In fast mode, writes to the database are not synchronized.
* 's' to open the database in _synchronized_ mode. Changes to the database are written to the file as they are made, rather than being delayed until the database is closed or synced explicitly.
* 'u' to open the database unlocked.
* 
#### 7.3.1.2 dbm.ndbm

The dbm.ndbm module provides an interface to the Unix ndbm implementations of the dbm format, depending on how the module was configured during compilation. The module attribute library identifies the name of the library configure was able to find when the extension module was compiled.

#### 7.3.1.3 dbm.dumb

The dbm.dumb module is a portable fallback implementation of the DBM API when no other implementations are available. No external dependencies are required to use dbm.dumb, but it is slower than most other implementations.

