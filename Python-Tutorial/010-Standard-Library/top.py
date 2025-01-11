import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

# $ python3 top.py --lines=5 alpha.txt beta.txt
# Namespace(filenames=['alpha.txt', 'beta.txt'], lines=5)