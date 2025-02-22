# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## 6.2 pathlib — Filesystem Paths as Objects

Purpose:	Parse, build, test, and otherwise work on filenames and paths using an object-oriented API instead of low-level string operations.

### 6.2.1 Path Representations

pathlib includes classes for managing filesystem paths formatted using either the POSIX standard or Microsoft Windows syntax. It includes so called “pure” classes, which operate on strings but do not interact with an actual filesystem, and “concrete” classes, which extend the API to include operations that reflect or modify data on the local filesystem.

The pure classes PurePosixPath and PureWindowsPath can be instantiated and used on any operating system, since they only work on names. To instantiate the correct class for working with a real filesystem, use Path to get either a PosixPath or WindowsPath, depending on the platform.

### 6.2.2 Building Paths

To instantiate a new path, give a string as the first argument. The string representation of the path object is this name value. To create a new path referring to a value relative to an existing path, use the / operator to extend the path. The argument to the operator can either be a string or another path object.

```
# pathlib_operator.py
import pathlib

usr = pathlib.PurePosixPath("/usr")
print(usr)

usr_local = usr / "local"
print(usr_local)

usr_share = usr / pathlib.PurePosixPath("share")
print(usr_share)

root = usr / ".."
print(root)

etc = root / "/etc/"
print(etc)
```

As the value for root in the example output shows, the operator combines the path values as they are given, and does not normalize the result when it contains the parent directory reference "..". However, if a segment begins with the path separator it is interpreted as a new “root” reference in the same way as os.path.join(). Extra path separators are removed from the middle of the path value, as in the etc example here.

```
$ python3 pathlib_operator.py
/usr
/usr/local
/usr/share
/usr/..
/etc
```

The concrete path classes include a resolve() method for normalizing a path by looking at the filesystem for directories and symbolic links and producing the absolute path referred to by a name.

```
# pathlib_resolve.py
import pathlib

usr_local = pathlib.Path("/usr/local")
share = usr_local / ".." / "share"
print(share.resolve())
```

Here the relative path is converted to the absolute path to /usr/share. If the input path includes symlinks, those are expanded as well to allow the resolved path to refer directly to the target.

```
$ python3 pathlib_resolve.py
/usr/share
```

To build paths when the segments are not known in advance, use joinpath(), passing each path segment as a separate argument.

```
# pathlib_joinpath.py
import pathlib

root = pathlib.PurePosixPath("/")
subdirs = ["usr", "local"]
usr_local = root.joinpath(*subdirs)
print(usr_local)
```

As with the / operator, calling joinpath() creates a new instance.

```
$ python3 pathlib_joinpath.py
/usr/local
```

Given an existing path object, it is easy to build a new one with minor differences such as referring to a different file in the same directory. Use with_name() to create a new path that replaces the name portion of a path with a different file name. Use with_suffix() to create a new path that replaces the file name’s extension with a different value.

```
# pathlib_from_existing.py
import pathlib

ind = pathlib.PurePosixPath("source/pathlib/index.rst")
print(ind)

py = ind.with_name("pathlib_from_existing.py")
print(py)

pyc = py.with_suffix(".pyc")
print(pyc)
```

Both methods return new objects, and the original is left unchanged.

```
$ python3 pathlib_from_existing.py
source/pathlib/index.rst
source/pathlib/pathlib_from_existing.py
source/pathlib/pathlib_from_existing.pyc
```

### 6.2.3 Parsing Paths

Path objects have methods and properties for extracting partial values from the name. For example, the parts property produces a sequence of path segments parsed based on the path separator value.

```
# pathlib_parts.py
import pathlib

p = pathlib.PurePosixPath("/usr/local")
print(p.parts)
```

The sequence is a tuple, reflecting the immutability of the path instance.

```
$ python3 pathlib_parts.py
('/', 'usr', 'local')
```

There are two ways to navigate “up” the filesystem hierarchy from a given path object. The parent property refers to a new path instance for the directory containing the path, the value returned by os.path.dirname(). The parents property is an iterable that produces parent directory references, continually going “up” the path hierarchy until reaching the root.

```
# pathlib_parents.py
import pathlib

p = pathlib.PurePosixPath("/usr/local/lib")

print("parent: {}".format(p.parent))

print("\nhierarchy:")
for up in p.parents:
    print(up)
```

The example iterates over the parents property and prints the member values.

```
$ python3 pathlib_parents.py
parent: /usr/local

hierarchy:
/usr/local
/usr
/
```

Other parts of the path can be accessed through properties of the path object. The name property holds the last part of the path, after the final path separator (the same value that os.path.basename() produces). The suffix property holds the value after the extension separator and the stem property holds the portion of the name before the suffix.

```
# pathlib_name.py
import pathlib

p = pathlib.PurePosixPath("./source/pathlib/pathlib_name.py")
print("path  : {}".format(p))
print("name  : {}".format(p.name))
print("suffix: {}".format(p.suffix))
print("stem  : {}".format(p.stem))
```

