# [Chapter 9: Cryptography](https://pymotw.com/3/cryptographic.html)

## [9.2 hmac — Cryptographic Message Signing and Verification](https://pymotw.com/3/hmac/index.html)

**Purpose:**	The hmac module implements keyed-hashing for message authentication, as described in RFC 2104.

The HMAC algorithm can be used to verify the integrity of information passed between applications or stored in a potentially vulnerable location. The basic idea is to generate a cryptographic hash of the actual data combined with a shared secret key. The resulting hash can then be used to check the transmitted or stored message to determine a level of trust, without transmitting the secret key.

<div style="color:black; background-color: pink">
Warning

Disclaimer: I am not a security expert. For the full details on HMAC, check out [RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104.html).
</div>

### 9.2.1 Signing Messages

The new() function creates a new object for calculating a message signature. This example uses the default MD5 hash algorithm.

```
# hmac_simple.py
import hmac
import hashlib

digest_maker = hmac.new(b"secret-shared-key-goes-here", digestmod=hashlib.sha256)

with open("lorem.txt", "rb") as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)
```

When run, the code reads a data file and computes an HMAC signature for it.

```
$ python3 hmac_simple.py
d55701ebfe5fdcf9b75889130a1bbae284dadda338c06d1cb92de686a257f693
```

### 9.2.2 Alternate Digest Types

Although the default cryptographic algorithm for hmac is MD5, that is not the most secure method to use. MD5 hashes have some weaknesses, such as collisions (where two different messages produce the same hash). The SHA-1 algorithm is considered to be stronger, and should be used instead.

```
# hmac_sha.py
import hmac
import hashlib

digest_maker = hmac.new(
    b"secret-shared-key-goes-here",
    b"",
    hashlib.sha1,
)

with open("hmac_sha.py", "rb") as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)
```

The new() function takes three arguments. The first is the secret key, which should be shared between the two endpoints that are communicating so both ends can use the same value. The second value is an initial message. If the message content that needs to be authenticated is small, such as a timestamp or HTTP POST, the entire body of the message can be passed to new() instead of using the update() method. The last argument is the digest module to be used. The default is hashlib.md5. This example passes 'sha1', causing hmac to use hashlib.sha1

```
$ python3 hmac_sha.py
c4c4a58bba01500ab6247254bdcf5991aff715ff
```
