# Exercise 2-10. Rewrite the function lower, which converts upper case letters to lower case, 
# with a conditional expression instead of if-else.

def lower(s1):
    newstr = ""
    for c in s1:
        newstr += (chr(ord(c) - ord('A') + ord('a')) if c >= 'A' and c <= 'Z' else c)
    return newstr

str = "The rain in Spain falls mainly in the plain."
print(repr(str), repr(lower(str)))

# $ python exercise-2-10.py
# 'The rain in Spain falls mainly in the plain.' 'the rain in spain falls mainly in the plain.'