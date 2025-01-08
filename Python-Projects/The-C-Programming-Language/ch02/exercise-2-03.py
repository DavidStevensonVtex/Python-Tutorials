# Exercise 2-3: Write the function htoi(s), which converts a string of hexadecimal digit 
# (including an optional 0x or OX) into it equaivalent integer.

def htoi(s):
    i = 0
    s = s.lower()
    first_two = s[:2]
    # print("first_two", first_two)
    if first_two == "0x":
        s = s[2:]
    # print("s", s)
    total = 0
    for c in list(s):
        total *= 16
        # print(c, ord(c), ord(c))
        value = 0
        cvalue = ord(c)
        if (c >= '0' and c <= '9'):
            value = ord(c) - ord('0')
        elif (c >= 'a' and c <= 'f'):
            value = 10 + ord(c) - ord('a')
        else:
            print("Invalid character: ignored: ", c)
            continue

        total += value
        # print("value", value, "total", total)

    return total

print("B1", htoi("B1"))
print("0xB1", htoi("B1"))
print("ff", htoi("ff"))
print("0Xff", htoi("0xff"))
        
