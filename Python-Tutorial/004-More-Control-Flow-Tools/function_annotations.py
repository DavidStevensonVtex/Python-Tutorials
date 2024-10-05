# 4.9.8. Function Annotations

# Function annotations are completely optional metadata information
# about the types used by user-defined functions (see PEP 3107 and
# PEP 484 for more information).

# Annotations are stored in the __annotations__ attribute of the function
# as a dictionary and have no effect on any other part of the function.


def f(ham: str, eggs: str = "eggs") -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs


print(f("spam"))
# Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
# Arguments: spam eggs
# 'spam and eggs'
