# bz2_file_writelines.py
import bz2
import io
import itertools
import os

data = "The same line, over and over.\n"

with bz2.BZ2File("lines.bz2", "wb") as output:
    with io.TextIOWrapper(output, encoding="utf-8") as enc:
        enc.writelines(itertools.repeat(data, 10))

os.system("bzcat lines.bz2")
