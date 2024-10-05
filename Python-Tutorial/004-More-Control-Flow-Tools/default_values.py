# The default values are evaluated at the point of function definition in the defining scope, so that

i = 5


def f(arg=i):
    print(arg)


i = 6
f()

# Results
# 5
