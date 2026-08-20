try:
    num = int(input("Enter a number:"))
    print(6 / num)
    
except ValueError:
    print("Innvalid Input")
    
except ZeroDivisionError:
    print("Cannot divide by zero")