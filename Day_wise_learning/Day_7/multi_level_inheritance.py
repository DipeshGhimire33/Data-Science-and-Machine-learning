# Basic multilevel inheritance.


class Grandfather:
    """Represent a grandfather."""

    def grandfather_says(self) -> None:
        """Display a message from the grandfather."""
        print("I am your father's dad.")


class Father(Grandfather):
    """Represent a father."""

    def father_says(self) -> None:
        """Display a message from the father."""
        print("I am your father.")


class Child(Father):
    """Represent a child."""

    def child_says(self) -> None:
        """Display a message from the child."""
        print("I am a child.")


child = Child()

child.child_says()
child.father_says()
child.grandfather_says()


# Multilevel inheritance with employee information.


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Employee(Person):
    """Represent an employee."""

    def __init__(self, name: str, age: int, employee_id: int):
        super().__init__(name, age)
        self.employee_id = employee_id


class Manager(Employee):
    """Represent a manager."""

    def __init__(
        self,
        name: str,
        age: int,
        employee_id: int,
        department: str,
    ):
        super().__init__(name, age, employee_id)
        self.department = department

    def intro(self) -> None:
        """Display the manager's information."""
        print(
            self.name,
            self.age,
            self.employee_id,
            self.department,
        )


manager = Manager("Ram", 50, 15, "Finance")
manager.intro()