# Basic calculator using a list of numbers.

number_of_variables = int(
    input("Enter the number of variables you want to perform an operation on: ")
)

numbers = [0] * number_of_variables

for i in range(number_of_variables):
    numbers[i] = float(input(f"Enter number {i + 1}: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = sum(numbers)
    print("Result:", result)

elif operation == "-":
    result = numbers[0] - sum(numbers[1:])
    print("Result:", result)

elif operation == "*":
    result = 1

    for number in numbers:
        result *= number

    print("Result:", result)

elif operation == "/":
    result = numbers[0]

    for number in numbers[1:]:
        if number == 0:
            print("Error: Division by zero is not allowed.")
            break

        result /= number
    else:
        print("Result:", result)

else:
    print("Error: Invalid operation.")