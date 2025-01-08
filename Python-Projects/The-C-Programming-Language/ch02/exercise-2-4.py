# Exercise 2-4: Write an alternate version of squeeze(s1, s2) that deletes each character in s1
# that matches any character in the string s2

def squeeze(s1, s2):
    newstring = ""
    for s in s1:
        skip = False
        if s in s2:
            skip = True
        if not skip:
            newstring += s
    return newstring

str = " squeeze  ;  me  :  tight   "
print(repr(str), repr(squeeze(str, " ;:")))