# [Chapter 7: Data Persistence and Exchange](https://pymotw.com/3/persistence.html)

## [7.6 csv — Comma-separated Value Files](https://pymotw.com/3/csv/index.html)

**Purpose:**	Read and write comma separated value files.

The csv module can be used to work with data exported from spreadsheets and databases into text files formatted with fields and records, commonly referred to as comma-separated value (CSV) format because commas are often used to separate the fields in a record.

### 7.6.1 Reading

Use reader() to create a an object for reading data from a CSV file. The reader can be used as an iterator to process the rows of the file in order. For example

```
# csv_reader.py
import csv
import sys

with open(sys.argv[1], 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

The first argument to reader() is the source of text lines. In this case, it is a file, but any iterable is accepted (a StringIO instance, list, etc.). Other optional arguments can be given to control how the input data is parsed.

```
"Title 1","Title 2","Title 3","Title 4"
1,"a",08/18/07,"å"
2,"b",08/19/07,"∫"
3,"c",08/20/07,"ç"
```

As it is read, each row of the input data is parsed and converted to a list of strings.

```
$ python3 csv_reader.py testdata.csv
['Title 1', 'Title 2', 'Title 3', 'Title 4']
['1', 'a', '08/18/07', 'å']
['2', 'b', '08/19/07', '∫']
['3', 'c', '08/20/07', 'ç']
```

The parser handles line breaks embedded within strings in a row, which is why a “row” is not always the same as a “line” of input from the file.

```
"Title 1","Title 2","Title 3"
1,"first line
second line",08/18/07
```

Fields with line breaks in the input retain the internal line breaks when they are returned by the parser.

```
$ python3 csv_reader.py testlinebreak.csv
['Title 1', 'Title 2', 'Title 3']
['1', 'first line\nsecond line', '08/18/07']
```

### 7.6.2 Writing

Writing CSV files is just as easy as reading them. Use writer() to create an object for writing, then iterate over the rows, using writerow() to print them.

```
# csv_writer.py
import csv
import sys

unicode_chars = 'å∫ç'

with open(sys.argv[1], 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('Title 1', 'Title 2', 'Title 3', 'Title 4'))
    for i in range(3):
        row = (
            i + 1,
            chr(ord('a') + i),
            '08/{:02d}/07'.format(i + 1),
            unicode_chars[i],
        )
        writer.writerow(row)

print(open(sys.argv[1], 'rt').read())
```

The output does not look exactly like the exported data used in the reader example because it lacks quotes around some of the values.

```
$ python3 csv_writer.py testout.csv
Title 1,Title 2,Title 3,Title 4
1,a,08/01/07,å
2,b,08/02/07,∫
3,c,08/03/07,ç
```