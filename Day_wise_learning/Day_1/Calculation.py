# Construction of basic calculator using python programming language, two variable at a time

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

c = input("Enter operation (+, -, *, /): ")

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero is not allowed.")    

# Construction of one time simple calculator is done.