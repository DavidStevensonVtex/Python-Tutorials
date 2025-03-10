# tarfile_getmember.py
import tarfile
import time

with tarfile.open('example.tar', 'r') as t:
    for filename in ['./tarfile.md', 'notthere.txt']:
        try:
            info = t.getmember(filename)
        except KeyError:
            print('ERROR: Did not find {} in tar archive'.format(
                filename))
        else:
            print('{} is {:d} bytes'.format(
                info.name, info.size))