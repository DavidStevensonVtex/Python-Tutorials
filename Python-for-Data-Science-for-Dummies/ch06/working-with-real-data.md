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
