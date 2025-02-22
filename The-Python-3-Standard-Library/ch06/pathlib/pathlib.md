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