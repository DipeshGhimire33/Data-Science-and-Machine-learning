class Point:
    """Represent a point in a two-dimensional coordinate system."""

    def __init__(self, x: float, y: float):
        """Initialize a point with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Return the point as a string."""
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """Return a new point by adding two points."""
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Point(new_x, new_y)

    def __mul__(self, other):
        """Return a new point by multiplying two points."""
        new_x = self.x * other.x
        new_y = self.y * other.y

        return Point(new_x, new_y)

    def quadrant(self) -> str:
        """Return the quadrant or axis containing the point."""
        if not self.x and not self.y:
            return "origin"
        elif not self.x or not self.y:
            return "axis"

        quadrant_map = {
            (True, True): "first",
            (False, True): "second",
            (False, False): "third",
            (True, False): "fourth",
        }

        return quadrant_map[(self.x > 0, self.y > 0)]


point1 = Point(5, 4)
point2 = Point(5, 4)

point3 = point1 + point2
print(point3)

point4 = point1 * point2
print(point4)

point5 = Point(0, 1)

print(point1.quadrant())
print(point5.quadrant())