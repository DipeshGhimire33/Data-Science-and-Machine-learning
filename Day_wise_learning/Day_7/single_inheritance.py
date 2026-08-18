class Animal:
    """Represent an animal."""

    def __init__(self, name: str, age: int):
        """Initialize an animal."""
        self.name = name
        self.age = age

    def intro(self) -> None:
        """Display a basic introduction."""
        print(f"Hello, I am {self.name}")


class Cat(Animal):
    """Represent a cat."""

    def __init__(self, name: str, age: int, color: str):
        """Initialize a cat."""
        super().__init__(name, age)
        self.color = color

    def details(self) -> None:
        """Display the cat's details."""
        print(
            f"Hello, I am {self.name}, "
            f"age: {self.age}, color: {self.color}"
        )


cat = Cat("Ruby", 5, "Purple")

cat.intro()
cat.details()