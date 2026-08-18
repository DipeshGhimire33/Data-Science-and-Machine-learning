class Example:
    """Demonstrate addition using a default argument."""

    def add(self, first, second, third=0):
        """Return the sum of two or three values."""
        return first + second + third


example = Example()

print(example.add(5, 4))
print(example.add(5, 4, 3))
print(example.add("5", "4", "9"))
print(round(example.add(5.657, 4.378), 2))


class ExampleOne:
    """Demonstrate addition using variable-length arguments."""

    def add(self, *args):
        """Return the sum of all provided numbers."""
        return sum(args)


example_one = ExampleOne()

print(example_one.add(45, 68.215, 49, 45, 55.55))