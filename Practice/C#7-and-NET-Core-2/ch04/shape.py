from abc import ABC, abstractmethod

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"(width: {self.width} height: {self.height})"


class Shape(ABC):
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def draw(self):
        print(f"(position: {self.position}, size: {self.size})")

    def move(self, newPosition):
        self.position.x = newPosition.x
        self.position.y = newPosition.y

    @abstractmethod
    def resize(self, width, height):
        pass
        

class Rectangle(Shape):
    def __init__(self, position, size):
        super().__init__(position, size)

    def draw(self):
        print(f"Rectangle with {self.position}, size: {self.size}")

    def move(self, newPosition):
        super().move(newPosition)

    def resize(self, width, height):
        self.size.width = width
        self.size.height = height

class Ellipse(Shape):
    def __init__(self, position, size):
        super().__init__(position, size)

    def draw(self):
        print(f"Ellipse with {self.position}, size: {self.size}")

    def move(self, newPosition):
        super().move(newPosition)

    def resize(self, width, height):
        self.size.width = width
        self.size.height = height

# TypeError: Can't instantiate abstract class Rectangle with abstract method resize
r = Rectangle(Position(12, 34), Size(5, 7))
r.draw()
r.move(Position(123, 456))
r.draw()

r.resize(25, 29)
r.draw()

print()
e = Ellipse(Position(56, 78), Size(11, 13))
e.draw()
e.resize(31, 37)
e.draw()

# $ python shape.py
# Rectangle with (x: 12, y: 34), size: (width: 5 height: 7)
# Rectangle with (x: 123, y: 456), size: (width: 5 height: 7)
# Rectangle with (x: 123, y: 456), size: (width: 25 height: 29)

# Ellipse with (x: 56, y: 78), size: (width: 11 height: 13)
# Ellipse with (x: 56, y: 78), size: (width: 31 height: 37)