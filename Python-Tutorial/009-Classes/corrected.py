class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")

print("Fido's tricks: ", d.tricks)
print("Buddy's tricks: ", e.tricks)

# $ python corrected.py
# Fido's tricks:  ['roll over']
# Buddy's tricks:  ['play dead']
