# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.2 shelve — Persistent Storage of Objects](https://pymotw.com/3/shelve/index.html)

Purpose:	The shelve module implements persistent storage for arbitrary Python objects that can be pickled, using a dictionary-like API.

The shelve module can be used as a simple persistent storage option for Python objects when a relational database is not required. The shelf is accessed by keys, just as with a dictionary. The values are pickled and written to a database created and managed by dbm.