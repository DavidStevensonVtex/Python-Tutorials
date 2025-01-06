import sys

nc = 0
while (c := sys.stdin.read(1)):
    nc += 1
print("%d" % nc)

# $ python char-count.py < rain-in-Spain.txt 
# 95
