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
        return "meow"


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> str:
        """Return the sound made by a dog."""
        return "woof"


cat = Cat("Ruby", 5)

cat.intro()
print(cat.speak())