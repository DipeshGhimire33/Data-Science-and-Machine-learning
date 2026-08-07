# Construction of calculator using List, two variable at a time ,

a= int(input("enter the no of variables you want to perform operation on: "))
x = [0] * a             # creates a list of size 'a' initialized with zeros

for i in range(a):
    x[i] = float(input("Enter number {}: ".format(i + 1)))          #format(i+1) displays the number of variable being entered

b = input("Enter operation (+, -, *, /): ")

if b == '+':
    result = sum(x)  # Sum all numbers in the list
    print("Result:", result)
elif b == '-':
    print("Result:", x[0] - sum(x[1:]))  # Subtract all subsequent numbers from the first
elif b == '*':
    result = 1
    for num in x:
        result *= num  # Multiply all numbers in the list
    print("Result:", result)
elif b == '/':
    result = x[0]
    for num in x[1:]:                       #x[1:] means all elements of the list x starting from index 1 to the end of the list
        if num != 0:
            result /= num  # Divide the result by each subsequent number
        else:
            print("Error: Division by zero is not allowed.")
            break
    else:
        print("Result:", result)


# List operations was used to make a calculator




        