# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.3 dbm — Unix Key-Value Databases](https://pymotw.com/3/dbm/index.html)

Purpose:	dbm provides a generic dictionary-like interface to DBM-style, string-keyed databases

dbm is a front-end for DBM-style databases that use simple string values as keys to access records containing strings. It uses whichdb() to identify databases, then opens them with the appropriate module. It is used as a back-end for [shelve](https://pymotw.com/3/shelve/index.html), which stores objects in a DBM database using [pickle](https://pymotw.com/3/pickle/index.html).