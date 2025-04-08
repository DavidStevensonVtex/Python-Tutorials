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