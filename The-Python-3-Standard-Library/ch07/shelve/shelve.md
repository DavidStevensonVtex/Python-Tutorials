# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.2 shelve — Persistent Storage of Objects](https://pymotw.com/3/shelve/index.html)

Purpose:	The shelve module implements persistent storage for arbitrary Python objects that can be pickled, using a dictionary-like API.

The shelve module can be used as a simple persistent storage option for Python objects when a relational database is not required. The shelf is accessed by keys, just as with a dictionary. The values are pickled and written to a database created and managed by [dbm](https://pymotw.com/3/dbm/index.html#module-dbm).

### 7.2.1 Creating a new Shelf

The simplest way to use shelve is via the DbfilenameShelf class. It uses dbm to store the data. The class can be used directly, or by calling shelve.open().

```
# shelve_create.py
import shelve

with shelve.open("test_shelf.db") as s:
    s["key1"] = {
        "int": 10,
        "float": 9.5,
        "string": "Sample data",
    }
```

To access the data again, open the shelf and use it like a dictionary.

```
# shelve_existing.py
import shelve

with shelve.open("test_shelf.db") as s:
    existing = s["key1"]

print(existing)
```

Running both sample scripts produces the following output.

```
$ python3 shelve_create.py
$ python3 shelve_existing.py
{'int': 10, 'float': 9.5, 'string': 'Sample data'}
```

The [dbm](https://pymotw.com/3/dbm/index.html#module-dbm) module does not support multiple applications writing to the same database at the same time, but it does support concurrent read-only clients. If a client will not be modifying the shelf, tell shelve to open the database read-only by passing flag='r'.

```
# shelve_readonly.py
import dbm
import shelve

with shelve.open("test_shelf.db", flag="r") as s:
    print("Existing:", s["key1"])
    try:
        s["key1"] = "new value"
    except dbm.error as err:
        print("ERROR: {}".format(err))
```

If the program tries to modify the database while it is opened read-only, an access error exception is generated. The exception type depends on the database module selected by [dbm](https://pymotw.com/3/dbm/index.html#module-dbm) when the database was created.

```
$ python3 shelve_readonly.py
Existing: {'int': 10, 'float': 9.5, 'string': 'Sample data'}
ERROR: Reader can't store
```

