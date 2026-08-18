# Basic multiple inheritance.


class Parent1:
    """Represent the first parent."""

    def parent1(self) -> None:
        """Display a message from Parent1."""
        print("This is Parent 1.")


class Parent2:
    """Represent the second parent."""

    def parent2(self) -> None:
        """Display a message from Parent2."""
        print("This is Parent 2.")


class Parent3:
    """Represent the third parent."""

    def parent1(self) -> None:
        """Display a message from Parent3."""
        print("This is Parent 3.")


class Child(Parent3, Parent2, Parent1):
    """Represent a child inheriting from three parents."""

    def child_of_3(self) -> None:
        """Display a message from the child."""
        print("This is the child.")


child = Child()

child.parent1()
child.parent2()
child.child_of_3()