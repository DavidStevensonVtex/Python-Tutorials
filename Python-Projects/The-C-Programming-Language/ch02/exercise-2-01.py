# Exercise 2-1. Write a program to determine the ranges of 
# char, short,int and long variables, both signed and unsigned.

# derived from /usr/include/limits.h

class Limits:
    SCHAR_MIN = -128
    CHAR_MIN = 127
    UCHAR_MAX = 255
    CHAR_MIN = 0

    SHRT_MIN = -32768
    SHRT_MAX = 32767
    USHRT_MAX = 65535

    INT_MAX = 2147483647
    INT_MIN = (-INT_MAX - 1)
    UINT_MAX = 4294967295

    LONG_MAX = 9223372036854775807
    LONG_MIN =(-LONG_MAX - 1)
    ULONG_MAX = 18446744073709551615

print("Limits.INT_MIN", Limits.INT_MIN)
print("Limits.UINT_MAX", Limits.UINT_MAX)
print("Limits.LONG_MIN", Limits.LONG_MIN)

# $ python exercise-2-1.py 
# Limits.INT_MIN -2147483648
# Limits.UINT_MAX 4294967295
# Limits.LONG_MIN -9223372036854775808