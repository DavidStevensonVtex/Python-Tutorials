# string_constants.py
import inspect
import string


def is_str(value):
    return isinstance(value, str)


for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))

# $ python3 string_constants.py 
# ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ascii_lowercase='abcdefghijklmnopqrstuvwxyz'

# ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# digits='0123456789'

# hexdigits='0123456789abcdefABCDEF'

# octdigits='01234567'

# printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

# punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# whitespace=' \t\n\r\x0b\x0c'