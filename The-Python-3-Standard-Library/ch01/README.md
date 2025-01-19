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

#### 1.1.5 String Constants

```
# string_constants.py
import inspect
import string


def is_str(value):
    return isinstance(value, str)


for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))
```

```
$ python3 string_constants.py 
ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

ascii_lowercase='abcdefghijklmnopqrstuvwxyz'

ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

digits='0123456789'

hexdigits='0123456789abcdefABCDEF'

octdigits='01234567'

printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

whitespace=' \t\n\r\x0b\x0c'
```

### 1.2 textwrap: Formatting Text Paragraphs

The `textwrap` module can be used to format text for output in situations where pretty-printing is desired. It offers programmatic functinality simlar to the paragrap wrapping or filling features found in many text editors and word processors.

#### 1.2.1 Example Data

```
# textwrap_example.py

sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
```

#### 1.2.2 Filling Paragraphs

```
# textwrap_fill.py
import textwrap
from textwrap_example import sample_text

print(textwrap.fill(sample_text, width=50))
```

#### 1.2.3 Removing Existing Indentation

The previous example has embedded tabs and extra spaces mixed into the middle of the output, so it is not formatted very cleanly. Removing the common whitespace prefix from all of the lines in the sample text with dedent() produces better results and allows the use of docstrings or embedded multiline strings straight from Python code while removing the formatting of the code itself. The sample string has an artificial indent level introduced for illustrating this feature.

```
# textwrap_dedent.py
import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)
```