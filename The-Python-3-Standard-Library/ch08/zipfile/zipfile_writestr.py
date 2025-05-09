# zipfile_writestr.py
from zipfile_infolist import print_info
import zipfile

msg = "This data did not exist in a file."
with zipfile.ZipFile(
    "writestr.zip",
    mode="w",
    compression=zipfile.ZIP_DEFLATED,
) as zf:
    zf.writestr("from_string.txt", msg)

print_info("writestr.zip")

with zipfile.ZipFile("writestr.zip", "r") as zf:
    print(zf.read("from_string.txt"))
