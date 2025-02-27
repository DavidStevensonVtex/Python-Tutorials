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