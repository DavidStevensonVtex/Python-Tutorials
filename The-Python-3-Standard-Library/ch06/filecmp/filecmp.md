# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.8 filecmp — Compare Files](https://pymotw.com/3/filecmp/index.html)

Purpose:	Compare files and directories on the file system.

The filecmp module includes functions and a class for comparing files and directories on the file system.

### 6.8.1 Example Data

The examples in this discussion use a set of test files created by filecmp_mkexamples.py.

```
# filecmp_mkexamples.py
import os


def mkfile(filename, body=None):
    with open(filename, "w") as f:
        f.write(body or filename)
    return


def make_example_dir(top):
    if not os.path.exists(top):
        os.mkdir(top)
    curdir = os.getcwd()
    os.chdir(top)

    os.mkdir("dir1")
    os.mkdir("dir2")

    mkfile("dir1/file_only_in_dir1")
    mkfile("dir2/file_only_in_dir2")

    os.mkdir("dir1/dir_only_in_dir1")
    os.mkdir("dir2/dir_only_in_dir2")

    os.mkdir("dir1/common_dir")
    os.mkdir("dir2/common_dir")

    mkfile("dir1/common_file", "this file is the same")
    os.link("dir1/common_file", "dir2/common_file")

    mkfile("dir1/contents_differ")
    mkfile("dir2/contents_differ")
    # Update the access and modification times so most of the stat
    # results will match.
    st = os.stat("dir1/contents_differ")
    os.utime("dir2/contents_differ", (st.st_atime, st.st_mtime))

    mkfile("dir1/file_in_dir1", "This is a file in dir1")
    os.mkdir("dir2/file_in_dir1")

    os.chdir(curdir)
    return


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__) or os.getcwd())
    make_example_dir("example")
    make_example_dir("example/dir1/common_dir")
    make_example_dir("example/dir2/common_dir")
```

Running the script produces a tree of files under the directory example:

```
$ find example | sort
example
example/dir1
example/dir1/common_dir
example/dir1/common_dir/dir1
example/dir1/common_dir/dir1/common_dir
example/dir1/common_dir/dir1/common_file
example/dir1/common_dir/dir1/contents_differ
example/dir1/common_dir/dir1/dir_only_in_dir1
example/dir1/common_dir/dir1/file_in_dir1
example/dir1/common_dir/dir1/file_only_in_dir1
example/dir1/common_dir/dir2
example/dir1/common_dir/dir2/common_dir
example/dir1/common_dir/dir2/common_file
example/dir1/common_dir/dir2/contents_differ
example/dir1/common_dir/dir2/dir_only_in_dir2
example/dir1/common_dir/dir2/file_in_dir1
example/dir1/common_dir/dir2/file_only_in_dir2
example/dir1/common_file
example/dir1/contents_differ
example/dir1/dir_only_in_dir1
example/dir1/file_in_dir1
example/dir1/file_only_in_dir1
example/dir2
example/dir2/common_dir
example/dir2/common_dir/dir1
example/dir2/common_dir/dir1/common_dir
example/dir2/common_dir/dir1/common_file
example/dir2/common_dir/dir1/contents_differ
example/dir2/common_dir/dir1/dir_only_in_dir1
example/dir2/common_dir/dir1/file_in_dir1
example/dir2/common_dir/dir1/file_only_in_dir1
example/dir2/common_dir/dir2
example/dir2/common_dir/dir2/common_dir
example/dir2/common_dir/dir2/common_file
example/dir2/common_dir/dir2/contents_differ
example/dir2/common_dir/dir2/dir_only_in_dir2
example/dir2/common_dir/dir2/file_in_dir1
example/dir2/common_dir/dir2/file_only_in_dir2
example/dir2/common_file
example/dir2/contents_differ
example/dir2/dir_only_in_dir2
example/dir2/file_in_dir1
example/dir2/file_only_in_dir2
```

The same directory structure is repeated one time under the “common_dir” directories to give interesting recursive comparison options.

### 6.8.2 Comparing Files

cmp() compares two files on the file system.

```
# filecmp_cmp.py
import filecmp

print("common_file    :", end=" ")
print(
    filecmp.cmp("example/dir1/common_file", "example/dir2/common_file", shallow=True),
    end=" ",
)
print(
    filecmp.cmp("example/dir1/common_file", "example/dir2/common_file", shallow=False)
)

print("contents_differ:", end=" ")
print(
    filecmp.cmp(
        "example/dir1/contents_differ", "example/dir2/contents_differ", shallow=True
    ),
    end=" ",
)
print(
    filecmp.cmp(
        "example/dir1/contents_differ", "example/dir2/contents_differ", shallow=False
    )
)

print("identical      :", end=" ")
print(
    filecmp.cmp(
        "example/dir1/file_only_in_dir1", "example/dir1/file_only_in_dir1", shallow=True
    ),
    end=" ",
)
print(
    filecmp.cmp(
        "example/dir1/file_only_in_dir1",
        "example/dir1/file_only_in_dir1",
        shallow=False,
    )
)
```

The shallow argument tells cmp() whether to look at the contents of the file, in addition to its metadata. The default is to perform a shallow comparison using the information available from os.stat(). If the stat results are the same, the files are considered the same. Because the stat output includes the inode on Linux, separate files are not treated as the same even if all of their other metadata (size, creation time, etc.) match. In those cases, the file contents are compared. When shallow is False, the contents of the file are always compared.

```
$ python3 filecmp_cmp.py
common_file    : True True
contents_differ: True False
identical      : True True
```

To compare a set of files in two directories without recursing, use cmpfiles(). The arguments are the names of the directories and a list of files to be checked in the two locations. The list of common files passed in should contain only filenames (directories always result in a mismatch) and the files must be present in both locations. The next example shows a simple way to build the common list. The comparison also takes the shallow flag, just as with cmp().

```
# filecmp_cmpfiles.py
import filecmp
import os

# Determine the items that exist in both directories
d1_contents = set(os.listdir("example/dir1"))
d2_contents = set(os.listdir("example/dir2"))
common = list(d1_contents & d2_contents)
common_files = [f for f in common if os.path.isfile(os.path.join("example/dir1", f))]
print("Common files:", common_files)

# Compare the directories
match, mismatch, errors = filecmp.cmpfiles(
    "example/dir1",
    "example/dir2",
    common_files,
)
print("Match       :", match)
print("Mismatch    :", mismatch)
print("Errors      :", errors)
```

cmpfiles() returns three lists of filenames containing files that match, files that do not match, and files that could not be compared (due to permission problems or for any other reason).

```
$ python3 filecmp_cmpfiles.py
Common files: ['file_in_dir1', 'common_file', 'contents_differ']
Match       : ['common_file', 'contents_differ']
Mismatch    : ['file_in_dir1']
Errors      : []
```