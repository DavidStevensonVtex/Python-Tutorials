# Most Values are True

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# Example
# The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# >>> bool("abc")
# True
# >>> bool(123)
# True
# >>> bool(["apple", "cherry", "banana"])
# True