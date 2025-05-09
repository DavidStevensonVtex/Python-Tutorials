# bz2_incremental.py
import bz2
import binascii
import io

compressor = bz2.BZ2Compressor()

with open("lorem.txt", "rb") as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print("Compressed: {}".format(binascii.hexlify(compressed)))
        else:
            print("buffering...")
    remaining = compressor.flush()
    print("Flushed: {}".format(binascii.hexlify(remaining)))
