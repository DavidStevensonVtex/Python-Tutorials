# ospath_expanduser.py
import os.path

for user in ["", "dstevenson", "nosuchuser"]:
    lookup = "~" + user
    print("{!r:>15} : {!r}".format(lookup, os.path.expanduser(lookup)))