Although the suffix and stem values are similar to the values produced by os.path.splitext(), the values are based only on the value of name and not the full path.

```
$ python3 pathlib_name.py
path  : source/pathlib/pathlib_name.py
name  : pathlib_name.py
suffix: .py
stem  : pathlib_name
```

### 6.2.4 Creating Concrete Paths

Instances of the concrete Path class can be created from string arguments referring to the name (or potential name) of a file, directory, or symbolic link on the file system. The class also provides several convenience methods for building instances using commonly used locations that change, such as the current working directory and the user’s home directory.

```
# pathlib_convenience.py
import pathlib

home = pathlib.Path.home()
print("home: ", home)

cwd = pathlib.Path.cwd()
print("cwd : ", cwd)
```

Both methods create Path instances pre-populated with an absolute file system reference.

```
$ python3 pathlib_convenience.py
home:  /home/dstevenson
cwd :  /home/dstevenson/Python/GitHub/Python-Tutorials/The-Python-3-Standard-Library/ch06/pathlib
```

### 6.2.5 Directory Contents

There are three methods for accessing the directory listings to discover the names of files available on the file system. iterdir() is a generator, yielding a new Path instance for each item in the containing directory.

```
# pathlib_iterdir.py
import pathlib

p = pathlib.Path(".")

for f in p.iterdir():
    print(f)
```

If the Path does not refer to a directory, iterdir() raises NotADirectoryError.

```
$ python3 pathlib_iterdir.py
pathlib_joinpath.py
pathlib_from_existing.py
pathlib_parts.py
pathlib_convenience.py
pathlib_iterdir.py
pathlib_parents.py
pathlib_operator.py
pathlib_name.py
pathlib_resolve.py
pathlib.md
```

Use glob() to find only files matching a pattern.

```
# pathlib_glob.py
import pathlib

p = pathlib.Path("..")

for f in p.glob("*.md"):
    print(f)
```

This example shows all of the Markdown files in the parent directory of the script.

```
$ python3 pathlib_glob.py
../the-file-system.md
```

The glob processor supports recursive scanning using the pattern prefix ** or by calling rglob() instead of glob().

```
# pathlib_rglob.py
import pathlib

p = pathlib.Path("..")

for f in p.rglob("pathlib_*.py"):
    print(f)
```

Because this example starts from the parent directory, a recursive search is necessary to find the example files matching pathlib_*.py.

```
$ python3 pathlib_rglob.py
../pathlib/pathlib_joinpath.py
../pathlib/pathlib_from_existing.py
../pathlib/pathlib_glob.py
../pathlib/pathlib_parts.py
../pathlib/pathlib_rglob.py
../pathlib/pathlib_convenience.py
../pathlib/pathlib_iterdir.py
../pathlib/pathlib_parents.py
../pathlib/pathlib_operator.py
../pathlib/pathlib_name.py
../pathlib/pathlib_resolve.py
```

### 6.2.6 Reading and Writing Files

Each Path instance includes methods for working with the contents of the file to which it refers. For immediately retrieving the contents, use read_bytes() or read_text(). To write to the file, use write_bytes() or write_text(). Use the open() method to open the file and retain the file handle, instead of passing the name to the built-in open() function.

```
# pathlib_read_write.py
import pathlib

f = pathlib.Path("example.txt")

f.write_bytes("This is the content".encode("utf-8"))

with f.open("r", encoding="utf-8") as handle:
    print("read from open(): {!r}".format(handle.read()))

print("read_text(): {!r}".format(f.read_text("utf-8")))
```

The convenience methods do some type checking before opening the file and writing to it, but otherwise they are equivalent to doing the operation directly.

```
$ python3 pathlib_read_write.py
read from open(): 'This is the content'
read_text(): 'This is the content'
```

### 6.2.7 Manipulating Directories and Symbolic Links

Paths representing directories or symbolic links that do not exist can be used to create the associated file system entries.

```
# pathlib_mkdir.py
import pathlib

p = pathlib.Path("example_dir")

print("Creating {}".format(p))
p.mkdir()
```

If the path already exists, mkdir() raises a FileExistsError.

```
$ python3 pathlib_mkdir.py
Creating example_dir
$ python3 pathlib_mkdir.py
Creating example_dir
Traceback (most recent call last):
  File "pathlib_mkdir.py", line 7, in <module>
    p.mkdir()
  File "/usr/lib/python3.8/pathlib.py", line 1288, in mkdir
    self._accessor.mkdir(self, mode)
FileExistsError: [Errno 17] File exists: 'example_dir'
```

Use symlink_to() to create a symbolic link. The link will be named based on the path’s value and will refer to the name given as argument to symlink_to().

```
# pathlib_symlink_to.py
import pathlib

p = pathlib.Path("example_link")

p.symlink_to("pathlib.md")

print(p)
print(p.resolve().name)
```

This example creates a symbolic link, then uses resolve() to read the link to find what it points to and print the name.

```
$ python3 pathlib_symlink_to.py
example_link
pathlib.md
```