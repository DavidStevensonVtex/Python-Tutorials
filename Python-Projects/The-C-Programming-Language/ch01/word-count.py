import sys

IN = 1
OUT = 0

state = OUT
nc = nl = nw = 0
while (c := sys.stdin.read(1)):
    nc += 1
    if (c == '\n'):
        nl += 1
    if (c == ' ' or c == '\n' or c == '\t'):
        state = OUT
    elif (state == OUT):
        state = IN
        nw += 1

print("%d %d %d" % (nl, nw, nc))

# $ python word-count.py < rain-in-Spain.txt 
# 1 20 95
