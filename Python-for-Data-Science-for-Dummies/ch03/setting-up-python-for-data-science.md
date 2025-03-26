# Python for Data Science for Dummies, 3rd Edition, © 2024

## Chapter 3: Setting Up Python for Data Science

This book relies on Jupyter Notebook version 6.5.2 supplied with the Anaconda 3 environment (version 2023.03) that supports the Python version 3.10.9 to create the coding examples.

### Working with Anaconda

Anaconda is actually a collection of tools as described at https://www.anaconda.com/products/navigator

#### Using Jupyter Notebook

Jupyter Notebook is an Integrated Development Environment that promotes the concept of [literate programming](https://guides.nyu.edu/datascience/literate-prog) as original defined by Donalk Knuth.

```
import sys
print('Python Version:\n', sys.version)

import os
result = os.popen('conda --version').read()
print('\nAnaconda Version: \n', result)

result =os.popen('conda list notebook$').read()
print('\nJupyter Notebook Version:\n', result)
```

```
$ python3 version-check.py 
Python Version:
 3.10.9 (main, Mar  1 2023, 18:23:06) [GCC 11.2.0]

Anaconda Version: 
 conda 23.1.0


Jupyter Notebook Version:
 # packages in environment at /home/dstevenson/anaconda3:
#
# Name                    Version                   Build  Channel
notebook                  6.5.2           py310h06a4308_0  
```

#### Accessing the Anaconda Prompt

You use the Anaconda Prompt to perform many command-line tasks related to working with Jupyter Notebook. The Anaconda Prompt provides a gateway to allowing maximum flexibility withyour Python programming environment, which is a significant advantage over using Google Colab (where it's a take-it-or-leave-it proposition).

### Installing Anaconda on Windows

### Installing Anaconda on Linux

Before you can perform the install, you must download a copy of the Linux software from the Anaconda site at https://repo.anaconda.com/archive/.

On most Linux systems, you can type 

`curl https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh --output Anaconda3-2023.03-Linux-x86_64.sh`

### Downloading the Datasets and Example Code

#### Using Jupyter Notebook

The program runs in your browser, so which platform you use for development doesn't matter; as long as it has a browser, you should be OK.

On a Windows system, you choose Start -> Jupyter Notebook or Start | Anaconda3 | Jupyter.

On Linux type:

`jupyter notebook`

#### Stopping the Jupyter Notebook server

No matter how you start Jupyter Notebook (or just Notebook, as it appears in the remaidner of the book), the system generally opens a command prompt or internal window to host Notebook. This window contains a server that makes the application work. After you close the browser window when a session is complete, select the server window and press Ctrl+C or Ctrl+Break to stop the server.

To exit the conda environment, type `conda deactivate` and press Enter.

#### Defining the code repository

The code you create and use in this book will reside in a repository on your hard drive. 

##### Defining a new folder

In Jupyter Notebook (see web browser):

1. Choose New->Folder.
2. Place a check in the box next to Untitled Folder
3. Click Rename at the top of the page.
4. Type P4DS4D3 and press Enter.

#### Creating a new notebook

Every new notebook is like a file folder. You can place individual examples in the file folder, just as you would sheets of paper into a physical file folder.

Use these steps to create a new notebook.

1. Click the P4DS4D3 entry on the Home page.
2. Choose New->Python 3 (ipykernel).
3. Click Untitled on the page.
4. Type P4DS4D3_Sample and press Enter.

##### Adding notebook content

1. Choose Markdown from the drop-down list that currently contains the word Code.
   
    A Markdown cell contains documentation text.

2.  Type \# Downloading the Datasets and Example Code and click Run (the button with the right-pointing arrow on the toolbar).
3.  

##### Exporting a notebook

To perform this task, you must export your notebook from the repository to a file.
You can then send the file to someone else who will import it into their repository.

You can open this notebook by clicking its entry in the repository list.

To export this code, choose File->Download As->Notebook (.ipnyb). What you see next depends on your browser, but you generally see some sort of dialog box for saving the notebook as a file. Chrome just downloads the file to the Downloads folder.

##### Removing a notebook

Seometimes notebooks get outdated or you simply don't need to work them any longer.

Use these steps to remove the file:

1. Select the check box next to the PDS4D3_03_Sample.ipynb entry.
2. Click the Delete (trashcan) icon.

    You see a Delete notebook warning message.

3. Click Delete

    Notebook removes the notebook file from the list.

##### Importing a notebook

To use the source code from this book, you must import the downloaded files into your repository. 

1. Click Upload on the Notebook PSDS4D3 page
2. Navigate to the directory containging the files you want to import into Notebook.
3. Highlight one or more files to import and click the Open (or other, similar) button to begin the upload process.
4. Click Upload.


#### Understanding the datasets used in this book

This book uses a number of datasets, all of which appear i the Scikit-learn library.
These datasets demonstrate various ways in which you can interact with data, and you use them in the examples to perform a variety of tasks. The he following list provies a quick overview of the functdions used to import datasets into your Python code:

* fetch_openml(): An open repository for machine learnign data and experiments. Anyone can upload open datasets to allow access to them.
* fetch_california_housing(): Regress analysis with the California housing dataset.
* Datasets: https://archive.ics.uci.edu/datasets
* https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data Analysis with the German Credit dataset described at 
* Palmer Penguins https://archive.ics.uci.edu/dataset/690/palmer+penguins-3
* Movie Lens dataset: https://files.grouplens.org/datasets/movielens/