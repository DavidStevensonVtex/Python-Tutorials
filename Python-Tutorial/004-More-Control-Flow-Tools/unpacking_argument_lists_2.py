# 4.9.5. Unpacking Argument Lists

# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:


def parrot(voltage, state="a stiff", action="voom"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.", end=" ")
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
# -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
