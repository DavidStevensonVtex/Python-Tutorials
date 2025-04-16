s1 = "a string"
s2 = s1
print(f"s1: {s1} s2: {s2}")
s1 = "another string"
print(f"s1 is now: {s1} s2 is now: {s2}")

# $ python strings-as-reference-types.py 
# s1: a string s2: a string
# s1 is now: another string s2 is now: a string