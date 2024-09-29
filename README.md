# Python-Tutorials

My self-training in Python

# [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

[Python web site](https://www.python.org/)

[The Python Language Reference](https://docs.python.org/3/reference/index.html)

[The Python Standard Library](https://docs.python.org/3/library/index.html)

## 2. Using the Python Interpreter

### 2.1. Invoking the Interpreter

```
python
Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep 6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

```
python -c command [arg]
```

```
python -m module [arg]
```

Typing an end-of-file character (`Control-D` on Unix, `Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status.

`quit()`

### 2.1.1. Argument Passing

`import sys`
`sys.argv[0]`

### 2.1.2. Interactive Mode

```
python
Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```

## 2.2. The Interpreter and Its Environment¶

### 2.2.1. Source Code Encoding

By default, Python source files are treated as encoded in UTF-8.

# 3. An Informal Introduction to Pytho

001-example.py:

```
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```

```
py .\001-example.py
```

## 3.1. Using Python as a Calculator

### 3.1.1. Numbers

```
py
Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5 # division always returns a floating-point number
1.6
>>> ^Z
```
