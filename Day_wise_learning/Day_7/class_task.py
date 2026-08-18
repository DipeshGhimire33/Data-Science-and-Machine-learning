class Student:
    """Represent a student and their marks."""

    def __init__(self, name: str, *marks: int):
        """Initialize a student with a name and marks."""
        self.name = name
        self.marks = marks

    def total(self) -> int:
        """Return the total marks."""
        return sum(self.marks)

    def average(self) -> float:
        """Return the average marks."""
        return self.total() / len(self.marks)

    def display(self) -> None:
        """Display the student's name, total, and average marks."""
        print(f"Name: {self.name}")
        print(f"Total Marks: {self.total()}")
        print(f"Average Marks: {self.average()}")


student1 = Student("Dipesh", 60, 70, 80)
student1.display()