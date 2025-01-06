import sys

nl = 0
while (line := sys.stdin.readline()):
    nl += 1
print("%d" % nl)

# $ python line-count.py < rain-in-Spain.txt
# 1