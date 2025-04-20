class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)
        return cls.__instance

# Example usage:
s1 = Singleton()
s2 = Singleton()
print(s1 is s2) # Output: True