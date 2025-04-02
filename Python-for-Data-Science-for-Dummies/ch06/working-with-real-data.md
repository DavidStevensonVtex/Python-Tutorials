# Python for Data Science for Dummies, 3rd Edition, © 2024

## Chapter 6: Working with Real Data

Data is messy. It appears in all sorts of places, in many different forms, and you can interpret it in many ways.

Real data requiers a lot of work to use, and fortunately, Python is up to the task of manipulating it as needed.

The techniques in this chapter demonstrate how to access data in the formats you most commonly encounter when working with real-world data.

The Scikit-learn library includes a number of toy datasets (small datasets meant for you to play with). These datasets are complex enough to perform a number of tasks, such as experimenting with Python to perform data science tasks.

### Uploading, Streaming, and Sampling Data

Storing data in local computer memory represents the fastest and most reliable means to access it.
You load the data into memory from the storage location and then interact with it in memory.

This is the technique the book uses to access all the toy datasets found in the Scikit-learn library, so you see this technique used relatively often in the b ook.

Data scientists  call the columns in a database _features_ or _variables_.

#### Uploading small amounts of data into memory

The most convenient method that you can use to work with data is to load it directly into memory.

```
with open("Colors.txt", 'r') as open_file:
    print('Colors.txt content:\n' + open_file.read())
```

The loading process will fail if your system lacks sufficient memory to hold the data set.

You won't normally experience any problems when working with the toy datasets in the Scikit-learn library.

#### Streaming large amounts of data into memory

Some datasets will be so large that you won't be able to fit them entirely in memory at one time. In addition, you may find that some datasets load slowly because they reside on a remote site. Streaming solves both issues by enabling you to work with the data a little at a time. You download individual pieces so that you can work with just part of the data as you receive it, rather than waiting for the entire dataset to download.

```
with open("Colors.txt", 'r') as open_file:
    for observation in open_file:
        print('Reading Data: ' + observation, end="")
```

#### Generating variatiosn on image data

Sometimes you need to import and analyze image data. The source and type of the image does make a difference.

A good starting point is to simply read a local image in, obtain statistics about that image, and isplay the image onscreen, as shown in the following code:

```
import matplotlib.pyplot as plt
import matplotlib.image as img
%matplotlib inline

image = img.imread("Colorblk.jpg")
print(image.shape)
print(image.size)
plt.imshow(image)
plt.show()
```

This example begins by importing two _matplotlib_ libraries, _image_ and _pyplot_.

After the code reads the file, it begins by displaying the image _shape_ property - the number of horizontal pixels, vertical pixels, and pixel depth (the number of bits used to represent colors).

#### Sampling data in different ways

Data streaming obtains all the records from a data source.

Sampling data (retrieving records a set number of records apart, such as every fifth record).

```
n = 2
with open("Colors.txt", 'r') as open_file:
    for j, observation in enumerate(open_file):
        if j % n==0:
            print('Reading Line: ' + str(j) +
            ' Content: ' + observation, end="")
```

```
from random import random
sample_size = 0.25
with open("Colors.txt", 'r') as open_file:
    for j, observation in enumerate(open_file):
        if random()<=sample_size:
            print('Reading Line: ' + str(j) +
            ' Content: ' + observation, end="")
```

### Accessing Data in Structured Flat-File Form

In many cases, the data you need to work with won't appear within a library, such as the toy datasets in the Scikit-learn library. Real-world data usually appears in a file of some type, and a flat file presents the easiest kind of file to work with. In a flat file the data appears as a simple list of entries that you can read one at a time, if desired, into memory. Depending on the requirements for your project, you can read all or part of the file.

The pandas library used in the se ctions that follow makes it much easier to read and understand flat-file data. Classes and methods in the padas library interpret (parse) the flat-file data to make it easier to manipulate.

The least formatted and therefore easiest-to-read flat-file format is the text file. However, a text file als treats all data as strings, so you often have to convert numeric data into other forms. A comma-separated value (CSV) file provides more formatting and more informatino, but it requires a little more effort to read. At the high end of flat-file formatting are custom data formats, such as an Excel file,which contains extensive formatting and could include multiple datasets in a single file.

Working with structure data is easier because you know where each field begins and ends.

#### Reading from a text file

Text files can use a variety of storage formats. 

```
import pandas as pd
color_table = pd.io.parsers.read_table("Colors.txt")
print(color_table)
```

```
    Color  Value
0     Red      1
1  Orange      2
2  Yellow      3
3   Green      4
4    Blue      5
5  Purple      6
6   Black      7
7   White      8
```

Notice that the parser correctly interprets the first row as consisting of filed names. It numbers the records from 0 through 7. Using` read_table()`  method arguments, you can adjust how the parser interprets the input file, but the default settings usually work best. 

[pandas documentation](https://pandas.pydata.org/docs/)

[Pandas read_table()](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html)

#### Reading CSV delimited format

A CSV file provides more formatting that a simple text file. In fact, CSV files can become quite complicated. 

* A header defines each of the fields
* Fields are separated by commas.
* Records are separated by linefeeds.
* Strings are enclosed in double quotes.
* Integers and real numbers appear without double quotes.

Pands makes it easy to work with the CSV file as formatted data:

```
import pandas as pd
titanic = pd.io.parsers.read_csv("titanic.csv")
X = titanic[['age']]
print(X)
```

```
            age
0       29.0000
1        0.9167
2        2.0000
3       30.0000
4       25.0000
...         ...
1304    14.5000
1305  9999.0000
1306    26.5000
1307    27.0000
1308    29.0000

[1309 rows x 1 columns]
```

Notice that the parser of choice this time is `read_csv()`, which understands CSV files and provides you with new options for working with it. 

[Pandas read_csv()](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)

To create the output as a list, you simply change the third line of code to read 

`X = titanic[['age']].values`