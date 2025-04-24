from typing import Union


def print_thing(thing: Union[str, int]) -> None:
    if isinstance(thing, str):
        print("string", thing)
    else:
        print("number", thing)


print_thing("abc")
print_thing(123)
