# Basic Python programs.


# 1. Basic input and output

print("Hello user, please enter your name:")
name = input()

print(f"Hello {name}! Welcome to the program.")

age = input("Please enter your age: ")

confirmation = ""

while confirmation != "yes":
    confirmation = input(
        f"Are you sure you are {age} years old? (yes/no): "
    ).lower()

    if confirmation == "yes":
        print("Great! Let's continue.")
        print(f"Your name is {name} and your age is {age}.")
    else:
        age = input("Please enter your age again: ")


# 2. Temperature conversion

continue_conversion = "yes"

while continue_conversion == "yes":
    option = input(
        "\nPlease select the conversion you want to perform:\n"
        "1. Celsius to Fahrenheit\n"
        "2. Fahrenheit to Celsius\n"
        "3. Celsius to Kelvin\n"
        "4. Kelvin to Celsius\n"
        "5. Fahrenheit to Kelvin\n"
        "6. Kelvin to Fahrenheit\n"
        "Enter 1, 2, 3, 4, 5, or 6: "
    )

    if option == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    elif option == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

    elif option == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C is equal to {kelvin:.2f}K")

    elif option == "4":
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin}K is equal to {celsius:.2f}°C")

    elif option == "5":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = ((fahrenheit - 32) * 5 / 9) + 273.15
        print(f"{fahrenheit}°F is equal to {kelvin:.2f}K")

    elif option == "6":
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = ((kelvin - 273.15) * 9 / 5) + 32
        print(f"{kelvin}K is equal to {fahrenheit:.2f}°F")

    else:
        print("Invalid option.")

    continue_conversion = input(
        "Do you want to continue? (yes/no): "
    ).lower()


# 3. Calculate prime numbers from 1 to n.

n = int(input("Enter a number: "))
primes = []

for number in range(2, n + 1):
    is_prime = True

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)

print(primes)


# 4. Printing basic structures using loops.

for i in range(6):
    print("*" * i)

for i in range(6):
    print(" " * (6 - i) + "*" * i)

for i in range(6):
    print(" " * (6 - i) + "* " * i)


# 5. Separating the digits of numbers in a list.

numbers = [5, 32, 6, 77, 64, 69, 11]
digits = []

for number in numbers:
    tens = number // 10
    ones = number % 10

    if tens != 0:
        digits.append(tens)

    digits.append(ones)

    print(digits)