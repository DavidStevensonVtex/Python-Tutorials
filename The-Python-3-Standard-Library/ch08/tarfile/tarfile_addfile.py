# tarfile_addfile.py
import tarfile

print("creating archive")
with tarfile.open("tarfile_addfile.tar", mode="w") as out:
    print("adding README.txt as RENAMED.txt")
    info = out.gettarinfo("README.txt", arcname="RENAMED.txt")
    out.addfile(info)

print()
print("Contents:")
with tarfile.open("tarfile_addfile.tar", mode="r") as t:
    for member_info in t.getmembers():
        print(member_info.name)
