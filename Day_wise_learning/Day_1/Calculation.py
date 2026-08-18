# Basic calculator for two numbers.

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    if second_number != 0:
        print(first_number / second_number)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")