# re_test_patterns_groups.py
import re

def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print('{!r} ({})\n'.format(pattern, desc))
        print('  {!r}'.format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            prefix = ' ' * (s)
            print(
                '  {}{!r}{} '.format(prefix,
                                     text[s:e],
                                     ' ' * (len(text) - e)),
                end=' ',
            )
            print(match.groups())
            if match.groupdict():
                print('{}{}'.format(
                    ' ' * (len(text) - s),
                    match.groupdict()),
                )
        print()
    return