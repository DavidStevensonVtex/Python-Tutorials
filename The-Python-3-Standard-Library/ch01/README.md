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

### [1.2 textwrap: Formatting Text Paragraphs](https://pymotw.com/3/textwrap/index.html)

The `textwrap` module can be used to format text for output in situations where pretty-printing is desired. It offers programmatic functinality simlar to the paragrap wrapping or filling features found in many text editors and word processors.

[textwrap — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html)

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

#### 1.2.4 Combining Dedent and Fill

Next, the dedented text can be passed through fill() with a few different width values.

```
# textwrap_fill_width.py
import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print('{} Columns:\n'.format(width))
    print(textwrap.fill(dedented_text, width=width))
    print()
```

```
$ python3 textwrap_fill_width.py
45 Columns:

The textwrap module can be used to format
text for output in situations where pretty-
printing is desired.  It offers programmatic
functionality similar to the paragraph
wrapping or filling features found in many
text editors.

60 Columns:

The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
```

#### 1.2.5 Indenting Blocks

Use the indent() function to add consistent prefix text to all of the lines in a string. This example formats the same example text as though it was part of an email message being quoted in the reply, using > as the prefix for each line.

```
# textwrap_indent.py
import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '> ')

print('Quoted block:\n')
print(final)
```

The block of text is split on newlines, the prefix is added to each line that contains text, and then the lines are combined back into a new string and returned.


```
$ python3 textwrap_indent.py 
Quoted block:

>  The textwrap module can be used to format text
> for output in situations where pretty-printing is
> desired.  It offers programmatic functionality
> similar to the paragraph wrapping or filling
> features found in many text editors.

> Second paragraph after a blank line.
```

To control which lines receive the new prefix, pass a callable as the predicate argument to indent(). The callable will be invoked for each line of text in turn and the prefix will be added for lines where the return value is true.

```
# textwrap_indent_predicate.py
import textwrap
from textwrap_example import sample_text


def should_indent(line):
    print('Indent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0


dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, 'EVEN ',
                        predicate=should_indent)

print('\nQuoted block:\n')
print(final)
```

```
$ python3 textwrap_indent_predicate.py 
Indent ' The textwrap module can be used to format text\n'?
Indent 'for output in situations where pretty-printing is\n'?
Indent 'desired.  It offers programmatic functionality\n'?
Indent 'similar to the paragraph wrapping or filling\n'?
Indent 'features found in many text editors.'?

Quoted block:

EVEN  The textwrap module can be used to format text
for output in situations where pretty-printing is
EVEN desired.  It offers programmatic functionality
EVEN similar to the paragraph wrapping or filling
EVEN features found in many text editors.
```

#### 1.2.6 Hanging Indents

In the same way that it is possible to set the width of the output, the indent of the first line can be controlled independently of subsequent lines.

```
# textwrap_hanging_indent.py
import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=50,
                    ))
```

This makes it possible to produce a hanging indent, where the first line is indented less than the other lines.

```
$ python3 textwrap_hanging_indent.py
The textwrap module can be used to format text for
    output in situations where pretty-printing is
    desired.  It offers programmatic functionality
    similar to the paragraph wrapping or filling
    features found in many text editors.
```

#### 1.2.7 Truncating Long Text

To truncate text to create a summary or preview, use shorten(). All existing whitespace, such as tabs, newlines, and series of multiple spaces, will be standardized to a single space. Then the text will be truncated to a length less than or equal to what is requested, between word boundaries so that no partial words are included.

```
# textwrap_shorten.py
import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)

print('Original:\n')
print(original)

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)

print('\nShortened:\n')
print(shortened_wrapped)
```

If non-whitespace text is removed from the original text as part of the truncation, it is replaced with a placeholder value. The default value [...] can be replaced by providing a placeholder argument to shorten().

```
$ python3 textwrap_shorten.py
Original:

 The textwrap module can be used to format text
for output in situations where pretty-printing is
desired.  It offers programmatic functionality
similar to the paragraph wrapping or filling
features found in many text editors.

Shortened:

The textwrap module can be used to format text for
output in situations where pretty-printing [...]
```

### 1.3 [re: Regular Expressions](https://docs.python.org/3/library/re.html)

*Regular expressions* are text matching patterns described with a formal syntax. The patterns are interpreted as a set of instructions, which are then executed with a string as input to produce a matching subset or modified version of the original. The term “regular expressions” is frequently shortened to “regex” or “regexp” in conversation. Expressions can include literal text matching, repetition, pattern composition, branching, and other sophisticated rules. A large number of parsing problems are easier to solve with a regular expression than by creating a special-purpose lexer and parser.

Regular expressions are typically used in applications that involve a lot of text processing. For example, they are commonly used as search patterns in text editing programs used by developers, including vi, emacs, and modern IDEs. They are also an integral part of Unix command-line utilities such as sed, grep, and awk. Many programming languages include support for regular expressions in the language syntax (Perl, Ruby, Awk, and Tcl). Other languages, such as C, C++, and Python, support regular expressions through extension libraries.

