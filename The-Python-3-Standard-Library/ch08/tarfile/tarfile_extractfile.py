# tarfile_extractfile.py
import tarfile

with tarfile.open("example.tar", "r") as t:
    for filename in ["README.txt", "notthere.txt"]:
        try:
            f = t.extractfile(filename)
        except KeyError:
            print("ERROR: Did not find {} in tar archive".format(filename))
        else:
            print(filename, ":")
            print(f.read().decode("utf-8"))
