import sys

while True:
    c = sys.stdin.read(1);
    if not c:
        break   # Exit the loop if no more input
    sys.stdout.write(c)

# $ python copy.py < rain-in-Spain.txt 
# 1. The rain in Spain falls mainly in the plain.
# 2. The rain in Spain falls mainly in the plain.