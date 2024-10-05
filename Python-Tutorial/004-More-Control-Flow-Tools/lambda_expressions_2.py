# 4.9.6. Lambda Expressions

# Another use of lambda functions is to pass a small function as an argument:

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
# [(4, "four"), (1, "one"), (3, "three"), (2, "two")]
