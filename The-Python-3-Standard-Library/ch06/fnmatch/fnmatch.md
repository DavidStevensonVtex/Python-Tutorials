# [Chapter 6: The File System](https://pymotw.com/3/file_access.html)

## [6.4 fnmatch — Unix-style Glob Pattern Matching](https://pymotw.com/3/fnmatch/index.html)

Purpose:	Handle Unix-style filename comparisons.

The fnmatch module is used to compare filenames against glob-style patterns such as used by Unix shells.

### 6.4.1 Simple Matching

fnmatch() compares a single filename against a pattern and returns a boolean, indicating whether or not they match. The comparison is case-sensitive when the operating system uses a case-sensitive file system.

```
# fnmatch_fnmatch.py
import fnmatch
import os

pattern = "fnmatch_*.py"
print("Pattern :", pattern)
print()

files = os.listdir(".")
for name in sorted(files):
    print("Filename: {:<25} {}".format(name, fnmatch.fnmatch(name, pattern)))
```

In this example, the pattern matches all files starting with 'fnmatch_' and ending in '.py'.

```
$ python3 fnmatch_fnmatch.py
Pattern : fnmatch_*.py

Filename: fnmatch.md                False
Filename: fnmatch_fnmatch.py        True
```

To force a case-sensitive comparison, regardless of the file system and operating system settings, use fnmatchcase().

```
# fnmatch_fnmatchcase.py
import fnmatch
import os

pattern = "FNMATCH_*.PY"
print("Pattern :", pattern)
print()

files = os.listdir(".")

for name in sorted(files):
    print("Filename: {:<25} {}".format(name, fnmatch.fnmatchcase(name, pattern)))
```

Since the OS X system used to test this program uses a case-sensitive file system, no files match the modified pattern.

```
$ uname -a
Linux dstevensonlinux1 5.4.0-205-generic #225-Ubuntu SMP Fri Jan 10 22:23:35 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
$ python3 fnmatch_fnmatchcase.py
Pattern : FNMATCH_*.PY

Filename: fnmatch.md                False
Filename: fnmatch_fnmatch.py        False
Filename: fnmatch_fnmatchcase.py    False
```

### 6.4.2 Filtering

To test a sequence of filenames, use filter(), which returns a list of the names that match the pattern argument.

```
# fnmatch_filter.py
import fnmatch
import os
import pprint

pattern = "fnmatch_*.py"
print("Pattern :", pattern)

files = list(sorted(os.listdir(".")))

print("\nFiles   :")
pprint.pprint(files)

print("\nMatches :")
pprint.pprint(fnmatch.filter(files, pattern))
```

In this example, filter() returns the list of names of the example source files associated with this section.

```
$ python3 fnmatch_filter.py
Pattern : fnmatch_*.py

Files   :
['fnmatch.md',
 'fnmatch_filter.py',
 'fnmatch_fnmatch.py',
 'fnmatch_fnmatchcase.py']

Matches :
['fnmatch_filter.py', 'fnmatch_fnmatch.py', 'fnmatch_fnmatchcase.py']
```