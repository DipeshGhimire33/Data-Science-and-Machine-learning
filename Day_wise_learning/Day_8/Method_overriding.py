class Animal:
    """Represent a generic animal."""

    def __init__(self, name: str, age: int):
        """Initialize an animal."""
        self.name = name
        self.age = age

    def intro(self) -> str:
        """Return an introduction."""
        return f"Hello, I am {self.name}"

    def speak(self) -> str:
        """Return the generic animal sound."""
        return "I can speak"


class Cat(Animal):
    """Represent a cat."""

    def speak(self) -> str:
        """Return the sound made by a cat."""
        return "Meow"


cat = Cat("Rose", 7)

print(cat.speak())