# Chapter 2: [Data Structures](https://pymotw.com/3/data_structures.html)

## [2.7 struct — Binary Data Structures](https://pymotw.com/3/struct/index.html)

Purpose:	Convert between strings and binary data.

The [struct module](https://docs.python.org/3/library/struct.html) includes functions for converting between strings of bytes and native Python data types such as numbers and strings.

### 2.7.1 Functions versus Struct Class

A set of module-level functions is available for working with structured values, as well as the Struct class. Format specifiers are converted from their string format to a compiled representation, similar to the way regular expressions are handled. The conversion takes some resources, so it is typically more efficient to do it once when creating a Struct instance and call methods on the instance instead of using the module-level functions. All of the following examples use the Struct class.