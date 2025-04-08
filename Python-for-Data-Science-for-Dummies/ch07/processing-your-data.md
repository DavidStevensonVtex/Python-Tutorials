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
