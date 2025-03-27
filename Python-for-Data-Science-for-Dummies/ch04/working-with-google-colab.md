# Python for Data Science for Dummies, 3rd Edition, © 2024

## Chapter 4: Working with Google Colab

Colaboratory, or [Colab](https://colab.research.google.com/notebooks/welcome.ipynb) for short, is a free Google cloud-based service that replaces Jupyter Notebook in the cloud. You don't have to install anything on your system to use it. In most respects, you use Colab as you would a desktop installation of Jupyter Notebook.

### Defining Google Colab

Google Colab is the cloud version of Notebook. It even uses IPython (the previous name for Jupyter) Notebook (.ipynb) file for the site.  That's right: You're viewing a Notebook right there in your browser.

#### Understanding what Google Colab does

You use it to write and run code, create its associated documentation, and display graphics, just as you do with Notebook. There are small differences between Google Colab and Jupyter Notebook.

Notebook is a localized application.

Colab enables you to fully interact with your notebook files using GitHub as a repository. In fact, Colab supports a number of online storage options, so you can regard Colab as your online partner in creating Python code.

The other reason that you really need to know about Colab is that you can use it with your alternative device. During the writing process, some of the example code was tested on an Android-based tablet. The target tablet has Chrome installed and executes the code well enough to follow the examples. All this said, you likely won't want to try to write code using a tablet.

Google Colab generally doesn't work with browsers other than Chrome or Firefox.

#### Considering the online coding difference

For the most part, you use Colab just as you would Notebook. However, some features work differently. For example, to execute the code within a cell, you select that cell and click the Run button (right-facing arrow) for that cell. The current cell reamins selected, which means that you msut actually initiate the selection of the next cell as a separate action.

You can upload code from your local drive as desired and then save it to a Google Drive or GitHub. The code becomes accessible from any device at this point by accessing those same sources. All you need to do is load Colab to access it.

All this flexibility comes at the price of speed and ergonomics. In reviewing the various options, a local copy of Notebook generally executes the code in this book faster than a copy of Colab using any of the available configurations (even when working with a local copy of the .ipynb file). So, you trade speed for flexibility when working with Colab.

When workign with Colab, you have options to downlaod your source files only as .ipynb or .py files. Colab doesn't include all the other download options, inclduing (but not limited to) HTML, LaTeX, and PDF. Consequently, your options for creating presentations from the online content are also limited to some extent.

A Markdown cell in Notebook is a Text cell in Colab.