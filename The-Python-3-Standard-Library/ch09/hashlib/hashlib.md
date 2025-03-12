# [Chapter 9: Cryptography](https://pymotw.com/3/cryptographic.html)

## [9.1 hashlib — Cryptographic Hashing](https://pymotw.com/3/hashlib/index.html)

**Purpose:**	Cryptographic hashes and message digests

The hashlib module defines an API for accessing different cryptographic hashing algorithms. To work with a specific hash algorithm, use the appropriate constructor function or new() to create a hash object. From there, the objects use the same API, no matter what algorithm is being used.
