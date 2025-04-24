def zip_add(list1: list, list2: list) -> list:
    if len(list1) != len(list2):
        raise ValueError("Expected lists of the same length")

    return [a + b for a, b in zip(list1, list2)]


zip_add([1, 2, 3], ["abc", "def", "ghi"])
