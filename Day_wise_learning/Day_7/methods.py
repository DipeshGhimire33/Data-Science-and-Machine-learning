# Instance, class, and static methods.


class Person:
    """Represent a person."""

    count = 0

    def __init__(self, name: str, address: str = "Kathmandu"):
        """Initialize a person."""
        self.name = name
        self.address = address
        Person.count += 1

    def get_details(self) -> None:
        """Display the person's details."""
        print(f"I am {self.name} from {self.address}")

    @classmethod
    def get_count(cls) -> int:
        """Return the total number of Person objects created."""
        return cls.count

    @staticmethod
    def get_full_name(first_name: str, last_name: str) -> None:
        """Display a person's full name."""
        print(f"Hello Mr. {last_name} {first_name}")


person1 = Person("Rujan", "Jhapa")

person1.get_details()
person1.get_full_name("Rujan", "Katwal")