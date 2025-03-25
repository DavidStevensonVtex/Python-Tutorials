# Python for Data Science for Dummies, 3rd Edition, © 2024

## Chapter 2: Introducing Python's Capabilities and Wodners

### Working with Python

#### Contributing to Data Science

[Understanding How Python is Used in Data Science](https://www.datasciencegraduateprograms.com/python/)

Here are the reasons [ForecastWatch.com](https://forecastwatch.com/) chose Python:

* Library support: [Python Success Stories](https://www.python.org/about/success/forecastwatch/)
* Parallel Processing
* Data access: Forecast.com relies on a MySQL database accessed through the [MySQL for Python](https://sourceforge.net/projects/mysql-python/) library. [MySQL with Python 3.x - mysqlclient](https://pypi.org/project/mysqlclient/).
* Data display

#### Getting a taste of the language

This book relies on a much better environment, Jupyter Notebook (or Google Colab as an alternative).

#### Understanding the need for indentation

One of the most common errors that developers encounter is not providing the proper indentation for code.

#### Working with Jupyter Notebook and Google Colab

The vast majority of this book relies on Jupyter Notebook (with code also tested using Google Colab), which is part of the Anaconda installation you create in Chapter 3.

### Performing Rapid Prototyping and Experimentation

Python is all about creating applications quickly and then experimenting with them to see how things work. The act of creating an application design in code without necessarily filling in all the details is _prototyping_.

Data science doesn't rely on static solutions. You may have to try multiple solutiosn to find the particular solutin that works best.

The following list shows the phases in the order in which you normally perform them.

1. Building a data pipeline.
2. Performing the required shaping. The shape of the data -- the way in which it appears and its characteristics (such as data type), is important in performing analysis.
3. Analyzing the data. When analyzing data, you seldom employ a single algorithm and call it good enough. You can't know which algorithm will produce the most useful results at the outset.
4. Presenting a result. A picture is worth a thousand words, or so they say. Using the MATLAB-like plotting functionality provided by the Matplotlib library, you can create multiple presentations of the same data, each of which describes the data graphically in different ways.

[MATLAB](https://www.mathworks.com/products/matlab.html) is a widely used mathematical modeling program; see MATLAB For Dummies, 2nd Edition.

### Considering the Speed of Execution

In general, the following factors control the speed of execution for your data science application:

* Dataset size. When it comes to making business decisiosn, larger is better in most situations. Underestimating the effect of dataset size is deadly in data science applications, especially those that need to operate in real time (such as self-driving cars).
* Loading technique. Working with data in memory is always faster than working with data stored on disk. Accessing local data is always faster than accessing it across a network. Performing data science tasks that rely on internet access through web services is probably the slowest method of all.
* Coding style. To create fast data science applications, you must use best-of-method coding techniques.
* Machine capability. Running data science applications on a memory constrained system with a slower processor is an extremely painful process akin to sitting in the dentist's chair for a root canal without Novocain. Given that data science applications are both processor and disk bound, you can't really cut corners in any area and expect great results.
* Analysis algorithm. The algorithm you use determines the kidn of result you obtain and controls execution speed. You must experiment to find the best algorithm for your particular dataset.

### Visualizing Power

`pip install scikit-learn`

```
$ python3
>>> from sklearn.utils import Bunch
>>> items = dir(Bunch)
>>> for item in items:
...     if 'key' in item:
...             print(item)
... 
fromkeys
keys
```

Scikit-learn datasets appear within _bunches_ (a bunch is a kind of data structure).

Before you can work with a dataset, you must provide access to it in the local environment.
The following code shows the import process and demonstrates how you can use the _keys()_ function to display a list of keys that you can use to access data within the dataset.

```
$ python3
>>> from sklearn.datasets import fetch_california_housing
>>> housing = fetch_california_housing()
>>> print(housing.keys())
dict_keys(['data', 'target', 'frame', 'target_names', 'feature_names', 'DESCR'])
>>> 
>>> print(housing.feature_names)
['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
```

### Using the Python Ecosystem for Data Science

#### Accessing scientific tools using SciPy

The [SciPy stack](http://www.scipy.org/) contains a host of other libraries that you can also download separately. These libraries provide support for matematics, science, and engineering. 
These libraries are:

* NumPy
* SciPy
* Matplotlib
* Jupyter
* Sympy
* pandas

The SciPy library itself focuses on numerical routines, such as routines for numerical integration and optimization. SciPy is a general-purpsoe library that provides functionality for multiple problem domains. It also provides support for domain-specific libraries, such as Scikit-learn, Scikit-image, and statsmodels.

#### Performing fundamental scientific computing using NumPy

The [NumPy library](http://www.numpy.org/) provides the means for performing n-dimensional array manipulation, which is critical for data science work. The California Housing dataset used in the examples in Chapters 1 and 2 is ane example of an n-dimensional array, and you couldn't easily access it without NumPy functions that include support for linear algebra, Fourier transform, and random number generation ([see the listing of functions](http://docs.scipy.org/doc/numpy/reference/routines.html))

* [NumPy user guide](https://numpy.org/doc/stable/user/index.html)

#### Performing data analysis using pandas

The [pandas library](http://pandas.pydata.org/) provides support for data structures and data analsysis tools. The library is optimized to perform data science tasks especially fast and efficiently. The basic principle behind pandas is to provide data analysis and modeling support for Python that is similar to other languages, such as R.

### Implementing machine learning using Scikit-learn

The [Scikit-learn library](http://scikit-learn.org/stable/) is one of a number of Scikit libraries that build on the capabilities of NumPy and SciPy to allow Python developers to perform domain-specific tasks. In this case, the library focuses on data mining and data analysis.

It provides access to the following sorts of functionality:

* Classification
* Regression
* Clustering
* Dimensionality reduction
* Model selection
* Preprocessing

You can assume that Scikit-learn is the most important library for the book (even though it relies on other libraries to perform its work).


