import sys

def main():
    command = sys.argv[0].strip()
    toLower = True if command == "lower.py" else False
    toUpper = True if command == "upper.py" else False
    while line := sys.stdin.readline():
        if command == "lower.py": line = line.lower()
        if command == "upper.py": line = line.upper()
        print(line, end="")

main()

# $ python3 lower.py < rain-in-Spain.txt 
# the rain in spain falls mainly in the plain.

# it's tough to make predictions, especially about the future.
# -- yogi berra

# $ python3 upper.py < rain-in-Spain.txt 
# THE RAIN IN SPAIN FALLS MAINLY IN THE PLAIN.

# IT'S TOUGH TO MAKE PREDICTIONS, ESPECIALLY ABOUT THE FUTURE.
# -- YOGI BERRA