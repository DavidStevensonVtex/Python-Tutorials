# tarfile_extract.py
import tarfile
import os

os.mkdir("outdir")
with tarfile.open("example.tar", "r") as t:
    t.extract("./tarfile_is_tarfile.py", "outdir")
print(os.listdir("outdir"))
