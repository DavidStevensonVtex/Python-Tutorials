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

#### 7.6.2.1 Quoting

The default quoting behavior is different for the writer, so the second and third columns in the previous example are not quoted. To add quoting, set the quoting argument to one of the other quoting modes.

```
writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
```

In this case, QUOTE_NONNUMERIC adds quotes around all columns that contain values that are not numbers.

```
# csv_writer_quoted.py
import csv
import sys

unicode_chars = 'å∫ç'

with open(sys.argv[1], 'wt') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
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

There are four different quoting options, defined as constants in the csv module.

```
QUOTE_ALL          Quote everything, regardless of type.
QUOTE_MINIMAL      Quote fields with special characters (anything that would confuse a parser configured with the same dialect and options). This is the default
QUOTE_NONNUMERIC   Quote all fields that are not integers or floats. When used with the reader, input fields that are not quoted are converted to floats.
QUOTE_NONE         Do not quote anything on output. When used with the reader, quote characters are included in the field values (normally, they are treated as delimiters and stripped).
```

### 7.6.3 Dialects

There is no well-defined standard for comma-separated value files, so the parser needs to be flexible. This flexibility means there are many parameters to control how csv parses or writes data. Rather than passing each of these parameters to the reader and writer separately, they are grouped together into a dialect object.

Dialect classes can be registered by name, so that callers of the csv module do not need to know the parameter settings in advance. The complete list of registered dialects can be retrieved with list_dialects().

```
# csv_list_dialects.py
import csv

print(csv.list_dialects())
```

The standard library includes three dialects: excel, excel-tabs, and unix. The excel dialect is for working with data in the default export format for Microsoft Excel, and also works with LibreOffice. The unix dialect quotes all fields with double-quotes and uses \n as the record separator.

```
$ python3 csv_list_dialects.py
['excel', 'excel-tab', 'unix']
```

