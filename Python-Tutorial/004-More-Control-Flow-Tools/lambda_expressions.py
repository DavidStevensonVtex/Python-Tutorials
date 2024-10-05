# 4.9.6. Lambda Expressions

# Small anonymous functions can be created with the lambda keyword.
# This function returns the sum of its two arguments: lambda a, b: a+b.
# Lambda functions can be used wherever function objects are required.
# hey are syntactically restricted to a single expression. Semantically,
# they are just syntactic sugar for a normal function definition. Like
# nested function definitions, lambda functions can reference variables
# from the containing scope:


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
# 42
print(f(1))
# 43
