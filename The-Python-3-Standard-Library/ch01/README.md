# The Python 3 Standard Library by Example, by Doug Hellmann, ©2017

## Chapter 1: Text

The [str class](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) is the most obvious text processing tool available to Python programmers, but there are plenty of other tools in the standard library to make advanced text manipulation simple.

[string — Common string operations](https://docs.python.org/3/library/string.html#)

Programs may use [string.Template](https://docs.python.org/3/library/string.html#string.Template) as a simple way to parameterize strings beyond the features of str objects.

The [textwrap module](https://docs.python.org/3/library/textwrap.html) includes tools for formatting text from paragraphs by limiting the width of the output, adding indentation, and inserting line breaks to wrap lines consistently.

### 1.1. string: Text Constants and Templates

* string.ascii_letters
* string.ascii_lowercase
* string.ascii_uppercase
* string.digits
* string.hexdigits
* string.octdigits
* string.punctuation
* string.printable
* string.whitespace

#### 1.1.1 Functions

The function `capwords()` capitalizes all the words in a string.

```
import string
s = 'The quick brown fox jumped over the lazy dog.'
print(s)
print(string.capwords(s))
```

```
$ python3 string_capwords.py 
The quick brown fox jumped over the lazy dog.
The Quick Brown Fox Jumped Over The Lazy Dog.
```

#### 1.1.2 Templates

* \$\$ is an escape; it is replaced with a single \$.

* \$identifier names a substitution placeholder 

* \${identifier} is equivalent to $identifier.