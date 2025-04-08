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