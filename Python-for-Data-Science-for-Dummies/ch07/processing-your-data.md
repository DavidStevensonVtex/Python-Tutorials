# Python for Data Science for Dummies, 3rd Edition, © 2024

## Chapter 7: Processing Your Data

The characteristics, content, type, and other elements that define your data in its entirety forms the data _shape_. The shape of your data determines the kinds of tasks you can perform with it.

You rely on functions and algorithms to shape your data.

Note that shaping data doesn't mean changing its value. Think more allong the lines of rearranging the data so that you can work with it in an easier manner.

The goal of some types of data shaping is to create a larger dataset. In many cases, the data you need to perform an analysis doesn't appear in a single database or in a particular form. You need to shape the data and then combine it so that you have a single dataset in a known format before you can begin the analysis.

### Juggling between NumPy and pandas

There is no question that you need NumPy at all times. The pandas library is actually built on top of NumPy. However, you do need to make a choice between NumPy and pandas when performing tasks. You need the low-level functionality of NumPy to perform some tasks, but pandas makes things so much easier that you want to use it as often as possible.

#### Knowing when to use NumPy

Developers built pandas on top of NumPy. As a result, every task you perform using pandas also goes through NumPy. [To obtain the benefits of pandas, you pay a performance penalty in most cases](https://towardsdatascience.com/speed-testing-pandas-vs-numpy-ffbf80070ee7).

The speed issue may not be a concern at times, but when speed is essential, NumPy is always the better choice.

#### Knowing when to use pandas

You use pandas to make writing code easier and faster. Because pandas does a lot of the work for you, you could make a case for saying that using pandas also reduces the potential for coding errors. The essential consideration, though, is that the pandas library provides rich time-series functionality, data alignment, NA-friendly statistics, and _groupby()_, _merge()_, and _join()_ methods. Normally, you need to code these features when using NumPy, which means you keep reinventing the wheel.

pandas can be useful for performing such tasks as _binning_ and workign with a _dataframe_ (a two-dimensional labeled data structure with columns that can potentially contain different data types) so that you can calculate statistics on it.

In Chapter 9, you discover how to perform both discretization and binning.

Chaper 13 shows actual binning examples, such as obtaining a frequency for each categorical variable of a data set. In fact, many of the examples in Chapter 13 don't work without binnning.

#### It's All in the Preparation

The majority of a data scientist's time is actually spent preparing data becauset he data is seldom in any order to actually perform analysis. To prepare data for use, a data scientist must:

* Get the data
* Aggregate the data
* Create data subsets
* Clean the data
* Develop a single dataset by merging various datasets together

### Validating Your Data

You must validate your data before you use it to ensure that the data is at least close to what you expect it to be.

What validation does is ensure that you can perform an analysis of the data and reasonably expect that analysis to succeed.

#### Figuring out what's in your data

Finding duplicates is important because you end up

* Spending more computational time to process duplicates, which slows your algorithms down.

* Obtaining false results because duplicates implicitly overweight the results.

```
from lxml import objectify
import pandas as pd

xml = objectify.parse(open('XMLData2.xml'))
root = xml.getroot()
df = pd.DataFrame(columns=('Number', 'String', 'Boolean'))

for i in range(0,4):
    obj = root.getchildren()[i].getchildren()
    row = dict(zip(['Number', 'String', 'Boolean'],
                   [obj[0].text, obj[1].text,
                    obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    row_s = row_s.to_frame().transpose()
    df = pd.concat([df, row_s])

search = pd.DataFrame.duplicated(df)
print(df)
print(f"\n{search[search == True]}")
```

This example shows how to find duplicate rows.

This example begins by reading the data file into memory.
It then places the data into a _DataFrame_.

Your data is corrupted because it contains a duplicate row.
However, you can get rid of the duplicated row by searching for it.
The duplicated rows contain a Rtue next to their row number.

```
  Number  String Boolean
0      1   First    True
1      2  Second   False
2      3   Third    True
3      3   Third    True

3    True
dtype: bool
```

#### Removing duplicates

To get a clean dataset, you want to remove the duplicates from it. 

```
from lxml import objectify
import pandas as pd

xml = objectify.parse(open('XMLData2.xml'))
root = xml.getroot()
df = pd.DataFrame(columns=('Number', 'String', 'Boolean'))
for i in range(0,4):
    obj = root.getchildren()[i].getchildren()
    row = dict(zip(['Number', 'String', 'Boolean'],
                   [obj[0].text, obj[1].text,
                    obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    row_s = row_s.to_frame().transpose()
    df = pd.concat([df, row_s])

print(df.drop_duplicates())
```

```
  Number  String Boolean
0      1   First    True
1      2  Second   False
2      3   Third    True
```

#### Creating a data map and data plan

You need to know about your dataset -- that is, how it looks statistically. A _data map_ is an overview of the dataset. You use it to spot potential problems in your data, such as

* Redundant variables
* Possible errors
* Missing values
* Variable transformations

Checking for these problems goes into a _data plan_, which is a list of tasks you have to perform to ensure the integrity of your data. The following example shows a data map, A, with two datasets, B and C:

```
import pandas as pd
pd.set_option('display.width', 55)

df = pd.DataFrame({'A': [0,0,0,0,0,1,1],
                   'B': [1,2,3,5,4,2,5],
                   'C': [5,3,4,1,1,2,3]})

a_group_desc = df.groupby('A').describe()
print(a_group_desc)
```

In this case, the data map uses 0s for the first series and 1s for the second series. 
The _groupby()_ function places the datasets, B and C, into groups.
To determine whether the data map is viable, you obtain statistics using _describe()_.
What you end up with is a dataset B with two series 0 and 1 and a dataset C also with series 0 and 1, as shown in the following output.

```
      B                                            \
  count mean       std  min   25%  50%   75%  max   
A                                                   
0   5.0  3.0  1.581139  1.0  2.00  3.0  4.00  5.0   
1   2.0  3.5  2.121320  2.0  2.75  3.5  4.25  5.0   

      C                                            
  count mean       std  min   25%  50%   75%  max  
A                                                  
0   5.0  2.8  1.788854  1.0  1.00  3.0  4.00  5.0  
1   2.0  2.5  0.707107  2.0  2.25  2.5  2.75  3.0  
```

These statistics tell you about the two dataset series. The breakup of the two datasets using specific cases is the _data plan_. As you can see, the statistics tell you that this data plan may not be viable because some statistics are relatively far apart.

The default output from _describe()_ shows the data unstacked (printed horizontally).
Unfortunately, the unstacked data can print out with an unfortunate break, making it very hard to read. To keep this form happening, you set the width you want to use for the data by calling _pd.set_option('display.width', 55)_. [You can set a number of pandas options this way](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html).

Although the unstacked data is relatively easy to read and compare, you may prefer a more compact presentation. In this case, you can stack the data using the following code:

```
stacked = a_group_desc.stack()
print(stacked)
```

```
                B         C
A                          
0 count  5.000000  5.000000
  mean   3.000000  2.800000
  std    1.581139  1.788854
  min    1.000000  1.000000
  25%    2.000000  1.000000
  50%    3.000000  3.000000
  75%    4.000000  4.000000
  max    5.000000  5.000000
1 count  2.000000  2.000000
  mean   3.500000  2.500000
  std    2.121320  0.707107
  min    2.000000  2.000000
  25%    2.750000  2.250000
  50%    3.500000  2.500000
  75%    4.250000  2.750000
  max    5.000000  3.000000
```

You may not want all the data that _describe()_ provides. Perhaps you really just want to see the number of items in each series and their mean. 

```
print(a_group_desc.loc[:,(slice(None),['count','mean']),])
```

```
      B          C     
  count mean count mean
A                      
0   5.0  3.0   5.0  2.8
1   2.0  3.5   2.0  2.5
```