# NumPy Getting Started

## Installation of NumPy

If you have Python and PIP already installed on a system, then installation of NumPy is very easy.

Install it using this command:

`pip install numpy`

## Import NumPy

Once NumPy is installed, import it in your applications by adding the import keyword:

`import numpy`

Now NumPy is imported and ready to use.

```
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
```

## NumPy as np

NumPy is usually imported under the np alias.

alias: In Python alias are an alternate name for referring to the same thing.

Create an alias with the as keyword while importing:

`import numpy as np`

Now the NumPy package can be referred to as np instead of numpy.

## Checking NumPy Version
The version string is stored under __version__ attribute.

```
import numpy as np

print(np.__version__)
```