Multiple open source implementations of regular expressions exist, each sharing a common core syntax but with different extensions or modifications to their advanced features. The syntax used in Python’s re module is based on the syntax used for regular expressions in Perl, with a few Python-specific enhancements.

Note

Although the formal definition of “regular expression” is limited to expressions that describe regular languages, some of the extensions supported by re go beyond describing regular languages. The term “regular expression” is used here in a more general sense to mean any expression that can be evaluated by Python’s re module.

#### 1.3.1 Finding Patterns in Text

The most common use for re is to search for patterns in text. The search() function takes the pattern and text to scan, and returns a Match object when the pattern is found. If the pattern is not found, search() returns None.

Each Match object holds information about the nature of the match, including the original input string, the regular expression used, and the location within the original string where the pattern occurs.

```
# re_simple_match.py
import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))
```

The start() and end() methods give the indexes into the string showing where the text matched by the pattern occurs.

```
Found "this"
in "Does this text match the pattern?"
from 5 to 9 ("this")
```

#### 1.3.2 Compiling Expressions

Although re includes module-level functions for working with regular expressions as text strings, it is more efficient to compile the expressions a program uses frequently. The compile() function converts an expression string into a RegexObject.

```
# re_simple_compiled.py
import re

# Precompile the patterns
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]
text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')
```

The module-level functions maintain a cache of compiled expressions, but the size of the cache is limited and using compiled expressions directly avoids the overhead associated with cache lookup. Another advantage of using compiled expressions is that by precompiling all of the expressions when the module is loaded, the compilation work is shifted to application start time, instead of occurring at a point where the program may be responding to a user action.

```
$ python3 re_simple_compiled.py 
Text: 'Does this text match the pattern?'

Seeking "this" -> match!
Seeking "that" -> no match
```

#### 1.3.3 Multiple Matches

So far, the example patterns have all used search() to look for single instances of literal text strings. The findall() function returns all of the substrings of the input that match the pattern without overlapping.

```
# re_findall.py
import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))
```

This example input string includes two instances of ab.

```
$ python3 re_findall.py 
Found 'ab'
Found 'ab'
```

The finditer() function returns an iterator that produces Match instances instead of the strings returned by findall().

```
# re_finditer.py
import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(
        text[s:e], s, e))
```

This example finds the same two occurrences of ab, and the Match instance shows where they are found in the original input.

```
$ python3 re_finditer.py 
Found 'ab' at 0:2
Found 'ab' at 5:7
```

#### 1.3.4 Pattern Syntax

Regular expressions support more powerful patterns than simple literal text strings. Patterns can repeat, can be anchored to different logical locations within the input, and can be expressed in compact forms that do not require every literal character to be present in the pattern. All of these features are used by combining literal text values with meta-characters that are part of the regular expression pattern syntax implemented by re.

```
# re_test_patterns.py
import re

def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return


if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa',
                  [('ab', "'a' followed by 'b'"),
                   ])
```

The following examples will use test_patterns() to explore how variations in patterns change the way they match the same input text. The output shows the input text and the substring range from each portion of the input that matches the pattern.

```
$ python3 re_test_patterns.py
'ab' ('a' followed by 'b')

  'abbaaabbbbaaaaa'
  'ab'
  .....'ab'
```

##### 1.3.4.1 Repetition

There are five ways to express repetition in a pattern. A pattern followed by the meta-character * is repeated zero or more times (allowing a pattern to repeat zero times means it does not need to appear at all to match). If the * is replaced with +, the pattern must appear at least once. Using ? means the pattern appears zero or one time. For a specific number of occurrences, use {m} after the pattern, where m is the number of times the pattern should repeat. Finally, to allow a variable but limited number of repetitions, use {m,n}, where m is the minimum number of repetitions and n is the maximum. Leaving out n ({m,}) means the value must appear at least m times, with no maximum.

```
# re_repetition.py
from re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('ab*', 'a followed by zero or more b'),
     ('ab+', 'a followed by one or more b'),
     ('ab?', 'a followed by zero or one b'),
     ('ab{3}', 'a followed by three b'),
     ('ab{2,3}', 'a followed by two to three b')],
)
```

There are more matches for ab* and ab? than ab+.

```
$ python3 re_repetition.py 
'ab*' (a followed by zero or more b)

  'abbaabbba'
  'abb'
  ...'a'
  ....'abbb'
  ........'a'

'ab+' (a followed by one or more b)

  'abbaabbba'
  'abb'
  ....'abbb'

'ab?' (a followed by zero or one b)

  'abbaabbba'
  'ab'
  ...'a'
  ....'ab'
  ........'a'

'ab{3}' (a followed by three b)

  'abbaabbba'
  ....'abbb'

'ab{2,3}' (a followed by two to three b)

  'abbaabbba'
  'abb'
  ....'abbb'
```

