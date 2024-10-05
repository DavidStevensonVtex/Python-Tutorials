# 4.9.5. Unpacking Argument Lists

# The reverse situation occurs when the arguments are already in a
# list or tuple but need to be unpacked for a function call requiring
# separate positional arguments. For instance, the built-in range()
# function expects separate start and stop arguments. If they are not
# available separately, write the function call with the *-operator
# to unpack the arguments out of a list or tuple:


print(list(range(3, 6)))  # normal call with separate arguments
# [3, 4, 5]
args = [3, 6]
print(list(range(*args)))  # call with arguments unpacked from a list
# [3, 4, 5]
