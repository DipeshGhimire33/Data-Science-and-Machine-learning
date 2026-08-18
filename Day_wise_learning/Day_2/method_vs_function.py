# Basic use of a function.


def add_number(number):
    """Return the given number."""
    return number


number_of_values = int(input("Enter the number of values you want to add: "))
total = 0

for i in range(number_of_values):
    number = int(input(f"Enter number {i + 1}: "))
    total += add_number(number)

print("Sum:", total)


# Basic use of a class.


class Calculator:
    """Perform basic area and volume calculations."""

    def __init__(self, length, breadth):
        """Initialize the length and breadth."""
        self.length = length
        self.breadth = breadth

    def area(self):
        """Return the area of a rectangle."""
        return self.length * self.breadth

    def volume(self, height):
        """Return the volume of a cuboid."""
        return self.length * self.breadth * height


choice = input(
    "Do you want to calculate area or volume? "
).lower()

if choice == "area":
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))

    result = Calculator(length, breadth).area()

elif choice == "volume":
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    height = int(input("Enter height: "))

    result = Calculator(length, breadth).volume(height)

else:
    result = None
    print("Invalid choice.")

if result is not None:
    print(f"The result is {result}")