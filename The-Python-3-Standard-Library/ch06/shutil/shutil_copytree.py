# shutil_copytree.py
import glob
import pprint
import shutil

print("BEFORE:")
pprint.pprint(glob.glob("/tmp/example/*"))

shutil.copytree("../shutil", "/tmp/example")

print("\nAFTER:")
pprint.pprint(glob.glob("/tmp/example/*"))
