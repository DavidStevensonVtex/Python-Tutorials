from typing import List


# binsearch: find x in v[0] <= v[1] <= ... < v[n-1]
def binsearch(x: int, v: List[int]):
    low = 0
    high = len(v) - 1
    while low <= high:
        # floor division: // operator
        mid = (low + high) // 2
        if x < v[mid]:
            high = mid - 1
        elif x > v[mid]:
            low = mid + 1
        else:
            return mid
    return -1


vector = [1, 3, 5, 7, 9]
idx = binsearch(5, vector)
print(idx, vector[idx])

vector = [1, 3, 4, 6, 7, 9]
idx = binsearch(5, vector)
print(idx)

# $ python exercise-3-01.py
# 2 5
# -1
