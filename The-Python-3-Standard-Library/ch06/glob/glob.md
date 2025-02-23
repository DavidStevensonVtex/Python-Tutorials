# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.3 glob — Filename Pattern Matching](https://pymotw.com/3/glob/index.html)

Purpose:	Use Unix shell rules to find filenames matching a pattern.

Even though the glob API is small, the module packs a lot of power. It is useful in any situation where a program needs to look for a list of files on the file system with names matching a pattern. To create a list of filenames that all have a certain extension, prefix, or any common string in the middle, use glob instead of writing custom code to scan the directory contents.

The pattern rules for glob are not the same as the regular expressions used by the re module. Instead, they follow standard Unix path expansion rules. There are only a few special characters used to implement two different wild-cards and character ranges. The pattern rules are applied to segments of the filename (stopping at the path separator, /). Paths in the pattern can be relative or absolute. Shell variable names and tilde (~) are not expanded.

### 6.3.1 Example Data

The examples in this section assume the following test files are present in the current working directory.

```
$ python3 glob_maketestdata.py
dir
dir/file.txt
dir/file1.txt
dir/file2.txt
dir/filea.txt
dir/fileb.txt
dir/file?.txt
dir/file*.txt
dir/file[.txt
dir/subdir
dir/subdir/subfile.txt
```

If these files do not exist, use glob_maketestdata.py in the sample code to create them before running the following examples.

### 6.3.2 Wildcards

An asterisk (\*) matches zero or more characters in a segment of a name. For example, dir/\*.

```
# glob_asterisk.py
import glob

for name in sorted(glob.glob("dir/*")):
    print(name)
```

The pattern matches every path name (file or directory) in the directory dir, without recursing further into subdirectories. The data returned by glob() is not sorted, so the examples here sort it to make studying the results easier.

```
$ python3 glob_asterisk.py
dir/file*.txt
dir/file.txt
dir/file1.txt
dir/file2.txt
dir/file?.txt
dir/file[.txt
dir/filea.txt
dir/fileb.txt
dir/subdir
```

To list files in a subdirectory, the subdirectory must be included in the pattern.

```
# glob_subdir.py
import glob

print("Named explicitly:")
for name in sorted(glob.glob("dir/subdir/*")):
    print("  {}".format(name))

print("Named with wildcard:")
for name in sorted(glob.glob("dir/*/*")):
    print("  {}".format(name))
```

The first case shown earlier lists the subdirectory name explicitly, while the second case depends on a wildcard to find the directory.

```
$ python3 glob_subdir.py
Named explicitly:
  dir/subdir/subfile.txt
Named with wildcard:
  dir/subdir/subfile.txt
```

The results, in this case, are the same. If there was another subdirectory, the wildcard would match both subdirectories and include the filenames from both.