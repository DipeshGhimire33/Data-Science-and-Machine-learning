# Using zip() to combine multiple lists.

names = ["Bhijan", "Hulash", "Dipesh", "Rujan"]
grades = ["A", "B", "C", "A", "P"]
ages = [16, 26, 32, 56, 55]

student_data = list(zip(names, grades, ages))

print(student_data)