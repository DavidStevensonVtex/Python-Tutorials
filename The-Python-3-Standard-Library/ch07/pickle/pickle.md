# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.1 pickle — Object Serialization](https://pymotw.com/3/pickle/index.html)

Purpose:	Object serialization

The pickle module implements an algorithm for turning an arbitrary Python object into a series of bytes. This process is also called serializing the object. The byte stream representing the object can then be transmitted or stored, and later reconstructed to create a new object with the same characteristics.

<div style="color: black; background-color:pink">
Warning

The documentation for pickle makes clear that it offers no security guarantees. In fact, unpickling data can execute arbitrary code. Be careful using pickle for inter-process communication or data storage, and do not trust data that cannot be verified as secure. See the hmac module for an example of a secure way to verify the source of a pickled data source.
</div>

### 7.1.1 Encoding and Decoding Data in Strings

This first example Uses dumps() to encode a data structure as a string, then prints the string to the console. It uses a data structure made up of entirely built-in types. Instances of any class can be pickled, as will be illustrated in a later example.

```
# pickle_string.py
import pickle
import pprint

data = [{"a": "A", "b": 2, "c": 3.0}]
print("DATA:", end=" ")
pprint.pprint(data)

data_string = pickle.dumps(data)
print("PICKLE: {!r}".format(data_string))
```

By default, the pickle will be written in a binary format most compatible when sharing between Python 3 programs.

```
$ python3 pickle_string.py
DATA: [{'a': 'A', 'b': 2, 'c': 3.0}]
PICKLE: b'\x80\x04\x95#\x00\x00\x00\x00\x00\x00\x00]\x94}\x94(\x8c\x01a\x94\x8c\x01A\x94\x8c\x01b\x94K\x02\x8c\x01c\x94G@\x08\x00\x00\x00\x00\x00\x00ua.'
```

After the data is serialized, it can be written to a file, socket, pipe, etc. Later, the file can be read and the data unpickled to construct a new object with the same values.

```
# pickle_unpickle.py
import pickle
import pprint

data1 = [{"a": "A", "b": 2, "c": 3.0}]
print("BEFORE: ", end=" ")
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print("AFTER : ", end=" ")
pprint.pprint(data2)

print("SAME? :", (data1 is data2))
print("EQUAL?:", (data1 == data2))
```

The newly constructed object is equal to, but not the same object as, the original.

```
$ python3 pickle_unpickle.py
BEFORE:  [{'a': 'A', 'b': 2, 'c': 3.0}]
AFTER :  [{'a': 'A', 'b': 2, 'c': 3.0}]
SAME? : False
EQUAL?: True
```

### 7.1.2 Working with Streams

In addition to dumps() and loads(), pickle provides convenience functions for working with file-like streams. It is possible to write multiple objects to a stream, and then read them from the stream without knowing in advance how many objects are written, or how big they are.

```
# pickle_stream.py
import io
import pickle
import pprint


class SimpleObject:

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return


data = []
data.append(SimpleObject("pickle"))
data.append(SimpleObject("preserve"))
data.append(SimpleObject("last"))

# Simulate a file.
out_s = io.BytesIO()

# Write to the stream
for o in data:
    print("WRITING : {} ({})".format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

# Set up a read-able stream
in_s = io.BytesIO(out_s.getvalue())

# Read the data
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print("READ    : {} ({})".format(o.name, o.name_backwards))
```

The example simulates streams using two BytesIO buffers. The first receives the pickled objects, and its value is fed to a second from which load() reads. A simple database format could use pickles to store objects, too. The [shelve](https://pymotw.com/3/shelve/index.html#module-shelve) module is one such implementation.

```
$ python3 pickle_stream.py
WRITING : pickle (elkcip)
WRITING : preserve (evreserp)
WRITING : last (tsal)
READ    : pickle (elkcip)
READ    : preserve (evreserp)
READ    : last (tsal)
```

Besides storing data, pickles are handy for inter-process communication. For example, os.fork() and os.pipe() can be used to establish worker processes that read job instructions from one pipe and write the results to another pipe. The core code for managing the worker pool and sending jobs in and receiving responses can be reused, since the job and response objects do not have to be based on a particular class. When using pipes or sockets, do not forget to flush after dumping each object, to push the data through the connection to the other end. See the [multiprocessing](https://pymotw.com/3/multiprocessing/index.html#module-multiprocessing) module for a reusable worker pool manager.

### 7.1.3 Problems Reconstructing Objects

When working with custom classes, the class being pickled must appear in the namespace of the process reading the pickle. Only the data for the instance is pickled, not the class definition. The class name is used to find the constructor to create the new object when unpickling. The following example writes instances of a class to a file.

```
# pickle_dump_to_file_1.py
import pickle
import sys


class SimpleObject:

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = "".join(l)


if __name__ == "__main__":
    data = []
    data.append(SimpleObject("pickle"))
    data.append(SimpleObject("preserve"))
    data.append(SimpleObject("last"))

    filename = sys.argv[1]

    with open(filename, "wb") as out_s:
        for o in data:
            print("WRITING: {} ({})".format(o.name, o.name_backwards))
            pickle.dump(o, out_s)
```

When run, the script creates a file based on the name given as argument on the command line.

```
$ python3 pickle_dump_to_file_1.py test.dat
WRITING: pickle (elkcip)
WRITING: preserve (evreserp)
WRITING: last (tsal)
```

A simplistic attempt to load the resulting pickled objects fails.

```
# pickle_load_from_file_1.py
import pickle
import pprint
import sys

filename = sys.argv[1]

with open(filename, "rb") as in_s:
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print("READ: {} ({})".format(o.name, o.name_backwards))
```

This version fails because there is no SimpleObject class available.

```
$ python3 pickle_load_from_file_1.py test.dat
Traceback (most recent call last):
  File "pickle_load_from_file_1.py", line 11, in <module>
    o = pickle.load(in_s)
AttributeError: Can't get attribute 'SimpleObject' on <module '__main__' from 'pickle_load_from_file_1.py'>
```

The corrected version, which imports SimpleObject from the original script, succeeds. Adding this import statement to the end of the import list allows the script to find the class and construct the object.

`from pickle_dump_to_file_1 import SimpleObject`

Running the modified script now produces the desired results.

```
$ python3 pickle_load_from_file_2.py test.dat
READ: pickle (elkcip)
READ: preserve (evreserp)
READ: last (tsal)
```