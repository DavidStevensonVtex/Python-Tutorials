# def foo(name, **kwds):
#     return "name" in kwds


# foo(1, **{"name": 2})
# TypeError: foo() got multiple values for argument 'name'


def foo(name, /, **kwds):
    return "name" in kwds


print(foo(1, **{"name": 2}))
# True
