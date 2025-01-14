# [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

[The Python Standard Library](https://docs.python.org/3/library/)

## [11. Brief Tour of the Standard Library — Part II](https://docs.python.org/3/tutorial/stdlib2.html)

This second tour covers more advanced modules that support professional programming needs. These modules rarely occur in small scripts.

### 11.1. Output Formatting

The reprlib module provides a version of repr() customized for abbreviated displays of large or deeply nested containers:

```
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```


The pprint module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter. When the result is longer than one line, the “pretty printer” adds line breaks and indentation to more clearly reveal data structure:

```
>>> import pprint
'green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
>>> 
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

The textwrap module formats paragraphs of text to fit a given screen width:

```
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
>>> 
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```
The locale module accesses a database of culture specific data formats. The grouping attribute of locale’s format function provides a direct way of formatting numbers with group separators:

The following example may require a more up to date version of Python than 3.8:

```
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
252'
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format_string("%d", x, grouping=True)
locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'], x), grouping=True)Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.8/locale.py", line 608, in setlocale
    return _setlocale(category, locale)
locale.Error: unsupported locale setting
>>> 'English_United States.1252'
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format_string("%d", x, grouping=True)
'1234567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'], x), grouping=True)
'1234567.8000000000465661287307739257812500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
>>> 
```
