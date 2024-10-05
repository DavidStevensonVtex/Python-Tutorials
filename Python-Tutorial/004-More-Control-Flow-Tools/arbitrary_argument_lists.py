### 4.9.4. Arbitrary Argument Lists

# Finally, the least frequently used option is to specify that a
# function can be called with an arbitrary number of arguments.
# These arguments will be wrapped up in a tuple (see Tuples and Sequences).
# Before the variable number of arguments, zero or more normal arguments
# may occur.


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))
# earth/mars/venus
print(concat("earth", "mars", "venus", sep="."))
# earth/mars/venus
