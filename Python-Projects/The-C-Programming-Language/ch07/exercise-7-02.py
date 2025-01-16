# Exercise 7.2. Write a program that will print arbitrary input in a sensible way.
# as a minimum, it should print non-graphic characters in octal or hexadecimal
# according to local custom, and break long text lines.

# Note: match is not supported in Python 3.8, but is supported in Python 3.10
# $ python3 --version
# Python 3.8.10

# Other escape characters used in Python:

# Code	Result	Try it
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

import sys

MAX_LINE_LENGTH = 80

def isgraph(char):
    return char.isprintable() and not char.isspace()

outline = ""
output = ""
while line := sys.stdin.readline():
    index = 1
    outline = ""
    output = ""
    for c in line:
        if c == '\\':
            output = "\\\\"
        elif c == '\n':
            output = "\\n"
        elif c == '\r':
            output = "\\r"
        elif c == '\t':
            output = "\\t"
        elif c == '\b':
            output = "\\b"
        elif c == '\f':
            output = "\\f"
        else:
            if isgraph(c):
                output = c
            else:
                output = "\\x%.02x" % ord(c)

        if len(outline + output) >= MAX_LINE_LENGTH:
            print(outline + "\n", end="")
            outline = ""
        outline += output
        output = ""
    print(outline)

# $ python3 exercise-7-02.py < rain-in-Spain.txt 
# The\x20rain\x20in\x20Spain\x20falls\x20mainly\x20in\x20the\x20plain.\n
# \x20\x20\x20\x20abc\x20\x20\x20\x20\x20def\x20\x20\x20\x20\x20\\\\ghi\n
# It's\x20tough\x20to\x20make\x20predictions,\x20especially\x20about\x20the\x20fu
# ture.\n
# --\x20Yogi\x20Berra\n