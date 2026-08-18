class Animal:
    """Represent a generic animal."""

    def __init__(self, name: str, age: int):
        """Initialize an animal."""
        self.name = name
        self.age = age

    def intro(self) -> None:
        """Introduce the animal."""
        print(f"Hello, I am {self.name}")


class Cat(Animal):
    """Represent a cat."""

    def speak(self) -> str:
        """Return the sound made by a cat."""
        return "Meow"


class Tiger(Cat):
    """Represent a tiger."""

    def speak(self) -> str:
        """Return the sound made by a tiger."""
        return "Roar"


class Jaguar(Cat):
    """Represent a jaguar."""

    def speak(self) -> str:
        """Return the sound made by a jaguar."""
        return "Grrrr"


jaguar = Jaguar("Wilson", 13)

print(jaguar.speak())