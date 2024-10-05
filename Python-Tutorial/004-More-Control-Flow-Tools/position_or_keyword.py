def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)
standard_arg(arg=2)

# Results
# 2
# 2

pos_only_arg(1)
# Results
# 1

# pos_only_arg(arg=1)
# TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

# kwd_only_arg(3)
# TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
