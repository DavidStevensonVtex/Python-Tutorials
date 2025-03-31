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