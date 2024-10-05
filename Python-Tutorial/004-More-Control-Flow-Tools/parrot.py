# 4.9.2. Keyword Arguments

# Functions can also be called using keyword arguments of the
# form kwarg=value. For instance, the following function:


def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action="VOOOOOM")  # 2 keyword arguments
parrot(action="VOOOOOM", voltage=1000000)  # 2 keyword arguments
parrot("a million", "bereft of life", "jump")  # 3 positional arguments
parrot("a thousand", state="pushing up the daisies")  # 1 positional, 1 keyword

# Results
# -- This parrot wouldn't voom if you put 1000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !
# -- This parrot wouldn't voom if you put 1000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !
# -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !
# -- This parrot wouldn't VOOOOOM if you put 1000000 volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's a stiff !
# -- This parrot wouldn't jump if you put a million volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's bereft of life !
# -- This parrot wouldn't voom if you put a thousand volts through it.
# -- Lovely plumage, the Norwegian Blue
# -- It's pushing up the daisies !
