import sys

line = ""
longest = line

while (line := sys.stdin.readline()):
    if (len(line) > len(longest)):
        longest = line

print("%s" % longest)

# $ python longest-line.py < longest-line.txt
# This is the longest line in this very short file.