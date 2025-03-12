# [Chapter 9: Cryptography](https://pymotw.com/3/cryptographic.html)

## [9.1 hashlib — Cryptographic Hashing](https://pymotw.com/3/hashlib/index.html)

**Purpose:**	Cryptographic hashes and message digests

The hashlib module defines an API for accessing different cryptographic hashing algorithms. To work with a specific hash algorithm, use the appropriate constructor function or new() to create a hash object. From there, the objects use the same API, no matter what algorithm is being used.

### 9.1.1 Hash Algorithms

Since hashlib is “backed” by OpenSSL, all of the algorithms provided by that library are available, including:

* md5
* sha1
* sha224
* sha256
* sha384
* sha512*

Some algorithms are available on all platforms, and some depend on the underlying libraries. For lists of each, look at algorithms_guaranteed and algorithms_available respectively.

```
# hashlib_algorithms.py
import hashlib


print("Guaranteed:\n{}\n".format(", ".join(sorted(hashlib.algorithms_guaranteed))))
print("Available:\n{}".format(", ".join(sorted(hashlib.algorithms_available))))
```

```
$ python3 hashlib_algorithms.py
Guaranteed:
blake2b, blake2s, md5, sha1, sha224, sha256, sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512, shake_128, shake_256

Available:
blake2b, blake2s, md4, md5, md5-sha1, ripemd160, sha1, sha224, sha256, sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512, sha512_224, sha512_256, shake_128, shake_256, sm3, whirlpool
```

### 9.1.2 Sample Data

All of the examples in this section use the same sample data:

```
# hashlib_data.py
import hashlib

lorem = """Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum."""
```

### 9.1.3 MD5 Example

To calculate the MD5 hash, or digest, for a block of data (here a unicode string converted to a byte string), first create the hash object, then add the data and call digest() or hexdigest().

```
# hashlib_md5.py
import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode("utf-8"))
print(h.hexdigest())
```

This example uses the hexdigest() method instead of digest() because the output is formatted so it can be printed clearly. If a binary digest value is acceptable, use digest().

```
$ python3 hashlib_md5.py
3f2fd2c9e25d60fb0fa5d593b802b7a8
```

### 9.1.4 SHA1 Example

A SHA1 digest is calculated in the same way.

```
# hashlib_sha1.py
import hashlib

from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem.encode("utf-8"))
print(h.hexdigest())
```

The digest value is different in this example because the algorithm changed from MD5 to SHA1.

```
$ python3 hashlib_sha1.py
ea360b288b3dd178fe2625f55b2959bf1dba6eef
```