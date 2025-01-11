# File demo.py
import sys
print(sys.argv)

# $ python3 demo.py abc def ghi jkl
# ['demo.py', 'abc', 'def', 'ghi', 'jkl']

The [argparse](https://docs.python.org/3/library/argparse.html#module-argparse) module provides a more sophisticated mechanism to process command line arguments. 
The following script extracts one or more filenames and an optional number of lines to be displayed:

```
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```