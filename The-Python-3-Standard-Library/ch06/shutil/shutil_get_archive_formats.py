# shutil_get_archive_formats.py
import shutil

for format, description in shutil.get_archive_formats():
    print("{:<5}: {}".format(format, description))
