# A non integer string like 'a' can not be converted to integer (will raise an error):

import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')

# $ python value-error.py 
#     arr = np.array(['a', '2', '3'], dtype='i')
# ValueError: invalid literal for int() with base 10: 'a'