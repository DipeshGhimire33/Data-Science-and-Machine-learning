# Introduction to Python: Printing a message.

print("Hello to all! I am Dipesh Ghimire")


# Printing a message using user input.

name = input("Please enter your name: ")
print(f"Hello {name}! Welcome to the world of programming.")


# Printing a message on two lines.

print("Hello to all!\nI am Dipesh Ghimire")


# Using numeric data types.

age = 25
height = 5.9

print("Age:", age)
print("Height:", height)


# Using numeric data types with user input.

age = int(input("Please enter your age: "))
height = float(input("Please enter your height in feet: "))

print("Your age is:", age, "and your height is:", height)


# Using Boolean data types.

is_student = True
is_employed = False

print("Are you a student?", is_student)
print("Are you employed?", is_employed)


# Using user input with Boolean-style values.

is_student = input("Are you a student? (yes/no): ").lower()

print("Are you a student?", is_student)