def power(base, n):
    p = 1
    for i in range(1, n+1):
        p = p * base
    return p

for i in range(0, 10):
    print("%d %d %d" % (i, power(2,i), power(-3,i)))

# $ python power-function.py
# 0 1 1
# 1 2 -3
# 2 4 9
# 3 8 -27
# 4 16 81
# 5 32 -243
# 6 64 729
# 7 128 -2187
# 8 256 6561
# 9 512 -19683