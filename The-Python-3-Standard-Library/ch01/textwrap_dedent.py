# textwrap_dedent.py
import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
print('Dedented:')
print(dedented_text)

# $ python3 textwrap_dedent.py 
# Dedented:

# The textwrap module can be used to format text for output in
# situations where pretty-printing is desired.  It offers
# programmatic functionality similar to the paragraph wrapping
# or filling features found in many text editors.