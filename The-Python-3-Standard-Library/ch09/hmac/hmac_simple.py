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
