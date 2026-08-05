
# Introduction Program "printing a message"

print("Hello to all! I am Dipesh Ghimire")

# Introduction Program "printing a message" with user input

name = input("Please enter your name: ")
print("Hello " + name + "! Welcome to the world of programming.")

# Introduction Program "printing a message" in two lines
print("Hello to all!" 
" I am Dipesh Ghimire")

# Introduction Program "Using numeric data types"
age = 25
height = 5.9
print("Age:", age)
print("Height:", height)

# Introduction Program "Using Numeric data types with user input"

age = int(input("Please enter your age: "))
height = float(input("Please enter your height in feet: "))
print("Your age is:", age, "and your height is:", height)


# Introduction Program "Using Boolean data types ( True or False)"
is_student = True
print("Are you a student?", is_student)
is_employed = False
print("Are you employed?", is_employed)

# Introduction Program "Using Boolean data types with user input"
is_student = input("Are you a student? (yes/no): ").lower()
#.Lower() method is used to convert the input to lowercase for easier comparison
print("Are you a student?", is_student)