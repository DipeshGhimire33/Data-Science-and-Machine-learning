class AccessModifierExample:
    """Demonstrate public, protected, and private attributes and methods."""

    def __init__(self):
        self.public_attr = 1
        self.__private_attr = 2
        self._protected_attr = 3

    def public(self) -> None:
        """Demonstrate a public method."""
        print("Public method")

    def __private(self) -> None:
        """Demonstrate a private method."""
        print("Private method")

    def _protected(self) -> None:
        """Demonstrate a protected method."""
        print("Protected method")


obj = AccessModifierExample()

obj.public()
# obj.__private()
obj._protected()