# [Chapter 9: Cryptography](https://pymotw.com/3/cryptographic.html)

## [9.2 hmac — Cryptographic Message Signing and Verification](https://pymotw.com/3/hmac/index.html)

**Purpose:**	The hmac module implements keyed-hashing for message authentication, as described in RFC 2104.

The HMAC algorithm can be used to verify the integrity of information passed between applications or stored in a potentially vulnerable location. The basic idea is to generate a cryptographic hash of the actual data combined with a shared secret key. The resulting hash can then be used to check the transmitted or stored message to determine a level of trust, without transmitting the secret key.

<div style="color:black; background-color: pink">
Warning

Disclaimer: I am not a security expert. For the full details on HMAC, check out [RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104.html).
</div>