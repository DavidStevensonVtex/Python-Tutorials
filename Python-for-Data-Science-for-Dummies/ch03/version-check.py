import sys
print('Python Version:\n', sys.version)

import os
result = os.popen('conda --version').read()
print('\nAnaconda Version: \n', result)

result =os.popen('conda list notebook$').read()
print('\nJupyter Notebook Version:\n', result)