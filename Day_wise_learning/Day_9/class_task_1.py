class Pet:
    """Represent a pet with children and controlled energy."""

    def __init__(self, name: str, children=None, energy: int = 50):
        """Initialize a pet."""
        self.name = name
        self.children = children if children is not None else []
        self.__energy = 0

        self.set_energy(energy)

    def get_energy(self) -> int:
        """Return the pet's energy level."""
        return self.__energy

    def set_energy(self, value: int) -> None:
        """Set energy while keeping it between 0 and 100."""
        value = int(value)

        if value > 100:
            self.__energy = 100
        elif value < 0:
            self.__energy = 0
        else:
            self.__energy = value

    def add_child(self, *children) -> None:
        """Add one or more children."""
        self.children.extend(children)

    def display(self) -> None:
        """Display the pet's details."""
        print(
            f"My name is {self.name}, "
            f"with children {self.children}, "
            f"and energy {self.__energy}."
        )


pet1 = Pet("Ruby", energy=150)
pet2 = Pet("Rose", energy=60)


class RoboPet(Pet):
    """Represent a pet with increased energy."""

    def set_energy(self, value: int) -> None:
        """Increase the given energy by 20% before setting it."""
        value = 1.2 * value
        super().set_energy(value)


grandpa = RoboPet("Roman_Reigns", energy=20)

grandpa.add_child(pet1)
grandpa.add_child(pet2)


def get_total_family_energy(pet: Pet) -> int:
    """Return the energy of a pet and its direct children."""
    total_energy = pet.get_energy()

    for child in pet.children:
        total_energy += child.get_energy()

    return total_energy


print(get_total_family_energy(grandpa))