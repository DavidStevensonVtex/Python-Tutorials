import sys

PERMS = 0o666    # RW for owner, group, others
BUFSIZ = 512

if len(sys.argv) != 3:
    print("Usage: python3 copy-file-to-file.py inputfile outputfile", file=sys.stderr)
    exit(1)

with open(sys.argv[1], "rb") as inputfile:
    with open(sys.argv[2], "wb") as outputfile:
        outputfile.write(inputfile.read())

# $ python3 copy-file-to-file.py text.txt output.txt
# $ diff text.txt output.txt