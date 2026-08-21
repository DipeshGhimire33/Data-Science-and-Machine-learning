class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    # Getter
    @property
    def age(self):
        print("Getter called")
        return self._age

    # Setter
    @age.setter
    def age(self, value):
        print("Setter called")

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value

    # Deleter
    @age.deleter
    def age(self):
        print("Deleter called")
        del self._age


# Create object
student = Student("John", 20)

# Getter
print(student.age)

# Setter
student.age = 25
print(student.age)

# Deleter
del student.age

# This will cause an AttributeError because _age was deleted
print(student.age)