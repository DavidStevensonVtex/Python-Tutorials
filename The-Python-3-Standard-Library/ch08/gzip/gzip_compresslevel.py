# gzip_compresslevel.py
import gzip
import io
import os
import hashlib


def get_hash(data):
    return hashlib.md5(data).hexdigest()


data = open("lorem.txt", "r").read() * 1024
cksum = get_hash(data.encode("utf-8"))


print("Level  Size        Checksum")
print("-----  ----------  ---------------------------------")
print("data   {:>10}  {}".format(len(data), cksum))

for i in range(0, 10):
    filename = "compress-level-{}.gz".format(i)
    with gzip.open(filename, "wb", compresslevel=i) as output:
        with io.TextIOWrapper(output, encoding="utf-8") as enc:
            enc.write(data)
    size = os.stat(filename).st_size
    cksum = get_hash(open(filename, "rb").read())
    print("{:>5d}  {:>10d}  {}".format(i, size, cksum))
