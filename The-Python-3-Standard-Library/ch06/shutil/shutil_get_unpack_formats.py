# shutil_get_unpack_formats.py
import shutil

for format, exts, description in shutil.get_unpack_formats():
    print("{:<5}: {}, names ending in {}".format(format, description, exts))
