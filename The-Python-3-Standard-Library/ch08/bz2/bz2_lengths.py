# bz2_lengths.py
import bz2

original_data = b"This is the original text."

fmt = "{:>15}  {:>15}"
print(fmt.format("len(data)", "len(compressed)"))
print(fmt.format("-" * 15, "-" * 15))

for i in range(5):
    data = original_data * i
    compressed = bz2.compress(data)
    print(fmt.format(len(data), len(compressed)), end="")
    print("*" if len(data) < len(compressed) else "")
