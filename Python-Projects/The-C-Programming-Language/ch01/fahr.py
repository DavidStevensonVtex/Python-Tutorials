lower = 0
upper = 300
step = 20

fahr = lower
while (fahr <= upper):
    celsius = 5 * (fahr-32) / 9
    print("%d\t%d" %  (fahr, celsius))
    fahr = fahr + step

# 0       -17
# 20      -6
# 40      4
# 60      15
# 80      26
# 100     37
# 120     48
# 140     60
# 160     71
# 180     82
# 200     93
# 220     104
# 240     115
# 260     126
# 280     137
# 300     148