import sys

pattern = "ould"

line = ""
while line := sys.stdin.readline():
    if pattern in line:
        print(line, end="")

# $ python exercise-4-1.py < letter.txt
# Ah Love! could you ad I with Fate conspire
# Would not we shatter it to bits -- and then
# Re-mould it nearer to the Heart's Desire!
