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

#### Accessing the Anaconda Prompt

You use the Anaconda Prompt to perform many command-line tasks related to working with Jupyter Notebook. The Anaconda Prompt provides a gateway to allowing maximum flexibi9lity withyour Python programming environment, which is a significant advantage over using Google Colab (where it's a take-it-or-leave-it proposition).

