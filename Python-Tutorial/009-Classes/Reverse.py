class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
rev = Reverse('spam')
print("iter(rev)", iter(rev))
for char in rev:
    print(char, end=" ")
print()

# $ python Reverse.py
# iter(rev) <__main__.Reverse object at 0x000001F5D945A690>
# m a p s 