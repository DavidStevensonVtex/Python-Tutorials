# Exercise 2-5. Write the function any(s1,s2) which returns the first location
# in the string s1 where any character from the string s2 occurs, or -1 if s1
# contains no characters from s2. (The standard library function strpbrk does the 
# same job but returns a pointer to the location.)

def any(s1, s2):
    i = 0
    for c in s1:
        if c in s2:
            return s1[i:]
        i += 1
    return None


str = " squeeze  ;  me  :  tight   "
print(repr(str), repr(any(str, ";:")))
print()

str = "squeeze me tight"
print(repr(str), repr(any(str, ";:")))

# $ python exercise-2-5.py
# ' squeeze  ;  me  :  tight   ' ';  me  :  tight   '

# 'squeeze me tight' None