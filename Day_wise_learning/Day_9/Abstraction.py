import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for different shapes."""

    def __init__(self, length: float, breadth: float = 0, height: float = 0):
        """Initialize the dimensions of a shape."""
        self.length = length
        self.breadth = breadth
        self.height = height

    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area of the shape."""

    def volume(self) -> str:
        """Return a message when volume is not applicable."""
        return "Volume not applicable."


class Rectangle(Shape):
    """Represent a rectangle."""

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.length * self.breadth


rectangle = Rectangle(15, 20)

print(rectangle.area())
print(rectangle.volume())


class Cube(Shape):
    """Represent a cuboid using length, breadth, and height."""

    def area(self) -> float:
        """Return the total surface area."""
        return 2 * (
            self.length * self.breadth
            + self.breadth * self.height
            + self.height * self.length
        )


cube = Cube(15, 20, 15)

print(cube.area())


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius: float):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return math.pi * self.radius**2


circle = Circle(5)

print(round(circle.area(), 2))