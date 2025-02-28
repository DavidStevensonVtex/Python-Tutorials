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

### 7.2.2 Write-back

Shelves do not track modifications to volatile objects, by default. That means if the contents of an item stored in the shelf are changed, the shelf must be updated explicitly by storing the entire item again.

```
# shelve_withoutwriteback.py
import shelve

with shelve.open("test_shelf.db") as s:
    print(s["key1"])
    s["key1"]["new_value"] = "this was not here before"

with shelve.open("test_shelf.db", writeback=True) as s:
    print(s["key1"])
```

In this example, the dictionary at 'key1' is not stored again, so when the shelf is re-opened, the changes have not been preserved.

```
$ python3 shelve_create.py
$ python3 shelve_withoutwriteback.py
{'int': 10, 'float': 9.5, 'string': 'Sample data'}
{'int': 10, 'float': 9.5, 'string': 'Sample data'}
```

To automatically catch changes to volatile objects stored in the shelf, open it with writeback enabled. The writeback flag causes the shelf to remember all of the objects retrieved from the database using an in-memory cache. Each cache object is also written back to the database when the shelf is closed.

```
# shelve_writeback.py
import shelve
import pprint

with shelve.open("test_shelf.db", writeback=True) as s:
    print("Initial data:")
    pprint.pprint(s["key1"])

    s["key1"]["new_value"] = "this was not here before"
    print("\nModified:")
    pprint.pprint(s["key1"])

with shelve.open("test_shelf.db", writeback=True) as s:
    print("\nPreserved:")
    pprint.pprint(s["key1"])
```

Although it reduces the chance of programmer error, and can make object persistence more transparent, using writeback mode may not be desirable in every situation. The cache consumes extra memory while the shelf is open, and pausing to write every cached object back to the database when it is closed slows down the application. All of the cached objects are written back to the database because there is no way to tell if they have been modified. If the application reads data more than it writes, writeback will impact performance unnecessarily.

```
$ python3 shelve_create.py
$ python3 shelve_writeback.py
Initial data:
{'float': 9.5, 'int': 10, 'string': 'Sample data'}

Modified:
{'float': 9.5,
 'int': 10,
 'new_value': 'this was not here before',
 'string': 'Sample data'}

Preserved:
{'float': 9.5,
 'int': 10,
 'new_value': 'this was not here before',
 'string': 'Sample data'}
```