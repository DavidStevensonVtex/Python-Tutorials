# tempfile_tempdir.py
import tempfile

tempfile.tempdir = "/I/changed/this/path"
print("gettempdir():", tempfile.gettempdir())
