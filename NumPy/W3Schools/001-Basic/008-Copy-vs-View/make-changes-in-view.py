# Make Changes in the VIEW:
# Make a view, change the view, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

# $ python make-changes-in-view.py 
# [31  2  3  4  5]
# [31  2  3  4  5]