# itertools_repeat_zip.py
from itertools import *

for i, s in zip(count(), repeat("over-and-over", 5)):
    print(i, s)
