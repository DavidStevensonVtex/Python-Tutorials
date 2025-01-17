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

#### 1.1.3 Advanced Templates

Advanced usage: you can derive subclasses of Template to customize the placeholder syntax, delimiter character, or the entire regular expression used to parse template strings. To do this, you can override these class attributes:

* delimiter – The default value is $. Note that this should not be a regular expression

* idpattern – This is the regular expression describing the pattern for non-braced placeholders. The default value is the regular expression (?a:[_a-z][_a-z0-9]*). 

* braceidpattern – This is like idpattern but describes the pattern for braced placeholders. Defaults to None which means to fall back to idpattern. Added in version 3.7.

* flags 

#### 1.1.4 Formatter

The [Formatter class](https://docs.python.org/3/library/string.html#string.Formatter) implements the same layout specification language as the [format() method](https://docs.python.org/3/library/stdtypes.html#str.format) of `str`.

[Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)