When processing a repetition instruction, re will usually consume as much of the input as possible while matching the pattern. This so-called greedy behavior may result in fewer individual matches, or the matches may include more of the input text than intended. Greediness can be turned off by following the repetition instruction with ?.

```
# re_repetition_non_greedy.py
from re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('ab*?', 'a followed by zero or more b'),
     ('ab+?', 'a followed by one or more b'),
     ('ab??', 'a followed by zero or one b'),
     ('ab{3}?', 'a followed by three b'),
     ('ab{2,3}?', 'a followed by two to three b')],
)
```

Disabling greedy consumption of the input for any of the patterns where zero occurrences of b are allowed means the matched substring does not include any b characters.

```

$ python3 re_repetition_non_greedy.py 
'ab*?' (a followed by zero or more b)

  'abbaabbba'
  'a'
  ...'a'
  ....'a'
  ........'a'

'ab+?' (a followed by one or more b)

  'abbaabbba'
  'ab'
  ....'ab'

'ab??' (a followed by zero or one b)

  'abbaabbba'
  'a'
  ...'a'
  ....'a'
  ........'a'

'ab{3}?' (a followed by three b)

  'abbaabbba'
  ....'abbb'

'ab{2,3}?' (a followed by two to three b)

  'abbaabbba'
  'abb'
  ....'abb'

```

##### 1.3.4.2 Character Sets

A *character set* is a group of characters, any one of which can match at that point in the pattern. For example, [ab] would match either a or b.

```
# re_charset.py
from re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('[ab]', 'either a or b'),
     ('a[ab]+', 'a followed by 1 or more a or b'),
     ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')],
)
```

The greedy form of the expression (a[ab]+) consumes the entire string because the first letter is a and every subsequent character is either a or b.

```
$ python3 re_charset.py 
'[ab]' (either a or b)

  'abbaabbba'
  'a'
  .'b'
  ..'b'
  ...'a'
  ....'a'
  .....'b'
  ......'b'
  .......'b'
  ........'a'

'a[ab]+' (a followed by 1 or more a or b)

  'abbaabbba'
  'abbaabbba'

'a[ab]+?' (a followed by 1 or more a or b, not greedy)

  'abbaabbba'
  'ab'
  ...'aa'

```

A character set can also be used to exclude specific characters. The carat (^) means to look for characters that are not in the set following the carat.

```
# re_charset_exclude.py
from re_test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation.',
    [('[^-. ]+', 'sequences without -, ., or space')],
)
```

This pattern finds all of the substrings that do not contain the characters -, ., or a space.

```
$ python3 re_charset_exclude.py
'[^-. ]+' (sequences without -, ., or space)

  'This is some text -- with punctuation.'
  'This'
  .....'is'
  ........'some'
  .............'text'
  .....................'with'
  ..........................'punctuation'
```

As character sets grow larger, typing every character that should (or should not) match becomes tedious. A more compact format using character ranges can be used to define a character set to include all of the contiguous characters between the specified start and stop points.

```
# re_charset_ranges.py
from re_test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation.',
    [('[a-z]+', 'sequences of lowercase letters'),
     ('[A-Z]+', 'sequences of uppercase letters'),
     ('[a-zA-Z]+', 'sequences of letters of either case'),
     ('[A-Z][a-z]+', 'one uppercase followed by lowercase')],
)
```

Here the range a-z includes the lowercase ASCII letters, and the range A-Z includes the uppercase ASCII letters. The ranges can also be combined into a single character set.

```
$ python3 re_charset_ranges.py
'[a-z]+' (sequences of lowercase letters)

  'This is some text -- with punctuation.'
  .'his'
  .....'is'
  ........'some'
  .............'text'
  .....................'with'
  ..........................'punctuation'

'[A-Z]+' (sequences of uppercase letters)

  'This is some text -- with punctuation.'
  'T'

'[a-zA-Z]+' (sequences of letters of either case)

  'This is some text -- with punctuation.'
  'This'
  .....'is'
  ........'some'
  .............'text'
  .....................'with'
  ..........................'punctuation'

'[A-Z][a-z]+' (one uppercase followed by lowercase)

  'This is some text -- with punctuation.'
  'This'

```

As a special case of a character set, the meta-character dot, or period (.), indicates that the pattern should match any single character in that position.

```
# re_charset_dot.py
from re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('a.', 'a followed by any one character'),
     ('b.', 'b followed by any one character'),
     ('a.*b', 'a followed by anything, ending in b'),
     ('a.*?b', 'a followed by anything, ending in b')],
)
```

Combining the dot with repetition can result in very long matches, unless the non-greedy form is used.

```
$ python3 re_charset_dot.py
'a.' (a followed by any one character)

  'abbaabbba'
  'ab'
  ...'aa'

'b.' (b followed by any one character)

  'abbaabbba'
  .'bb'
  .....'bb'
  .......'ba'

'a.*b' (a followed by anything, ending in b)

  'abbaabbba'
  'abbaabbb'

'a.*?b' (a followed by anything, ending in b)

  'abbaabbba'
  'ab'
  ...'aab'

```