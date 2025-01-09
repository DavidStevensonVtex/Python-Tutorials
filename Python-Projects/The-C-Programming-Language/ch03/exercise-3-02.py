import sys

nwhite = nother = 0
ndigit = [0] * 10
while c := sys.stdin.read(1):
    match c:
        case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
            ndigit[ord(c) - ord("0")] += 1
        case " " | "\n" | "\t" | "\r":
            nwhite += 1
        case _:
            nother += 1

print("digits =", end="")
for i in range(0, len(ndigit)):
    print(" %d" % ndigit[i], end="")
print(", white space = %d, other = %d" % (nwhite, nother))

# $ python exercise-3-02.py < rain-in-Spain.txt
# digits = 1 3 2 1 1 1 1 1 1 1, white space = 30, other = 74
