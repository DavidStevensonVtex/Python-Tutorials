def identity(arg: Any) -> Any:
    return arg


print(identity(identity(42)))
