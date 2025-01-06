import sys

nwhite = nother = 0
ndigits = [0] * 10
 
while (c := sys.stdin.read(1)):
    if (c >= '0' and c <= '9'):
        ndigits[ord(c) - ord('0')] += 1
    elif (c == ' ' or c == '\n' or c == '\t'):
        nwhite += 1
    else:
        nother += 1

print("digits =", end = "")
for i in range(0, len(ndigits)):
    print(" %d" % ndigits[i], end = "")
print(", white space = %d, other = %d" % (nwhite, nother))

# $ python digit-count.py < rain-in-Spain.txt 
# digits = 0 1 1 0 0 0 0 0 0 0, white space = 19, other = 74