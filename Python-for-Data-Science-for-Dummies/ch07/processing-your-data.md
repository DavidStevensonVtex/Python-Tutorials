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

### Manipulating Categorical Variables

In data science, a _categorical variable_ is one that has a specific value from a limited selection of values. The number of values is usually fixed. Many developers will know categorical variables by the moniker _enumerations_. Each of the potential values that a categorical variable can assume is a _level_.

To understand how categorical variables work, say that you have a variable expressing the color of an object, such as a car, and that the user can select blue, red or green. To express the car's color in a way that computers can represent and effectively compute, an application assigns each color a numerical value, so blue is 1, red is 2, and green is 3. Normally, when you print each color, you see the value rather than the color.

If you use [pandas.DataFrame](https://pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.html), you can still see the symbolic value (blue, red, and green), even though the compuetr stores it as a numeric value.

#### Checking Your Version of pandas

The categorical variable examples in this section depend on your having a minimum version of pandas 1.5.0 installed on your system.

```
import pandas as pd
print(pd.__version__)
```

```
1.5.3
```

```
$ pip show pandas
Name: pandas
Version: 1.5.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: The Pandas Development Team
Author-email: pandas-dev@python.org
License: BSD-3-Clause
Location: /home/dstevenson/anaconda3/lib/python3.10/site-packages
Requires: numpy, python-dateutil, pytz
Required-by: datashader, holoviews, hvplot, seaborn, statsmodels, xarray
```

#### Creating Categorical Variables

Categorical variables have a specific number of values, which makes them incredibly valuable in performing a number of data science tasks.

```
import pandas as pd

car_colors = pd.Series(['Blue', 'Red', 'Green'],
                       dtype='category')

car_data = pd.Series(
    pd.Categorical(
        ['Yellow', 'Green', 'Red', 'Blue', 'Purple'], 
        categories=car_colors, ordered=False))

find_entries = pd.isnull(car_data)

print(car_colors)
print(f"\n{car_data}")
print(f"\n{find_entries[find_entries == True]}")
```

The example begins by creating a categorical varialbe, `car_colors`. The variable contains the values _Blue_, _Red_, and _Green as colors that are acceptable. Notice that you must specify a _dtype_ property value of _category_.

The next step is to create another series. This one uses a list of actual car colors, named `car_data`, as input. Not all the car colors match the predefined acceptable values. When this problem occurs, pandas otuputs Not a Number(NaN) instead of the car color.

In this case, you ask pandas which entries are null using _isnull()_ and place them in `find_entries`. You can then output just those entries that are actually null.

```
0     Blue
1      Red
2    Green
dtype: category
Categories (3, object): ['Blue', 'Green', 'Red']

0      NaN
1    Green
2      Red
3     Blue
4      NaN
dtype: category
Categories (3, object): ['Blue', 'Green', 'Red']

0    True
4    True
dtype: bool
```

#### Renaming Levels

There are times when the naming of the categories you use is inconvenient or otherwise wrong for a particular need. Fortunately, you can rename the categories as needed using the technique shown in the following example.

```
import pandas as pd

car_colors = pd.Series(['Blue', 'Red', 'Green'],
                       dtype='category')
car_data = pd.Series(
    pd.Categorical(
        ['Blue', 'Green', 'Red', 'Blue', 'Red'],
        categories=car_colors, ordered=False))

car_data = car_data.cat.rename_categories(
    ["Purple", "Yellow", "Mauve"])

print(car_data)
```

All you really need to do is set the _cat_ property to a new value, as shown. Here is the output from this example.

```
0    Purple
1    Yellow
2     Mauve
3    Purple
4     Mauve
dtype: category
Categories (3, object): ['Purple', 'Yellow', 'Mauve']
```

#### Combining Levels

A particular categorical level may be too small to offer significant data for analysis. Perhaps there are only a few of the values, which may not be enough to create a statistical difference. In this case, combining several small categories may offer better analysis results.

```
import pandas as pd

car_colors = pd.Series(['Blue', 'Red', 'Green'],
    dtype='category')
car_data = pd.Series(
    pd.Categorical(
       ['Blue', 'Green', 'Red', 'Green', 'Red', 'Green'],
       categories=car_colors, ordered=False))

car_data = car_data.cat.set_categories(
    ["Blue", "Red", "Green", "Blue_Red"])
print(car_data.loc[car_data.isin(['Red'])])
car_data.loc[car_data.isin(['Red'])] = 'Blue_Red'
car_data.loc[car_data.isin(['Blue'])] = 'Blue_Red'

car_data = car_data.cat.set_categories(
    ["Green", "Blue_Red"])
print(f"\n{car_data}")
```

What this example shows you is that there is only one _Blue_ item and only two _Red_ items, but there are three _Green_ items, which places _Green_ in the majority.

Combining _Blue_ and _Red_ together is a two-step process. First, you add the `Blue_Red` category to `car_data`. Then you change the _Red_ and _blue_ entrioes to `Blue_Red`, which creates a combined category. As a final step, you can remove the unneeded categories.

```
2    Red
4    Red
dtype: category
Categories (4, object): ['Blue', 'Red', 'Green', 'Blue_Red']

0    Blue_Red
1       Green
2    Blue_Red
3       Green
4    Blue_Red
5       Green
dtype: category
Categories (2, object): ['Green', 'Blue_Red']
```

Notice that there are now three `Blue_Red` entries and three _Green_ entires. The _Blue_ and _Red_ categories are no longer in use. The resultis thatthe levels are now combined as expected.

### Dealing with Dates in Your Data

Dates can present problems in data. For one thing, dates are stored as numeric values. However, the precise value of the number depends on the representation for the particular platform and could even depend on users' preferences.

[Excel users can choose to start dates in 1900 or 1904](https://learn.microsoft.com/en-us/office/troubleshoot/excel/1900-and-1904-date-system). The numeric encoding for each is different so the samedate can have two numeric values depending on the starting date.

Creating a time v alue format that represents a value the user can understand is hard. For example, you may need to use Greenwich Mean Time (GMT) in some situations but a local time zone in others.

#### Formatting date and time values

Pyuthon provides two common methods of formatting date and time. The first technique is to call `str()`, which simply turns a datatime value into a string without any formatting. The `strftime()` function requires more work because you must define how you want the _datetime_ value to appear after conversion.

[Python strftime cheatsheet](https://strftime.org/)

```
import datetime as dt

now = dt.datetime.now()

print(str(now))
print(now.strftime('%a, %d %B %Y'))
```

```
2025-04-11 13:55:07.315438
Fri, 11 April 2025
```

#### Using the right time transformation

Time zones and differences in local time can cause all sorts of problems when performing analysis. For that matter, some times of calculatiosn simply require a time shift in order to get the right results.


```
import datetime as dt

now = dt.datetime.now()
timevalue = now + dt.timedelta(hours=2)

print(now.strftime('%H:%M:%S'))
print(timevalue.strftime('%H:%M:%S'))
print(timevalue - now)
```

```
13:57:43
15:57:43
2:00:00
```

### Dealing with Missing Data

Sometimes the data you receive is missing information in specific fields.
For example, a customer record may be missing an age.

Having a strategy for dealing with missing data is important.

#### Finding the missing data

The following code shows how you can obtain a listing of missing values without too much effort.

```
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, np.NaN, 5, 6, None])

print(s.isnull())
print(f"\n{s[s.isnull()]}")
```

isnull() is a function in pandas that detects missing values in a Series object. It returns a boolean Series of the same shape as the input Series, where True indicates a missing value (NaN) and False indicates a non-missing value. isna() is an alias for isnull() and performs the same operation.

To enable the interpretation of square brackets [] with a Python class, the `__getitem__` method needs to be defined within the class. This special method allows instances of the class to behave like sequences (e.g., lists, tuples) or mappings (e.g., dictionaries) when accessed using square brackets.


```
0    False
1    False
2    False
3     True
4    False
5    False
6     True
dtype: bool

3   NaN
6   NaN
dtype: float64
```

#### Encoding missingness

After you figure out that your dataset is missing information, you need to consider what to do about it. The three possibilities are:

* to ignore the issue
* fill in the missing items
* or remove (drop) the missing entries from the dataset

```
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, np.NaN, 5, 6, None])

print(s.fillna(int(s.mean())))
print(f"\n{s.dropna()}")
```

The fillna() method replaces NaN (Not a Number) values in a Series with a specified value or using a specified method.

In pandas, a Series is a one-dimensional labeled array capable of holding data of any type. The mean() method, when applied to a pandas Series, calculates the arithmetic mean (average) of its elements. It sums all the values in the Series and divides by the number of non-missing values. 

dropna is a function in the pandas library used to remove missing values (NaNs) from a Series. It returns a new Series with the missing values removed. The original Series remains unchanged unless the inplace parameter is set to True.

```
0    1.0
1    2.0
2    3.0
3    3.0
4    5.0
5    6.0
6    3.0
dtype: float64

0    1.0
1    2.0
2    3.0
4    5.0
5    6.0
dtype: float64
```

Working with a series is straightforward because the dataset is so simple. When working with a DataFrame, however, the problem becomes significantly more complicated. You still have the option of dropping the entire row.

#### Imputing missing data

The previous section hints at the process of imputing missing data (ascribing characteristics based on how the data is used). The technique you use depends on the sort of data you're working with.

```
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

s = pd.DataFrame([1, 2, 3, np.nan, 5, 6, np.nan])

imp = SimpleImputer(missing_values=np.nan,
                    add_indicator=True,
                    strategy='mean')

imp.fit(s)
x = imp.transform(s)
print(x)
```

In this example, s is missing some values. The code creates an Imputer to replace these missing values. The `missing_values` parameter defines what to look for, which is `np.nan`. The add_indicator parameter creates a new binary featuer that will mark the imputed values, which is incredibly useful for many meachine learning models to show both the original values and the manipulated ones.

[Simple Imputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)

Before you can impute anything you must provide statistics for the Imputer to use by calling `fit()`. The code then calls `transform()` on s to fill in the missing values.

What does sklearn fit() do?

The fit method is a fundamental part of the Scikit-Learn library. It's used to train a machine learning model on a dataset. Specifically, the fit method takes in a dataset (typically represented as a 2D array or matrix) and a set of labels, and then fits the model to the data.

```
[[1.  0. ]
 [2.  0. ]
 [3.  0. ]
 [3.4 1. ]
 [5.  0. ]
 [6.  0. ]
 [3.4 1. ]]
```

### Slicing and Dicing: Filtering and Selecting Data

You may not need to work with all the data in a dataset. In fact, looking at just one particular column may be beneficial, such as age, or a set of rows with a significant amount of information.

You perform two steps to obtain just the data you need to perform a particular task:

1.  Filter rows to create a subset of the data that meets the criterion you select.
2.  Select data columns that contain the data you need to analyze.

The act of slicing and dicing data, gives you a subset of the data suitable for analysis.

#### Slicing rows

Slicing can occur in multiple ways when working with data, but the technique of interest in this section is to slice data from a row of 2-D or 3-D data. A 2-D array may contain temperatures (x axis) over a specific time frame (y axis). Slicing a row would mean seeing the temperatures at a specific time. 

A 3-D array may include an axiss for place (x-axis), product (y axis), and time (z axis), so that you can see sales over time. Perhaps you wantto track whether sales of an item are increasing, and specifically where they are increasing. Slicing a row would mean seeing all the sales for one specific product for all locations at any time.

```
x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9],],
             [[11,12,13], [14,15,16], [17,18,19],],
             [[21,22,23], [24,25,26], [27,28,29]]])
x[1]
```

```
array([[11, 12, 13],
       [14, 15, 16],
       [17, 18, 19]])
```
